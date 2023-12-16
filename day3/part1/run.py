import re

input_list = list()
with open('input.txt') as f:
    [input_list.append([*line.replace('\n', '')]) for line in f.readlines()]

y_max = len(input_list[0])
x_max = len(input_list)

parts = list()
for y, row in enumerate(input_list):
    curr_num = ''
    is_part = False

    for x, col in enumerate(row):
        if col.isdigit():
            curr_num += col
            # Look around this position (brute force, no need to be fancy here)
            pos_to_check = [[x + 1, y], [x + 1, y - 1], [x, y - 1], [x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
            for pos in pos_to_check:
                if 0 <= pos[1] < y_max and 0 <= pos[0] < x_max and not input_list[pos[1]][pos[0]].isdigit() and input_list[pos[1]][pos[0]] != ".":
                    is_part = True
        else:
            if len(curr_num) > 0:
                if is_part:
                    parts.append(int(curr_num))
                    is_part = False
                curr_num = ''

    if len(curr_num) > 0:
        if is_part:
            parts.append(int(curr_num))
            is_part = False
        curr_num = ''

print(parts)
print(sum(parts))
