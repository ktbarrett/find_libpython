import ctypes
import sys

import pytest
from find_libpython import (
    _get_proc_library,
    _is_cygwin,
    _is_posix,
    _linked_libpython_unix,
    find_libpython,
)

try:
    ctypes.CDLL("")
    can_get_handle_to_main = True
except OSError:
    print("Platform does not support opening the current process library")
    can_get_handle_to_main = False


def test_find_libpython():
    # find path
    path = find_libpython()
    # ensure we have a path
    assert path is not None
    # check to ensure it is a libpython share object
    lib = ctypes.CDLL(path)
    assert hasattr(lib, "Py_Initialize")
    # ensure it's the right version...
    lib.Py_GetVersion.restype = ctypes.c_char_p
    lib_version = lib.Py_GetVersion().decode().split()[0]
    curr_version = sys.version.split()[0]
    assert lib_version == curr_version


@pytest.mark.skipif(
    not _is_posix or _is_cygwin or not can_get_handle_to_main,
    reason="only linux support this",
)
def test_get_proc_library():
    # Get current library
    libpython = ctypes.CDLL("")

    # Get library for reference
    path_linked = _linked_libpython_unix(libpython)
    # Get library from /proc method
    path_from_proc = next(_get_proc_library())

    # Only compare paths if both return a library (not /usr/bin/python3.x)
    if "libpython" in path_linked:
        assert path_linked == path_from_proc
