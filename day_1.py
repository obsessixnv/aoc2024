from collections import Counter

with open("inputs/input1.txt") as file:
    lines = file.readlines()

left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

total = 0

for i in range(len(left_list)):
    difference  = abs(left_list[i]- right_list[i])
    total += difference

print(total)


similar = 0

right_count = Counter(right_list)

for number in left_list:
    if number in right_count:
        similar += number * right_count[number]


print(similar)