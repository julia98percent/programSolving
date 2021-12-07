def solution(lottos, win_nums):
    zero = lottos.count(0)
    cnt = 7
    for i in lottos:
        if i in win_nums:
            cnt-=1
    answer = [cnt-zero, cnt]
    return [6 if value==7 else value for value in answer]