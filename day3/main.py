import re

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
file_path = 'input.txt'
data = read_file(file_path=file_path)

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)

sumMatches = 0

for match in matches:
    match = match[4:-1]
    a, b = match.split(',')

    sumMatches += (int(a) * int(b))

#part two

pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
instructions = re.findall(pattern, "".join(data))

sumMatches = 0
enabled = True

for instruction in instructions:
    if instruction[0] == 'do()':
        enabled = True
    elif instruction[0] == "don't()":
        enabled = False
    elif enabled and "mul" in instruction[0]:
        a, b = int(instruction[1]), int(instruction[2])
        sumMatches += (a * b)
    
print(sumMatches)