package(default_visibility = ["//visibility:public"])

load("@service_c_requirements//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_image",
    "container_push",
)

py_library(
    name = "app_lib",
    srcs = ["app.py"],
    imports = ["."],
    deps = [
        requirement("flask"),
        requirement("werkzeug"),
        requirement("jinja2"),
        requirement("click"),
        requirement("itsdangerous"),
    ],
)

py_binary(
    name = "service_c",
    srcs = [
        "app.py",
        "cli.py",
    ],
    main = "cli.py",
    deps = [
        ":app_lib",
    ],
)

py_image(
    name = "image",
    srcs = [
        "app.py",
        "cli.py",
    ],
    main = "cli.py",
    deps = [
        ":app_lib",
    ],
)

container_image(
    name = "docker_image",
    base = ":image",
    ports = ["5000"],
)

container_push(
    name = "push",
    format = "Docker",
    image = ":docker_image",
    registry = "index.docker.io",
    repository = "harobed/service_c",
    tag = "develop",
)
