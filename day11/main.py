def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().split()
    
file_path = 'input.txt'
data = read_file(file_path=file_path)

def blink(stones):
    finalStones = []
    for stone in stones:
        if stone == "0":
            finalStones.append("1")
        elif len(stone) % 2 == 0: # even
            half = len(stone) // 2

            left = int(stone[:half])
            right = int(stone[half:])

            finalStones.append(str(left))
            finalStones.append(str(right))
        else:
            finalStones.append(str((int(stone)*2024)))
    
    return finalStones

for i in range(0, 75):
    print(i)
    data = blink(data)

print(len(data))