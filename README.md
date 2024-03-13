# find_libpython

A pypi project version of [this](https://gist.github.com/tkf/d980eee120611604c0b9b5fef5b8dae6) gist, which also appears
within the [PyCall](https://github.com/JuliaPy/PyCall.jl/blob/master/deps/find_libpython.py) library.

The library is designed to find the path to the libpython dynamic library for the current Python environment.
It should work with many types of installations, whether it be conda-managed, system-managed, or otherwise.
And it should function on Windows, Mac OS/OS X, and any Linux distribution.

This code is useful in several contexts, including projects that embed a Python interpreter into another process,
or Python library build systems.

## Usage

`find_libpython` is both a script and a Python package.
Usage as a script is useful in contexts like obtaining the path to libpython for linking in makefile-based build systems.
It could also be used to determine the path to libpython for embedding a Python interpreter in a process written in another language.
In that case the recommended usage is to simply call the script in a subprocess with no arguments and parse the output.

```
> find_libpython
/home/kaleb/miniconda3/envs/test/lib/libpython3.8.so.1.0
```

The full help message:
```
> find_libpython --help
usage: find_libpython [-h] [-v] [--list-all | --candidate-names | --candidate-paths | --platform-info | --version]

Locate libpython associated with this Python executable.

options:
  -h, --help         show this help message and exit
  -v, --verbose      Print debugging information.
  --list-all         Print list of all paths found.
  --candidate-names  Print list of candidate names of libpython.
  --candidate-paths  Print list of candidate paths of libpython.
  --platform-info    Print information about the platform and exit.
  --version          show program's version number and exit
```

Usage as a library might occur when you need to obtain the path to the library in a Python-based build system like distutils.
It is recommended to use the `find_libpython` method which will return the path to libpython as a string, or `None` if it cannot be found.

```python
>>> from find_libpython import find_libpython
>>> find_libpython()
'/home/kaleb/miniconda3/envs/test/lib/libpython3.8.so.1.0'
```
