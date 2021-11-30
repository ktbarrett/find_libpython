from find_libpython import find_libpython
import ctypes
import sys


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
