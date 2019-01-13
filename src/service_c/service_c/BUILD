load("@my_deps//:requirements.bzl", "requirement")

py_library(
    name = "app",
    srcs = ["app.py"],
    deps = [requirement("flask")],
)

py_binary(
    name = "cli",
    srcs = ["cli.py"],
    deps = ["//service_c:app"],
)
