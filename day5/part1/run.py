import re

input_list = list()
with open('input.txt') as f:
    [input_list.append(line.replace('\n', '')) for line in f.readlines()]

seeds = input_list[0].strip().replace('seeds: ', '').split(' ')

tables = dict()

current_dict_key = None
# Remove first 2 lines from input, already processed
for row in input_list[2:]:
    if not row:
        continue
        # break

    if '-to-' in row:
        dest_name = row.split(' ')[0].split('-')[2]
        src_name = row.split(' ')[0].split('-')[0]
        tables[src_name] = dict({"dest_name": dest_name, "table": list()})
        current_dict_key = src_name
    else:
        map_numbers = row.strip().split(' ')
        tables[current_dict_key]["table"].append(dict({"src": map_numbers[1], "dest": map_numbers[0], "len": map_numbers[2]}))

print(tables)

locations = list()

for curr_seed in seeds:
    print('processing', curr_seed)

    step = 'seed'
    matches = dict({step: curr_seed})
    while step is not None:
        if step in tables:
            print('Step', step)
            match = None
            for entry in tables[step]["table"]:
                src_range_start = int(entry["src"])
                src_range_end = src_range_start + (int(entry["len"]) - 1)
                dest_range_start = int(entry["dest"])
                dest_range_end = dest_range_start + (int(entry["dest"]) - 1)
                print('range src', src_range_start, src_range_end)
                step_int = int(matches[step])
                if src_range_start <= step_int <= src_range_end:
                    from_start_pos = step_int - src_range_start
                    match = dest_range_start + from_start_pos

            # Default to same value
            if match is None:
                match = matches[step]

            step = tables[step]["dest_name"]
            matches[step] = match
        else:
            step = None
            print('Next seed')
    locations.append(matches['location'])

print(locations)
print(min(locations))
