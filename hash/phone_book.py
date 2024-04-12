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



# 다 비교할 필요가 없다. (사전순이라서)
# 그럼, 
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    answer_my = 0
    for pre in phone_book:
        for compare in phone_book:
            if compare[:len(pre)] == pre:
                answer_my += 1
            if compare[0] > pre[0]:
                break
                
    # True가 2개 이상이면 answer is false
    if answer_my > len(phone_book):
        answer = False
    
    return answer
# phone = ["119", "97674223", "1195524421"]
# print(sorted(phone))
# print("119"[0])
