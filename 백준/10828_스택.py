import sys

input = sys.stdin.readline

stack = []
num = int(input())
for i in range(num):
    command = input().split()
    if command[0] == 'top':
        if len(stack):
            print(stack[-1])
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if len(stack) else 1)
    elif command[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else: print(-1)
    else:
       stack.append(command[-1])