def read_data(file_path):
    with open(file_path, 'r') as file:
        input_lines = file.readlines()

    split_index = input_lines.index('\n')

    ordering_rules = {}
    for line in input_lines[:split_index]:
        if line.strip():
            page1, page2 = map(int, line.strip().split('|'))
            if page1 not in ordering_rules:
                ordering_rules[page1] = []
            ordering_rules[page1].append(page2)

    update_orders = [
        list(map(int, line.strip().split(',')))
        for line in input_lines[split_index + 1:]
        if line.strip()
    ]

    return ordering_rules, update_orders


def is_correctly_ordered(update_order, ordering_rules):
    for i, page in enumerate(update_order):
        if page not in ordering_rules:
            continue
        for other_page in ordering_rules[page]:
            if other_page in update_order[:i]:
                return False
    return True


def correct_order(update_order, ordering_rules):
    corrected = update_order.copy()

    while not is_correctly_ordered(corrected, ordering_rules):
        for i, page in enumerate(corrected):
            if page not in ordering_rules:
                continue
            for other_page in ordering_rules[page]:
                for j in range(i):
                    if corrected[j] == other_page:
                        corrected.insert(i + 1, corrected.pop(j))
                        break

    return corrected


def task1(file_path):
    ordering_rules, update_orders = read_data(file_path)

    return sum(
        update_order[len(update_order) // 2]
        for update_order in update_orders
        if is_correctly_ordered(update_order, ordering_rules)
    )


def task2(file_path):
    ordering_rules, update_orders = read_data(file_path)

    return sum(
        correct_order(update_order, ordering_rules)[len(update_order) // 2]
        for update_order in update_orders
        if not is_correctly_ordered(update_order, ordering_rules)
    )


file_path = 'inputs/input5.txt'

print(task1(file_path))
print(task2(file_path))
