load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "master",
)

# Only needed for PIP support:
load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")

pip_import(
    name = "service_c_requirements",
    requirements = "//service_c:requirements.txt",
)

# Load the pip_install symbol for my_deps, and create the dependencies'
# repositories.
# load("@service_c_requirements//:requirements.bzl", "pip_install")
# pip_install()
