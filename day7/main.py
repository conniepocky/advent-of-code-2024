import itertools

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
file_path = 'input.txt'
data = read_file(file_path=file_path)

rows = data.split('\n')

sumValid = 0

for row in rows:
    row = row.split(' ')

    result = int(row[0].split(':')[0])
    row.pop(0)
    
    numbers = list(map(int, row))

    operators = ['+', '*']

    operator_combinations = itertools.product(operators, repeat=len(numbers) - 1)

    for ops in operator_combinations:
        expression = str(numbers[0])
        res = numbers[0]

        for num, op in zip(numbers[1:], ops):
            expression += f" {op} {num}"
            if op == '+':
                res += num
            elif op == '*':
                res *= num
        
        if res == result:
            sumValid += result
            break

print(sumValid)