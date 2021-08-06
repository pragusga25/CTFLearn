#!/usr/bin/env python3
import base64

str1 = base64.b64decode('xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p')
str2 = base64.b64decode('h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU')

flag = ''
for i in range(len(str1)):
  xored = str1[i] ^ str2[i]
  flag+=chr(xored)
  
print(flag)