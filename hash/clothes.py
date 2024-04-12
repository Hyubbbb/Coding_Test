'''
큰 그림
1. print(clothes[i][1])가 같은 애들끼리 묶어
2. e.g. num_headgear = 3, num_eyewear = 2, num_face = 3
    -> (3 + 2 + 3) + (3*2 + 3*3 + 2*3) + (3*2*3)
    -> 간단식이 있었다. (N+1)*(M+1)*(K+1) - 1
'''

def solution(clothes):
    answer = 0
    
    # 1. 카테고리 파악하기
    cat_dic = {}

    for name, category in clothes:
        if category not in cat_dic.keys():
            cat_dic[category] = 1

        else: 
            cat_dic[category] += 1

    tmp = 1
    for _, values in cat_dic.items():
        tmp *= (values+1)
    
    answer = tmp - 1
    
    return answer
