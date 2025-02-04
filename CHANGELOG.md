# CHANGELOG



## v0.4.0 (2023-08-18)

### Feature

* feat: Perun Singleton Class


BREAKING CHANGE:
Rework of main perun modules to enable regions.
Deprecated old monitor decorator in favour of &#39;function monitoring&#39;
Changes to output files, always produces a hdf5, and an optional second file (default text report)

Individual Commits
* wip: created perun class, created singleton decorator, removed backend decorator
* wip: removed _cached_sensors_config from coordination, handled by perun class
* wip: perun class progress, removed decorator
* wip: decorator is back on (sadly), started export command refactoring
* refactor: export command and configuration options (removed depth and raw options)
* refactor: changed api, removed bench prefix, commeted decorator out
* fix: corrections in suprocess and backends
* refactor: return to single file that acumulates everything, but slightly different
* fix: intel_rapl dram max value, wrong overwriting of hdf5 file
* wip: regions
* feat: regions
* fix: overlapping id correction
* refactor: metadata storage
* feat: actual regions
* refactor: io formating
* fix: io fixes
* fix: regions metric units, dependencies
* fix: gpu utilization and memory
* fix: formatting
* fix: missing total run node.
* wip:update docs
* docs: updated docs
* test: updated tests
* ci: appeasing mypy
* [pre-commit.ci] auto fixes from pre-commit.com hooks for more information, see https://pre-commit.ci
* ci: pydocstyle ignores docs/
---------

