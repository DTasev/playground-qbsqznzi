import ctypes
import struct
import time
import math

from pycca.asm import *


print("""
   Example 1: Return a value from call
------------------------------------------------------
""")

# To return a value from a function, just put it in eax or rax:
fn = mkfunction([
    mov(eax, 0xdeadbeef),
    ret()
])

# Tell ctypes how to interpret the return value
fn.restype = ctypes.c_uint32

# Call! Hopefully we get 0xdeadbeef back.
print("Return: 0x%x" % fn())
