def read_map(filename):
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f]
    return grid


def find_guard(grid):
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                return (x, y), cell
    return None, None


def turn_right(direction):
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return turns[direction]


def simulate_guard(grid):
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    position, facing = find_guard(grid)
    visited = set()
    visited.add(position)

    while True:
        dx, dy = directions[facing]
        new_x, new_y = position[0] + dx, position[1] + dy
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            break
        if grid[new_y][new_x] == '#':
            facing = turn_right(facing)
        else:
            position = (new_x, new_y)
            visited.add(position)

    return visited


filename = "inputs/input6.txt"  # Replace with the path to your input file
grid = read_map(filename)
visited_positions = simulate_guard(grid)
print(len(visited_positions))

