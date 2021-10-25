import sys

input = sys.stdin.readline

queue = []
num = int(input())
idx = 0 # 현재 인덱스

for i in range(num):
    command = input().split() # [push, 3] or [back] ... 
    if command[0] == 'front':
        if len(queue) - idx: # 인덱스와 queue의 길이가 같지 않다면 = 길이가 1 이상 (True)
            print(queue[idx])
        else: print(-1)

    elif command[0] == 'back':
        if len(queue) - idx:
            print(queue[-1])
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(queue) - idx)

    elif command[0] == 'empty':
        print(0 if len(queue) - idx else 1)


# pop 메소드 사용 -> 시간초과
    elif command[0] == 'pop':
            if len(queue) - idx == 0:
                print(-1)
            else: # 인덱스를 1 옮겨줌 - list의 길이: list[idx] ~ list[-1]
                print(queue[idx])
                idx += 1 
    else: # push
       queue.append(command[-1])