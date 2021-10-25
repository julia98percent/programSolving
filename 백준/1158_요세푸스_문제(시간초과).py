a, b = map(int, input().split())
nums = [x for x in range(1, a+1)]
result = []
cnt = 1
idx = 0
while len(result) < a :
    if (idx + 1) % b: # 1, 2, 4, ...
        nums.append(nums[idx])
    else: # 3 6
        result.append(nums[idx])
    idx += 1

print("<", ", ".join(map(str, result)), ">", sep='')