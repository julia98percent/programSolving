import sys

input = sys.stdin.readline

queue = []
num = int(input())
idx = 0

for i in range(num):
    command = input().split()
    if command[0] == 'front':
        if len(queue) - idx:
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

    elif command[0] == 'pop':
            if len(queue) - idx == 0:
                print(-1)
            else:
                print(queue[idx])
                idx += 1 
    else:
       queue.append(command[-1])