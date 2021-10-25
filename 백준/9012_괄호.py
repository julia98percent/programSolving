def isVPS(ps):
    stack = []
    for j in ps:
        if j == '(': # (이라면 그냥 넣는다
            stack.append('(')
        else: # )이라면
            if not len(stack): # )부터 들어온 경우
                return "NO"
            else: stack.pop() # (와 )가 만난 경우
    return "NO" if len(stack) else "YES" # 배열의 길이가 1 이상이라면 NO, else YES return

def main(num):
    for i in range(num):
        i = input()
        j = isVPS(i)
        print(j)
    return

n = int(input())
main(n)