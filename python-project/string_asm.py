# // { autofold
import ctypes
import struct
import time
import math
# // }

from pycca.asm import *


print("""
   Example 2: Jump to label
----------------------------------------------
""")

# Also show that we can give an assembly string rather than
# instruction objects:
fn = mkfunction("""
        mov  eax, 0x1
        jmp  start
    end:
        ret
        mov  eax, 0x1
        mov  eax, 0x1
    start:
        mov  eax, 0xdeadbeef
        jmp  end
        mov  eax, 0x1
""")

fn.restype = ctypes.c_uint32


with open('asm_content', 'r') as f:
    asm_lines = "".join(f.readlines())
fn2 = mkfunction(asm_lines)
fn2.restype = ctypes.c_uint32

# We get 0xdeadbeef back if jumps are followed.
print("Return: 0x%x" % fn())
print("Return: 0x%x" % fn2())
