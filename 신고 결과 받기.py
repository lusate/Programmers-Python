#Dictionary 사용한다

def solution(id_list, report ,k):
    #id_list 길이 만큼 초기값 0으로 해서 출력
    answer = [0] * len(id_list)
    '''
    ex) id_list = [1,2,3,4] 라고 했을 때 
    answer = [0,0,0,0]
    '''
    
    # 신고하는 id와 신고당하는 id 리스트
    reports = {x : 0 for x in id_list}
    '''
    ex) id_list = ["muzi", "frodo", "apeach", "neo"]

    reports = {x : 0 for x in id_list}

    print(reports)  하면
    {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
    '''
    
    #set 함수는 중복을 제거하기 위한 함수
    for r in set(report):
        reports[r.split()[1]] += 1
        
    '''
    report 만큼 반복
    reports[r.split()[0]] 은 신고하는 쪽 (0으로 초기화 되어 있음)
    reports[r.split()[1]] 은 신고 당하는 쪽 (0으로 초기화 되어 있음)
    
    신고당하는 id 에 1씩 더하면 3 2 2 3 2 가 출력됨
    '''
        
    for r in set(report):
        #신고 당하는 id쪽의 신고 당한 횟수 3 2 2 3 2 에서 k이상이라면
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
            #id_list의 index를 찾아야 하므로 index 함수가 필요하다
            #index 함수가 빠지면 'list' object is not callable 에러가 발생
        #print(answer)
        '''
        [0, 0, 0, 0]
        [1, 0, 0, 0]
        [2, 0, 0, 0]
        [2, 1, 0, 0]
        [2, 1, 1, 0]
        '''
    
    return answer



'''
from collections import defaultdict

def solution(id_list, report,k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)
	
    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a,b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1
    
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u]>=k:
                result +=1
        answer.append(result)
    return answer
    
이걸로도 가능
'''
