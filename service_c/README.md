# ServiceC

One line project overview.

## Rationalize

* Explain why do you have created this service.


## Quick demo

Lorem ipsum dolor sit amet, posuere vestibulum tempor lectus sed dictum integer, lobortis ipsum nunc et dui aliquam elementum, justo wisi est ac donec. Porttitor tellus, tincidunt porttitor est aliquet, donec libero suspendisse hendrerit.

### Running service_c


```sh
$ bazel run //service_c
```

### Build service_c

```sh
$ bazel build //service_c
```

Where is generated `service_c`:

```
$ ls ls bazel-bin/service_c/service_c
bazel-bin/service_c/service_c
```

### Execute tests

```sh
$ bazel test ...
$ cat ../bazel-testlogs/service_c/tests/test_sample/test.log
exec ${PAGER:-/usr/bin/less} "$0" || exit 1
Executing tests from //service_c/tests:test_sample
-----------------------------------------------------------------------------
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
42
```

### Build Docker Image

```sh
$ bazel build :docker_image
```

## Display all service_c Bazel targets

```
$ bazel query 'attr(visibility, "", "//service_c/...")'
INFO: Invocation ID: 33b84837-9c47-4690-8560-391095162916
//service_c:push
//service_c:docker_image
//service_c:image
//service_c:image.binary
//service_c:bin
Loading: 0 packages loaded
```
