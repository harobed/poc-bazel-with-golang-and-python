# ServiceA

One line project overview.

## Quick demo

Lorem ipsum dolor sit amet, posuere vestibulum tempor lectus sed dictum integer, lobortis ipsum nunc et dui aliquam elementum, justo wisi est ac donec. Porttitor tellus, tincidunt porttitor est aliquet, donec libero suspendisse hendrerit.


### Build service_a

```sh
$ bazel build //service_c/...
```

### Run service_a

```sh
$ bazel run //service_a/cmd:service_a
...
hello world
```

Where is generated `service_a` binary:

```
$ ls bazel-bin/service_a/cmd/darwin_amd64_stripped/service_a
bazel-bin/service_a/cmd/darwin_amd64_stripped/service_a
```


### Build Docker Image

```sh
$ bazel build //service_a/cmd:image
```

### Run Docker Image

```sh
$ bazel run //service_a/cmd:image
```

### Push Docker Image

```sh
$ bazel run //service_a/cmd:push
```
