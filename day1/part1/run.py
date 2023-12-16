import json

file = open("input.json", "r")
input_data = list(json.load(file))
file.close()

print(input_data)

output = 0
for s in input_data:
    left = ''
    right = ''
    for c in s:
        if c.isdigit():
            left = c
            break
    for cr in s[::-1]:
        if cr.isdigit():
            right = cr
            break

    output += int(left + right)

print(output)
