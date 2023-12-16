import re


# function to get unique values
def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for item in list1:
        # check if exists in unique_list or not
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


input_list = list()
with open('input.txt') as f:
    [input_list.append([*line.replace('\n', '')]) for line in f.readlines()]

y_max = len(input_list[0])
x_max = len(input_list)

ratios = list()
for y, row in enumerate(input_list):
    for x, col in enumerate(row):
        if "*" == col:
            parts_pos = list()
            # Look around this position (brute force, no need to be fancy here)
            pos_to_check = [[x + 1, y], [x + 1, y - 1], [x, y - 1], [x - 1, y - 1], [x - 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
            # We have to scan all pos around to count
            for pos in pos_to_check:
                if 0 <= pos[1] < y_max and 0 <= pos[0] < x_max and input_list[pos[1]][pos[0]].isdigit():
                    parts_pos.append(pos)

            if len(parts_pos) >= 2:
                parts_pos_hash = [[] for _ in range(len(parts_pos))]
                c = 0
                for part_pos in parts_pos:
                    parts_pos_hash[c].append(part_pos)
                    # Look right
                    lookup = part_pos[0] + 1
                    while lookup < x_max:
                        next_char = input_list[part_pos[1]][lookup]
                        if next_char.isdigit():
                            parts_pos_hash[c].append([lookup, part_pos[1]])
                            lookup += 1
                        else:
                            break

                    # Look left
                    lookup = part_pos[0] - 1
                    while lookup < x_max:
                        next_char = input_list[part_pos[1]][lookup]
                        if next_char.isdigit():
                            parts_pos_hash[c].insert(0, [lookup, part_pos[1]])
                            lookup -= 1
                        else:
                            break
                    c += 1

                # Remove duplicate positions
                unique_parts_pos = unique(parts_pos_hash)
                # This ensures we're not counting the same number twice
                if len(unique_parts_pos) == 2:
                    ratio = 1
                    for unique_p_pos in unique_parts_pos:
                        part_string = ''
                        for pos in unique_p_pos:
                            part_string += input_list[pos[1]][pos[0]]
                        ratio *= int(part_string)

                    print('found gear at', y+1, x+1)
                    print('ratio', ratio)
                    ratios.append(ratio)

print(ratios)
print(sum(ratios))
