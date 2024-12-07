def count_xmas(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    for i in range(rows):
        for j in range(cols - word_len + 1):
            if grid[i][j:j + word_len] == word:
                count += 1
            if grid[i][j:j + word_len][::-1] == word:
                count += 1

    for i in range(rows - word_len + 1):
        for j in range(cols):
            if "".join(grid[i + k][j] for k in range(word_len)) == word:
                count += 1
            if "".join(grid[i + k][j] for k in range(word_len))[::-1] == word:
                count += 1

    for i in range(rows - word_len + 1):
        for j in range(cols - word_len + 1):
            if "".join(grid[i + k][j + k] for k in range(word_len)) == word:
                count += 1
            if "".join(grid[i + k][j + k] for k in range(word_len))[::-1] == word:
                count += 1

    for i in range(word_len - 1, rows):
        for j in range(cols - word_len + 1):
            if "".join(grid[i - k][j + k] for k in range(word_len)) == word:
                count += 1
            if "".join(grid[i - k][j + k] for k in range(word_len))[::-1] == word:
                count += 1

    return count


file_path = 'inputs/input4.txt'

result1 = count_xmas(file_path)
print(result1)
