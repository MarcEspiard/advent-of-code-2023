import re

input_list = list()
with open('input.txt') as f:
    [input_list.append(line.replace('\n', '')) for line in f.readlines()]

# print(input_list)
_RE_COMBINE_WHITESPACE = re.compile(r"\s+")
points = list()
for row in input_list:
    splits = row.split(':')
    all_numbers = splits[1].split('|')
    winning_numbers = _RE_COMBINE_WHITESPACE.sub(" ", all_numbers[0]).strip().split(' ')
    my_numbers = _RE_COMBINE_WHITESPACE.sub(" ", all_numbers[1]).strip().split(' ')

    row_points = 0
    found = 0
    for num in my_numbers:
        if num in winning_numbers:
            row_points = max(row_points, 1)
            found += 1

    if row_points > 0:
        points.append(row_points * (2 ** (found - 1)))

print(points)
print(sum(points))
