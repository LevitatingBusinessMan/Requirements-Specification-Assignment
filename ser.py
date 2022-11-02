# For testing the serial connection

import serial
import os
import time
from Crypto.Cipher import AES
AES_KEY = bytearray([0xd7, 0xe7, 0xeb, 0x9e, 0x4c, 0xce, 0x25, 0x43, 0x62, 0x91, 0x1b, 0xdd, 0x3d, 0xf2, 0x16, 0xb2])
aes = AES.new(AES_KEY, AES.MODE_ECB)

ser = serial.Serial("/dev/ttyACM0", 9600)
time.sleep(2)
canary = os.urandom(4)
print("Canary: ", end='')
print(canary)
ser.write(canary)
ser.flush()
data = ser.read(16)
print(aes.decrypt(data))
print(aes.decrypt(data).split(b'\x00')[0])

res = aes.decrypt(data).split(b'\x00')[0]
uid = res[:4]
bcanary = res[4:]

print("uid: " + ":".join("{:02x}".format(c) for c in uid))
print("canary: " + ":".join("{:02x}".format(c) for c in bcanary))

print("Correct canary? " + str(canary == bcanary))
