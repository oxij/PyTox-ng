from distutils.core import setup, Extension

sources = ["pytox/pytox.c", "pytox/core.c", "pytox/av.c", "pytox/util.c"]

libraries = [
  "opus",
  "sodium",
  "toxcore",
  "vpx",
]

cflags = [
  "-Wall",
  # "-Werror",
  "-Wextra",
  "-Wno-declaration-after-statement",
  "-Wno-missing-field-initializers",
  "-Wno-unused-parameter",
  "-fno-strict-aliasing",
]

setup(
    name="PyTox-ng",
    version="0.2.18",
    description='Python bindings for https://github.com/TokTok/c-toxcore of https://tox.chat/',
    url='https://github.com/oxij/PyTox-ng',

    author='Wei-Ning Huang (AZ)',
    author_email='aitjcize@gmail.com',
    maintainer='Jan Malakhovski',
    maintainer_email='oxij@oxij.org',

    ext_modules=[
        Extension(
            "pytox",
            sources,
            extra_compile_args=cflags,
            libraries=libraries
        )
    ]
)
