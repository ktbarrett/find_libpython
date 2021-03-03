import sys
import os
import ctypes.util
import sysconfig


print(f"sys.platform: {sys.platform!r}")
print(f"os.name: {os.name!r}")
print(f"sysconfig.get_platform(): {sysconfig.get_platform()!r}")
print(f"ls LIBPL:", os.listdir(sysconfig.get_config_var('LIBPL')))
print("sysconfig.get_config_vars():")
for k, v in sysconfig.get_config_vars().items():
    print(k, v)
