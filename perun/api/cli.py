"""Command line api definition.

Uses click https://click.palletsprojects.com/en/8.1.x/ to manage complex cmdline configurations.
"""
import json
import sys
from pathlib import Path
from typing import Optional

import click

import perun
from perun import log
from perun.configuration import config, read_custom_config, save_to_config_callback
from perun.io.io import IOFormat
from perun.perun import Perun


@click.group()
@click.version_option(version=perun.__version__)
@click.option(
    "-c",
    "--configuration",
    default="./.perun.ini",
    help="Path to configuration file",
    type=click.Path(exists=False, dir_okay=False, readable=True),
    is_eager=True,
    callback=read_custom_config,
    expose_value=False,
)
@click.option(
    "-l",
    "--log_lvl",
    type=click.Choice(["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]),
    help="Loggging level",
    callback=save_to_config_callback,
    expose_value=False,
)
def cli():
    """Perun: Energy measuring and reporting tool."""
    log.setLevel(config.get("debug", "log_lvl"))


@cli.command()
@click.option(
    "--default",
    is_flag=True,
    show_default=True,
    default=False,
    help="Print default configuration",
)
def showconf(default: bool):
    """Print current perun configuration in INI format."""
    import sys

    from perun.configuration import _default_config

    if default:
        config.read_dict(_default_config)
        config.write(sys.stdout)
    else:
        config.write(sys.stdout)


@cli.command()
def sensors():
    """Print sensors assigned to each rank by perun."""
    perun = Perun(config)
    if perun.comm.Get_rank() == 0:
        for rank, bes in enumerate(perun.sensors_config):
            click.echo(f"Rank: {rank}")
            for key, items in bes.items():
                if len(items) > 0:
                    click.echo(f"   {key}:")
                    for device in items:
                        click.echo(f"       {device}")
                    click.echo("")

        click.echo("Hostnames: ")
        for host, ranks in perun.host_rank.items():
            click.echo(f"   {host}: {ranks}")


@cli.command()
def metadata():
    """Print global metadata dictionaries in json format."""
    perun = Perun(config)

    hostMD = perun.l_host_metadata
    hostMD["backends"] = perun.l_backend_metadata
    allHostsMD = perun.comm.gather(hostMD, root=0)

    if perun.comm.Get_rank() == 0 and allHostsMD:
        metadataDict = {}
        for host, assignedRanks in perun.host_rank.items():
            metadataDict[host] = allHostsMD[assignedRanks[0]]

        json.dump(metadataDict, sys.stdout, indent=4)


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument(
    "output_format",
    type=click.Choice([format.value for format in IOFormat]),
)
@click.option(
    "-i",
    "--id",
    "mr_id",
    type=str,
    default=None,
)
def export(input_file: str, output_format: str, mr_id: Optional[str]):
    """Export existing perun output file to another format."""
    in_file = Path(input_file)
    if not in_file.exists():
        click.echo("File does not exist.", err=True)
        return

    perun = Perun(config)

    out_path = in_file.parent
    inputFormat = IOFormat.fromSuffix(in_file.suffix)
    out_format = IOFormat(output_format)

    dataNode = perun.import_from(in_file, inputFormat)
    perun.export_to(out_path, dataNode, out_format, mr_id)


@cli.command(context_settings={"ignore_unknown_options": True})
# Output option
@click.option(
    "-n",
    "--app_name",
    help="Name of the monitored application. The name is used to distinguish between multiple applications in the same directory. If left empty, the filename will be  used.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "-i",
    "--run_id",
    help="Unique id of the latest run of the application. If left empty, perun will use the SLURM job id, or the current date.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "-f",
    "--format",
    type=click.Choice([format.value for format in IOFormat]),
    help="Report format.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "--data_out",
    type=click.Path(exists=False, dir_okay=True, file_okay=False),
    help="Where to save the output files, defaults to the current working directory.",
    callback=save_to_config_callback,
    expose_value=False,
)
# Sampling Options
@click.option(
    "--sampling_rate",
    type=float,
    help="Sampling rate in seconds.",
    callback=save_to_config_callback,
    expose_value=False,
)
# Post processing options
@click.option(
    "--pue",
    type=float,
    help="Data center Power Usage Efficiency.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "--emissions_factor",
    type=float,
    help="Emissions factor at compute resource location.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "--price_factor",
    type=float,
    help="Electricity price factor at compute resource location.",
    callback=save_to_config_callback,
    expose_value=False,
)
# Benchmarking
@click.option(
    "--rounds",
    type=int,
    help="Number of rounds to run the app.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "--warmup_rounds",
    type=int,
    help="Number of warmup rounds to run the app.",
    callback=save_to_config_callback,
    expose_value=False,
)
@click.option(
    "-m",
    "--module",
    help="Run script 'path/to/script.py' as a module (eq. to python -m path.to.script) instead of "
         "as a standard top-level script (eq. to python path/to/script.py).",
    is_flag=True,
)
@click.argument("script", type=click.Path(exists=True))
@click.argument("script_args", nargs=-1)
def monitor(
        module: bool,
        script: str,
        script_args: tuple,
):
    """
    Gather power consumption from hardware devices while SCRIPT [SCRIPT_ARGS] is running.

    SCRIPT is a path to the python script to monitor, run with arguments SCRIPT_ARGS.
    MONITOR is a boolean which, when set to True, runs SCRIPT as a module.
    """
    # Setup script arguments

    import sys

    perun = Perun(config)

    filePath: Path = Path(script)
    log.debug(f"Script path: {filePath}")

    if module:
        # find root package path to add to sys.path
        # (either it doesn't contain an __ini__.py or does plus requirements / .git)
        # todo: This doesn't necessarily cover all cases...
        pkgPath = filePath.absolute().parent
        while pkgPath:
            initFile = Path(pkgPath, "__init__.py")
            if (not initFile.is_file() or
                    (initFile.is_file() and any(file.name.startswith("requirements") for file in
                                                pkgPath.iterdir() if file.is_file())) or
                    (initFile.is_file() and Path(pkgPath, ".git").is_dir())
            ):
                break
            pkgPath = pkgPath.parent

        # construct the module name
        moduleStr = str(filePath.absolute().relative_to(pkgPath).with_suffix('')).replace('/', '.')
        sys.argv = [moduleStr] + list(script_args)
        # add project root directory as system path to search through
        sys.path.insert(0, str(pkgPath))
    else:
        # if running as a script, keep the original script path
        moduleStr = None
        sys.argv = [script] + list(script_args)
        # add parent directory to system paths to search through
        sys.path.insert(0, str(filePath.parent.absolute()))

    log.debug(f"Script args: {sys.argv}")

    perun.monitor_application(filePath, moduleStr)


def main():
    """Cli entrypoint."""
    cli(auto_envvar_prefix="PERUN")
