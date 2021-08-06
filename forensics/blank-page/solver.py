#!/usr/bin/env python3

with open('TheMessage.txt','r') as f:
  data = f.read()
  
flag=''
for i in data:
  if i == ' ':
    flag+='0'
  else:
    flag+='1'

flag = int(flag,2)
flag = hex(flag)
flag = bytes.fromhex(flag[2:])

print(flag.decode('ASCII'))