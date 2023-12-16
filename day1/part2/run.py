import json
import re

file = open("input.json", "r")
# file = open("input_example.json", "r")
input_data = list(json.load(file))
file.close()
replace_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
search_pattern = r'one|two|three|four|five|six|seven|eight|nine'
entries_to_replace = replace_dict.keys()

print(input_data)
outnum = 0
output = list()
for s in input_data:
    search_space = ''
    left = ''
    right = ''
    for c in s:
        if c.isdigit():
            left = c
            break
        else:
            search_space += c
            match = re.search(search_pattern, search_space)
            if match:
                left = replace_dict[match.group()]
                break

    search_space = ''
    for cr in s[::-1]:
        if cr.isdigit():
            right = cr
            break
        else:
            search_space = cr + search_space
            match = re.search(search_pattern, search_space)
            if match:
                right = replace_dict[match.group()]
                break

    outnum += int(left + right)
    output.append(left + right)

print(output)
print(outnum)
