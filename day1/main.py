#read txt file

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
    
file_path = 'data.txt'
data = read_file(file_path=file_path)

rows = data.split('\n')

list1 = []
list2 = []

for row in rows:
    num1, num2 = map(int, row.split()) 
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()

#part 1

# sumDistances = 0

# for i in range(len(list1)):
#     distance = abs(list1[i] - list2[i])
#     sumDistances += distance

# print(sumDistances)

#part 2

sumSimilarityScore = 0

for i in range(len(list1)):
    n = list2.count(list1[i])

    sumSimilarityScore += (n * list1[i])

print(sumSimilarityScore)