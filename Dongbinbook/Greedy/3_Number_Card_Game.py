N, M = map(int, input().split())

result = 0

for i in range(N):
  data = list(map(int, input().split()))
  if result < min(data):
    result = min(data)

print(result)
