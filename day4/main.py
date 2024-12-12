def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip().splitlines()
    
    return [list(line) for line in data]
    
file_path = 'input.txt'
grid = read_file(file_path=file_path)

keyword = "XMAS"

rows = len(grid)
cols = len(grid[0])

def is_valid_direction(row, col, dx, dy):
    for i in range(len(keyword)):
        x = row + i * dx
        y = col + i * dy
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != keyword[i]:
            return False
    return True
    
def count_occurrences():
    sumWord = 0
    for row in range(rows):
        for col in range(cols):
            for dx, dy in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                if is_valid_direction(row, col, dx, dy):
                    sumWord += 1

    return sumWord

print(count_occurrences())