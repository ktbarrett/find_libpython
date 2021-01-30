from find_libpython import find_libpython
import ctypes


def test_find_libpython():
    # find path
    path = find_libpython()
    # ensure we have a path
    assert path is not None
    # check to ensure it is a libpython share object
    lib = ctypes.CDLL(path)
    assert hasattr(lib, 'Py_Initialize')
