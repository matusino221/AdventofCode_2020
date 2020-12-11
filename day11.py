import re
import sys
from copy import deepcopy


def read_file(filename):
    try:
        with open(filename) as f:
            content = f.readlines()

        # I converted the file data to integers because I know
        # that the input data is made up of numbers greater than 0
        content = [info.strip() for info in content]

    except:
        print('Error to read file')
        sys.exit()

    return content


if __name__ == "__main__":
    input_data = read_file("day11input.txt")
    data = input_data.copy()
    # data = [
    #     "L.LL.LL.LL",
    #     "LLLLLLL.LL",
    #     "L.L.L..L..",
    #     "LLLL.LL.LL",
    #     "L.LL.LL.LL",
    #     "L.LLLLL.LL",
    #     "..L.L.....",
    #     "LLLLLLLLLL",
    #     "L.LLLLLL.L",
    #     "L.LLLLL.LL",
    # ]
    # data.append("")
    print("-----------------------------PART1-----------------------------------")
    seats_occupied = 0
    seats_occupied_prev = -1
    data_strip = [list(i.strip()) for i in data]
    while seats_occupied_prev != seats_occupied:
        new_data_strip = deepcopy(data_strip)
        for i in range(len(data_strip)):
            for j in range(len(data_strip[0])):
                nocc = 0
                # actual place is i,j
                # check all place around
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if not (di == 0 and dj == 0):  # is not a actual place
                            ii = i + di
                            jj = j + dj
                            # place is not empty
                            if 0 <= ii < len(data_strip) and 0 <= jj < len(data_strip[0]) and data_strip[ii][jj] == '#':
                                nocc += 1

                if data_strip[i][j] == 'L' and nocc == 0:
                    new_data_strip[i][j] = '#'
                elif data_strip[i][j] == '#' and nocc >= 4:
                    new_data_strip[i][j] = 'L'

        data_strip = deepcopy(new_data_strip)
        seats_occupied_prev = seats_occupied
        seats_occupied = sum([row.count('#') for row in data_strip])

    for line in data_strip:
        print("".join(line))
    seats_occupied = sum([row.count('#') for row in data_strip])
    print(seats_occupied)
    print("-----------------------------PART2-----------------------------------")
    seats_occupied = 0
    seats_occupied_prev = -1
    data_strip = [list(i.strip()) for i in data]
    while seats_occupied_prev != seats_occupied:
        new_data_strip = deepcopy(data_strip)
        for i in range(len(data_strip)):
            for j in range(len(data_strip[0])):
                nocc = 0
                # actual place is i,j
                # check all place around
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if not (di == 0 and dj == 0):  # is not a actual place
                            ii = i + di
                            jj = j + dj

                            while 0 <= ii < len(data_strip) and 0 <= jj < len(data_strip[0]) and data_strip[ii][
                                jj] == '.':
                                ii += di
                                jj += dj
                            # place is not empty
                            if 0 <= ii < len(data_strip) and 0 <= jj < len(data_strip[0]) and data_strip[ii][jj] == '#':
                                nocc += 1

                if data_strip[i][j] == 'L' and nocc == 0:
                    new_data_strip[i][j] = '#'
                elif data_strip[i][j] == '#' and nocc >= 5:
                    new_data_strip[i][j] = 'L'

        data_strip = deepcopy(new_data_strip)
        seats_occupied_prev = seats_occupied
        seats_occupied = sum([row.count('#') for row in data_strip])

    for line in data_strip:
        print("".join(line))
    seats_occupied = sum([row.count('#') for row in data_strip])
    print(seats_occupied)
