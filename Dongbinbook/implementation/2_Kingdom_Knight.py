loc = input()

# a1 -> h8

result = 0

# 알파벳을 숫자로 변환 (a를 1로 맞추기 위해 ord('a')를 뺀 후 1을 더함)
loc_col = ord(loc[0]) - ord('a') + 1
loc_row = int(loc[1])

if abs(4.5 - loc_row) < 2.5:
  if abs(4.5 - loc_col) < 2.5:
    result = 8
  elif abs(4.5 - loc_col) == 2.5:
    result = 6
  elif abs(4.5 - loc_col) == 3.5:
    result = 4
    
elif abs(4.5 - loc_row) == 2.5:
  if abs(4.5 - loc_col) < 2.5:
    result = 6
  elif abs(4.5 - loc_col) == 2.5:
    result = 4
  elif abs(4.5 - loc_col) == 3.5:
    result = 3
    
elif abs(4.5 - loc_row) == 3.5:
  if abs(4.5 - loc_col) < 2.5:
    result = 4
  elif abs(4.5 - loc_col) == 2.5:
    result = 3
  elif abs(4.5 - loc_col) == 3.5:
    result = 2

print(result)
