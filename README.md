# POC Bazel + Golang + Python

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


## POC Roadmap

- Python support:
  - [ ] Auto generate BUILD with [Pazel](https://github.com/tuomasr/pazel)
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
