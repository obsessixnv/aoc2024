import re

def part_1(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, data)

    total_sum = 0
    for match in matches:
        x = int(match[0])
        y = int(match[1])
        total_sum += x * y
    return total_sum

file_path = 'inputs/input3.txt'

result1 = part_1(file_path)
print(result1)


def part_2(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    instructions = re.findall(r'(do\(\))|(don\'t\(\))|(mul\(\d+,\d+\))', data)

    total_sum = 0
    mul_enabled = True
    for do_instr, dont_instr, mul_instr in instructions:
        if do_instr:
            mul_enabled = True
        elif dont_instr:
            mul_enabled = False
        elif mul_instr and mul_enabled:
            x, y = map(int, re.findall(r'\d+', mul_instr))
            total_sum += x * y

    return total_sum

result2 = part_2(file_path)
print(result2)