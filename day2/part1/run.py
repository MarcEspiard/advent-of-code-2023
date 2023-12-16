input_list = list()
with open('input.txt') as f:
    [input_list.append(line.replace('\n', '').replace(' ', '')) for line in f.readlines()]

possible = list()
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
    for game in games:
        colors = game.split(',')
        for color in colors:
            numCubes = int(color.replace('blue', '').replace('red', '').replace('green', ''))
            if numCubes > max_red and "red" in color:
                is_possible = False
                break
            if numCubes > max_green and "green" in color:
                is_possible = False
                break
            if numCubes > max_blue and "blue" in color:
                is_possible = False
                break
        else:
            continue
        break

    if is_possible:
        possible.append(int(gameId))

print('Total:', sum(possible))