Co-authored-by: io3047@kit.edu &lt;io3047@hkn1990.localdomain&gt;
Co-authored-by: pre-commit-ci[bot] &lt;66853113+pre-commit-ci[bot]@users.noreply.github.com&gt; ([`574b340`](https://github.com/Helmholtz-AI-Energy/perun/commit/574b3408ad5e9d7ce9cde5d16ae7ae95e9c53b83))

### Unknown

* Merge branch &#39;release&#39; ([`aa53d94`](https://github.com/Helmholtz-AI-Energy/perun/commit/aa53d948d06ed6ad77d20b206765452e35c4992c))


## v0.3.3 (2023-07-24)

### Documentation

* docs: OpenSSF badge ([`bebc329`](https://github.com/Helmholtz-AI-Energy/perun/commit/bebc3296fbcaf621c5af34aaf6326c8c5b9a8e8e))

### Unknown

* Update README.md ([`74887f1`](https://github.com/Helmholtz-AI-Energy/perun/commit/74887f157e01c7a078826fff3ecb94ab345838f6))


## v0.3.2 (2023-06-02)

### Unknown

* 0.3.2

0.3.2 [skip ci] ([`14731b6`](https://github.com/Helmholtz-AI-Energy/perun/commit/14731b6a9bea39304cd8deae7b46e8a93135c507))

* Merge branch &#39;release&#39; ([`b3884c5`](https://github.com/Helmholtz-AI-Energy/perun/commit/b3884c5e5598e985d13ffaf8446f99520ae5a706))


## v0.3.1 (2023-06-01)

### Documentation

* docs: updated fair badge ([`827557d`](https://github.com/Helmholtz-AI-Energy/perun/commit/827557d5ffd0828cb168577d471219fe1e7fcee1))

* docs: Zenodo badge ([`c1043c5`](https://github.com/Helmholtz-AI-Energy/perun/commit/c1043c563166aedeef51da4c5c64ea8323836d31))

### Unknown

* 0.3.1

0.3.1 [skip ci] ([`a7e50f3`](https://github.com/Helmholtz-AI-Energy/perun/commit/a7e50f3483e1393fc3c6c6980273d70e9da8d977))


## v0.3.0 (2023-05-31)

### Documentation

* docs: fair-software badge (#47)

* docs: fair-software action

* docs: added fair badge to readme

* docs: more badges

* fix: badge formating

* docs: downloads badge

* ci: limit fair action to pushes to main ([`34585cd`](https://github.com/Helmholtz-AI-Energy/perun/commit/34585cd8f3d353c1e2591a498004677a8315864c))

### Feature

* feat: extra host metadata ([`f576046`](https://github.com/Helmholtz-AI-Energy/perun/commit/f57604625e3072391e76a55945dce63d72e038b2))

### Unknown

* 0.3.0

0.3.0 [skip ci] ([`f4b6f19`](https://github.com/Helmholtz-AI-Energy/perun/commit/f4b6f19b8985a9130b931caa76e8c00fc378aaaf))

* Merge branch &#39;release&#39; ([`7eb62a0`](https://github.com/Helmholtz-AI-Energy/perun/commit/7eb62a0e37ae9c21f539d8dc3b675760746761db))

* Update README.md

Added whitespace in the README to get spacing between logo and badges ([`57f15bf`](https://github.com/Helmholtz-AI-Energy/perun/commit/57f15bff0e25b662ab782eebb782cf335d31c63e))


## v0.2.0 (2023-03-28)

### Documentation

* docs: update README.md

* 0.1.1

0.1.1 [skip ci]

* docs: updated readme

* docs: data structure image

* docs: code snipet correction

---------

Co-authored-by: github-actions &lt;github-actions@github.com&gt; ([`7880070`](https://github.com/Helmholtz-AI-Energy/perun/commit/7880070307497cb213effd2d1387afbd88435e99))

### Unknown

* 0.2.0

0.2.0 [skip ci] ([`09c2ad1`](https://github.com/Helmholtz-AI-Energy/perun/commit/09c2ad1d0e9532a63022a334f4e7ab142ea1ddcb))

* quickfix release #38

feat: co2 and money in text summary
fix: removed minimal bench format option
docs: updated docs
fix: ignoring psys object in rapl interface
fix: fix start event for non measuring mpi ranks ([`926ac32`](https://github.com/Helmholtz-AI-Energy/perun/commit/926ac3238e4bfbfd33586600c9829d96e70a067e))

* Merge branch &#39;release&#39; ([`3b6c628`](https://github.com/Helmholtz-AI-Energy/perun/commit/3b6c628375987aef174de52a821ede237213128c))


## v0.1.1 (2023-03-22)

### Unknown

* 0.1.1

0.1.1 [skip ci] ([`ce70bf8`](https://github.com/Helmholtz-AI-Energy/perun/commit/ce70bf8ab9685d06e5aff6ebfd1bc09f86d9fab6))

* 0.1.0

0.1.0 [skip ci] ([`d40a45e`](https://github.com/Helmholtz-AI-Energy/perun/commit/d40a45e167e25e554000505025b366fb94c1941e))


## v0.1.0 (2023-03-17)

### Ci

* ci: test action trigger on anything except on release ([`ea76a8c`](https://github.com/Helmholtz-AI-Energy/perun/commit/ea76a8cb9baa5afaf57f308133151ff0dcb7dd34))

### Unknown

* 0.1.0

0.1.0 [skip ci] ([`d7f545d`](https://github.com/Helmholtz-AI-Energy/perun/commit/d7f545ddf146fcbbe6919a0249219a99ed197667))


## v0.1.0-beta.18 (2022-12-16)

### Unknown

* 0.1.0-beta.18

Automatically generated by python-semantic-release ([`0edc10b`](https://github.com/Helmholtz-AI-Energy/perun/commit/0edc10b1663e3be68c9d08d143316a6e4837c0d2))

* refactor/mpi4py-optional (#24)

* feat: removed mpi4py dependency

* docs: updated readme

* fix: configuration corrections ([`047022e`](https://github.com/Helmholtz-AI-Energy/perun/commit/047022ef18d7c504c7f93916f2088638bc4658d0))


## v0.1.0-beta.17 (2022-12-07)

### Test

* test: mocked backend, tested assignedDevices ([`9aa805d`](https://github.com/Helmholtz-AI-Energy/perun/commit/9aa805d5d2e8c0b709d640f6a8663f6120532a2c))

### Unknown

* 0.1.0-beta.17

Automatically generated by python-semantic-release ([`1c89721`](https://github.com/Helmholtz-AI-Energy/perun/commit/1c897213820c5cccf984212ed256a83d4830c99a))

* tests: backend fixture autoused and monkeypatched ([`e0484ce`](https://github.com/Helmholtz-AI-Energy/perun/commit/e0484ce8ae9ecd3efeaa28439da7be4937f6b330))


## v0.1.0-beta.16 (2022-09-20)

### Unknown

* 0.1.0-beta.16

Automatically generated by python-semantic-release ([`6309b46`](https://github.com/Helmholtz-AI-Energy/perun/commit/6309b46d0201649313506703657f7d01ad3f460b))


## v0.1.0-beta.15 (2022-09-19)

### Fix

* fix: relaxed dependencies (will tighten them later) ([`6509481`](https://github.com/Helmholtz-AI-Energy/perun/commit/650948170150eee242ae9bc78d1ea6bb1e9285b4))

### Unknown

* 0.1.0-beta.15

Automatically generated by python-semantic-release ([`e4687c4`](https://github.com/Helmholtz-AI-Energy/perun/commit/e4687c4a5ed7ed7e59d0dd7f59f9150696c06a64))


## v0.1.0-beta.14 (2022-09-19)

### Unknown

* 0.1.0-beta.14

Automatically generated by python-semantic-release ([`05a3915`](https://github.com/Helmholtz-AI-Energy/perun/commit/05a3915fa108d3f1dc2e46a673e1c27e0826ba37))


## v0.1.0-beta.13 (2022-09-02)

### Unknown

* 0.1.0-beta.13

Automatically generated by python-semantic-release ([`d99923f`](https://github.com/Helmholtz-AI-Energy/perun/commit/d99923f8449b63298260c4ed49051d9db41b1f18))


## v0.1.0-beta.12 (2022-08-30)

### Unknown

* 0.1.0-beta.12

Automatically generated by python-semantic-release ([`be6e84c`](https://github.com/Helmholtz-AI-Energy/perun/commit/be6e84cfbd52ed53a6f073ddd8588a4955138653))


## v0.1.0-beta.11 (2022-08-29)

### Unknown

* 0.1.0-beta.11

Automatically generated by python-semantic-release ([`b92def6`](https://github.com/Helmholtz-AI-Energy/perun/commit/b92def6f36ac453f003a3bf946d1c79797404202))


## v0.1.0-beta.10 (2022-08-24)

### Unknown

* 0.1.0-beta.10

Automatically generated by python-semantic-release ([`4d00219`](https://github.com/Helmholtz-AI-Energy/perun/commit/4d0021985790d01e2bd6ddac180a9f905d54e3b3))


## v0.1.0-beta.9 (2022-08-23)

### Unknown

* 0.1.0-beta.9

Automatically generated by python-semantic-release ([`b68fee8`](https://github.com/Helmholtz-AI-Energy/perun/commit/b68fee897e61f15525ffabacea5ed0d11238ac80))


## v0.1.0-beta.8 (2022-08-22)

### Ci

* ci: v3

python-semantic-release
Github needs a better action editor ([`e2f38e5`](https://github.com/Helmholtz-AI-Energy/perun/commit/e2f38e5281ea510694f6f58b04824cb8a589ea65))

### Unknown

* 0.1.0-beta.8

Automatically generated by python-semantic-release ([`ef91afa`](https://github.com/Helmholtz-AI-Energy/perun/commit/ef91afa02124767df2e92cf22e8b18332180724b))


## v0.1.0-beta.7 (2022-08-17)

### Unknown

* 0.1.0-beta.7

Automatically generated by python-semantic-release ([`b1090f4`](https://github.com/Helmholtz-AI-Energy/perun/commit/b1090f4efc6d57aaac52d52f0fa0ce7956273f50))


## v0.1.0-beta.6 (2022-08-15)

### Documentation

* docs: expanded usage documentation ([`e2c0c2d`](https://github.com/Helmholtz-AI-Energy/perun/commit/e2c0c2dae77100a68fcab9c875f9c22efce4d149))

### Unknown

* 0.1.0-beta.6

Automatically generated by python-semantic-release ([`9842763`](https://github.com/Helmholtz-AI-Energy/perun/commit/984276398412ef8d7037b1956189b3c681192a7e))


## v0.1.0-beta.5 (2022-08-11)

### Fix

* fix: missing report after monitor ([`5234a96`](https://github.com/Helmholtz-AI-Energy/perun/commit/5234a96292de553b57f4aaa82deb90153fe41ffc))

### Unknown

* 0.1.0-beta.5

Automatically generated by python-semantic-release ([`e65fdd6`](https://github.com/Helmholtz-AI-Energy/perun/commit/e65fdd66334e546c1a6555c470275795f6cad1a4))


## v0.1.0-beta.4 (2022-08-11)

### Documentation

* docs: updated readme ([`75d10bb`](https://github.com/Helmholtz-AI-Energy/perun/commit/75d10bbbef942695c8505bb5863a71ae523fbe54))

### Unknown

* 0.1.0-beta.4

Automatically generated by python-semantic-release ([`725b9f8`](https://github.com/Helmholtz-AI-Energy/perun/commit/725b9f8a5e24ef11001f63579674ddc18f7a3291))


## v0.1.0-beta.3 (2022-08-11)

### Unknown

* 0.1.0-beta.3

Automatically generated by python-semantic-release ([`e704d89`](https://github.com/Helmholtz-AI-Energy/perun/commit/e704d89508205ef93bd3ccd5e3a09bc1832dd3c3))


## v0.1.0-beta.2 (2022-08-11)

### Unknown

* 0.1.0-beta.2

Automatically generated by python-semantic-release ([`fd98e02`](https://github.com/Helmholtz-AI-Energy/perun/commit/fd98e025b0beb1a21f04af03d74d53a758069195))


## v0.1.0-beta.1 (2022-08-11)

### Feature

* feat: text, json and yaml reports ([`9503751`](https://github.com/Helmholtz-AI-Energy/perun/commit/95037516594189959fbfb2b2894d18cdba7b5819))

### Unknown

* 0.1.0-beta.1

Automatically generated by python-semantic-release ([`dae5ad9`](https://github.com/Helmholtz-AI-Energy/perun/commit/dae5ad92d8c91d8f5a36bab1b731c4fe6ad66b14))
