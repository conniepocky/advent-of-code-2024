def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
file_path = 'input.txt'
data = read_file(file_path=file_path)

p1, p2 = data.split('\n\n')
rules = [list(line.split('|')) for line in p1.splitlines()]

print(rules)
updates = list((line.split(',') for line in p2.splitlines()))

def adheres_to_rule(rule: list[int], update: list[int]) -> bool:
    assert len(rule) == 2
    l, r = rule
    if l in update and r in update:
        return update.index(l) < update.index(r)

    return True

def middle(l):
    return l[len(l) // 2]

part_1 = 0

for update in updates:
    if all(adheres_to_rule(r, update) for r in rules):
        part_1 += int(middle(update))

print(part_1)