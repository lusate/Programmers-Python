def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    
    zero = lottos.count(0) #lottos에 있는 0의 개수를 카운트
    match = 0
    
    #lottos와 win_nums 일치하는 번호 확인
    for i in win_nums:
        #i는 win_nums에 있는 숫자들
        if i in lottos:  #lottos 에 있는 숫자가 i와 같다면
            match+=1
            
    answer = rank[zero + match], rank[match]
    return answer



#테스트 케이스 실행
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

rank=[6,6,5,4,3,2,1]

#0 의 개수를 카운트
zero = lottos.count(0)
match = 0

for i in win_nums:
    #i는 win_nums에 있는 숫자들
    if i in lottos: #lottos 에 있는 숫자가 i와 같다면
        match+=1
        print(match)
        
print(rank[zero + match], rank[match])
