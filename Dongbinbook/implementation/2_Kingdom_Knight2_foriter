loc = input()

# a1 -> h8

result = 0

# 알파벳을 숫자로 변환 (a를 1로 맞추기 위해 ord('a')를 뺀 후 1을 더함)
loc_row = int(loc[1])
loc_col = ord(loc[0]) - ord('a') + 1

steps = [(-2, -1), (-2, 1),   # 상
         (2, -1), (2, 1),     # 하
         (1, -2), (-1, -2),   # 좌
         (1, 2), (-1, 2)     # 우
        ]

for step in steps:
  new_row = loc_row + step[0]
  new_col = loc_col + step[1]

  if (1 <= new_row <= 8) & (1 <= new_col <= 8):
    result += 1

print(result)
