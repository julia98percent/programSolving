def isVPS(ps):
    stack = []
    for j in ps:
        if j == '(':
            stack.append('(')
        else:
            if not len(stack):
                return "NO"
            else: stack.pop()
    return "NO" if len(stack) else "YES"

def main(num):
    for i in range(num):
        i = input()
        j = isVPS(i)
        print(j)
    return

n = int(input())
main(n)