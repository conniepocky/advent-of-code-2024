def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
file_path = 'input.txt'
data = read_file(file_path=file_path)

reports = data.split('\n')

for i in range(len(reports)):
    reports[i] = list(map(int, reports[i].split()))

sumSafe = 0

def is_safe(row):
    difference = [a - b for a, b in zip(row, row[1:])]
    is_all_same = all(i > 0 for i in difference) or all(i < 0 for i in difference)
    is_in_range = all(0 < abs(i) <= 3 for i in difference)
    if is_all_same and is_in_range:
        return True
    return False

# part 1

# for report in reports:  
#     if is_safe(report):
#         sumSafe += 1
            
# part 2

for report in reports:
    if is_safe(report):
        sumSafe += 1
    else:
        for i in range(0, len(report)):
            newList = report.copy()
            newList.pop(i)
            if is_safe(newList):
                sumSafe += 1
                break

print(sumSafe)