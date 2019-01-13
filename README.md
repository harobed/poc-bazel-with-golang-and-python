# POC Bazel + Golang + Python

This is a Project Structure POC with Bazel support for Python and Golang services.

## POC Roadmap

- [ ] New Project Structure (updated version of [Managing a Go monorepo with Bazel](https://filipnikolovski.com/managing-go-monorepo-with-bazel/))
- Python support:
  - [ ] Auto generate BUILD with [Pazel](https://github.com/tuomasr/pazel). Warning, it is pre alpha tool. At this time, I have this issue [#20](https://github.com/tuomasr/pazel/issues/20)
  - [X] Install requirements
  - [X] Run
  - [X] Execute tests
  - [X] Build Docker Image
  - [X] Push Docker Image
  - [ ] Generate Protobuf
- Golang support:
  - [X] Auto generate BUILD with [Gazelle](https://github.com/bazelbuild/bazel-gazelle/)
  - [ ] Install vendors (see [rules_go_dep](https://github.com/scele/rules_go_dep))
  - [X] Run
  - [ ] Execute tests
  - [X] Build Docker Image
  - [X] Push Docker Image
  - [ ] Generate Protobuf

## Project Structure

Services :

- `service_a` and `service_b` are Golang project
- `service_c` is a Python project

```
platform
  |-- src
  |    |-- service_a
  |    |   |--cmd
  |    |   |  `--bar
  |    |   |     |--BUILD
  |    |   |     `--main.go
  |    |   |-- utils
  |    |   |-- vendor
  |    |   |-- Gopkg.lock
  |    |   |-- Gopkg.toml
  |    |   |-- BUILD
  |    |   `-- WORKSPACE
  |    |-- service_b
  |    |   |--cmd
  |    |   |  `--bar
  |    |   |     |--BUILD
  |    |   |     `--main.go
  |    |   |-- utils
  |    |   |-- vendor
  |    |   |-- Gopkg.lock
  |    |   |-- Gopkg.toml
  |    |   |-- BUILD
  |    |   `-- WORKSPACE
  |    |-- service_c
  |    |   |-- app.py
  |    |   |   `-- tests
  |    |   |       |-- BUILD
  |    |   |       `-- test_sample.py
  |    |   |-- requirements.in
  |    |   |-- requirements.txt
  |    |   |-- BUILD
  |    |   `-- WORKSPACE
  |    `--pkg
  |-- README.md
  `-- gitlab-ci.yml
```

### Project Structure Rationalize

- This Project Structure must be compatible with Monorepo mindset and Multirepo mindset
- I want to be able to extract each service (`service_a`, `service_b`...) in individuals Git repository, then each project must be autonomous (own `WORKSPACE`, `Gopkg.lock`, and `requirements.txt` files)


## Prerequisite

- [Bazel](https://docs.bazel.build/versions/master/install-os-x.html#step-2-install-the-bazel-homebrew-package)

```
$ brew tap bazelbuild/tap
$ brew tap-pin bazelbuild/tap
$ brew install bazelbuild/tap/bazel
$ brew install buildifier
```

Golang dependencies:

```
$ brew install go dep
```

Python dependencies:

```
$ brew install python3
```





## Run

Run binary:

```
$ bazel run //service_c
```

Run Docker Image:

```
$ bazel run //service_c:image
```

## Push Docker image

```
$ bazel run //service_c:push
```

## Build

If you want build only:

```
$ bazel build //...
```

## Execute tests

```
$ bazel test //...
```

## Clean repository

```
$ bazel clean
```

## How to use Gazelle to generate Golang BUILD files

```
$ bazel run //:gazelle
```

## Ressources

- [Bazel Python Rules](https://github.com/bazelbuild/rules_python#overview)
- [Managing a Go monorepo with Bazel](https://filipnikolovski.com/managing-go-monorepo-with-bazel/)
