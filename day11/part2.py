from collections import defaultdict
import sys

sys.setrecursionlimit(2**30)

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip().split()
    
file_path = 'input.txt'
data = read_file(file_path=file_path)

raw_nums = list(map(int, data))

nums = defaultdict(int)
for x in raw_nums:
    nums[x] += 1

print(nums)

def blink(stones: dict):
    final_stones = defaultdict(int)
    for x in nums:
        length = len(str(x))
        if x == 0:
            final_stones[1] += nums[0] 
        elif length % 2 == 0:
            final_stones[int(str(x)[:length // 2])] += nums[x]
            final_stones[int(str(x)[length // 2:])] += nums[x]
        else:
            final_stones[x * 2024] += nums[x]
    
    return final_stones


for i in range(75):
    nums = blink(nums)

ans = 0

for x in nums:
    ans += nums[x]

print(ans)