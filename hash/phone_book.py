# def solution(phone_book):
#     answer = True
    
#     answer_my = 0
#     for pre in phone_book:
#         for compare in phone_book:
#             if compare[:len(pre)] == pre:
#                 answer_my += 1
                
#     # True가 2개 이상이면 answer is false
#     if answer_my > len(phone_book):
#         answer = False
    
#     return answer



# 다 비교할 필요가 없다. (사전순이라서) -> 아..! 자신의 바로 뒤에서 접두사 발견이 안 되면, 그 뒤는 아예 의미가 없겠구나!!!!!
# 그럼, 
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    
    return answer
# phone = ["119", "97674223", "1195524421"]
# print(sorted(phone))
# print("119"[0])
