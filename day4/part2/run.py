import re

input_list = list()
with open('input.txt') as f:
    [input_list.append(line.replace('\n', '')) for line in f.readlines()]

list_max = len(input_list)
# print(input_list)
_RE_COMBINE_WHITESPACE = re.compile(r"\s+")
cards_processed = list()
card_map = [1 for _ in range(len(input_list))]

for index, row in enumerate(input_list):
    splits = row.split(':')
    all_numbers = splits[1].split('|')
    winning_numbers = _RE_COMBINE_WHITESPACE.sub(" ", all_numbers[0]).strip().split(' ')
    my_numbers = _RE_COMBINE_WHITESPACE.sub(" ", all_numbers[1]).strip().split(' ')

    found = 0
    for num in my_numbers:
        if num in winning_numbers:
            found += 1

    if found > 0:
        for y in range(found):
            cm_index = index + y + 1
            if 0 <= cm_index < list_max:
                card_map[cm_index] += 1 * card_map[index]

    cards_processed.append(card_map[index])

print(card_map)
print(cards_processed)
print(sum(cards_processed))
