n = int(input())

# 00시00분00초 -> n시 59분 59초까지 (3 포함)

result = 0

for h in range(n+1): # hour
  for m in range(60): # min
    for s in range(60): # sec
      time = str(h)+str(m)+str(s)
      if '3' in time:
        result += 1

print(result)
