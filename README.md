# POC Bazel + Golang + Python

## Prerequisite

- [Bazel](https://docs.bazel.build/versions/master/install-os-x.html#step-2-install-the-bazel-homebrew-package)

```
$ brew tap bazelbuild/tap
$ brew tap-pin bazelbuild/tap
$ brew install bazelbuild/tap/bazel
```

## Build

```
$ bazel build //...
```
