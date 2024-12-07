def is_safe_report(report):
    difference = []
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        difference.append(diff)

    for diff in difference:
        if not (1 <= abs(diff) <= 3):
            return False

    increasing = True
    decreasing = True

    for diff in difference:
        if diff < 0:
            increasing = False
        if diff > 0:
            decreasing = False

    if increasing or decreasing:
        return True
    else:
        return False


def count_safe_reports(file_path):
    with open(file_path) as file:
        lines = file.readlines()

    is_safe = 0
    for line in lines:
        report = list(map(int, line.strip().split()))
        if is_safe_report(report):
            is_safe += 1

    return is_safe

file = 'inputs/input2.txt'

result = count_safe_reports(file)
print(result)