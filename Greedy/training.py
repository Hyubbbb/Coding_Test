# 학생 번호: 체격순
# 바로 인접한 번호의 학생에게만 체육복 빌려줄 수 있다
# 최대한 많은 학생이 수업을 듣도록

'''
매개변수
1. 전체 학생의 수 n, 
2. 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
3. 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
''' 

# 체육수업을 들을 수 있는 학생의 최댓값을 return

def solution(n, lost, reserve):
    answer = 0
    
    
    # 0. 여분 & 도난 (교집합)
    intersection = list(set(lost) & set(reserve))
    lost_new = list(set(lost) - set(intersection))
    reserve_new = list(set(reserve) - set(intersection))
    
    
    # 1. 1벌은 갖고 있는 친구들
    answer = n - len(lost_new)
    
    
    # 2. 여벌 주기
    for num in reserve_new:
        # 2-1) lost와 reserve에 동시 존재 O
        if num in lost_new:
            lost_new.remove(num)
            answer += 1
        
        # 2-2) lost와 reserve에 동시 존재 X
        else:
            if num-1 in lost_new:
                lost_new.remove(num-1)
                answer += 1

            elif num+1 in lost_new:
                lost_new.remove(num+1)
                answer += 1
            
    return answer
