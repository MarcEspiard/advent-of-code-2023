from functools import reduce

input_list = list()
with open('input.txt') as f:
    [input_list.append(line.replace('\n', '').replace(' ', '')) for line in f.readlines()]

powers = list()
max_red = 12
max_green = 13
max_blue = 14

for gameRow in input_list:
    # print(gameRow)
    splits = gameRow.split(':')
    gameId = splits[0].replace('Game', '')
    # print(gameId)
    games = splits[1].split(';')
    is_possible = True

    # [R,G,B]
    maxes = list([0, 0, 0])

    for game in games:
        colors = game.split(',')
        for color in colors:
            numCubes = int(color.replace('blue', '').replace('red', '').replace('green', ''))
            if "red" in color:
                maxes[0] = max(maxes[0], numCubes)
                continue
            if "green" in color:
                maxes[1] = max(maxes[1], numCubes)
                continue
            if "blue" in color:
                maxes[2] = max(maxes[2], numCubes)
                continue

    powers.append(reduce((lambda x, y: x * y), maxes))

print('Total:', sum(powers))
