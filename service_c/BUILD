load("@service_c_requirements//:requirements.bzl", "requirement")

py_binary(
  name="service_c",
  srcs=["cli.py", "app.py"],
  main="cli.py",
  deps=[
    requirement("flask"),
  ]
)
