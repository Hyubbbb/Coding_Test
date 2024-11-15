# n = map(int, input())
n = int(input())
steps = input().split()

result = [1, 1]

# LRUD
x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]

for i in steps:
  if i == 'L':
    result[1] -= 1
  elif i == 'R':
    result[1] += 1
  elif i == 'U':
    result[0] -= 1
  elif i == 'D':
    result[0] += 1

  if result[0] < 1:
    result[0] = 1
  elif result[0] > n:
    result[0] = n
  elif result[1] < 1:
    result[1] = 1
  elif result[1] > n:
    result[1] = n
  
print(result)
