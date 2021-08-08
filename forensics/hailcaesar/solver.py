data = """2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0"""

for i in range(10000):
  flag=''
  for j in data:
    orded = ord(j) + i
    if(orded > 126):
      orded = 32 + orded % 127
    flag+=chr(orded)
  print(f'[-] shift {i}: {flag}') 
  if 'CTF' in flag:
    print(f'[+] Flag: {flag}')
    break