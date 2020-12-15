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
    input_data = read_file("day15input.txt")
    data = input_data.copy()
    # data = [
        # "0,3,6",  # 436
        # "1,3,2",  # 1
        # "2,1,3",  # 10
        # "1,2,3",  # 27
        # "2,3,1",  # 78
        # "3,2,1",  # 438
        # "3,1,2",  # 1836
    # ]
    # data.append("")
    print("-----------------------------PART1-----------------------------------")
    starting_numbers = [int(i) for i in data[0].split(',')]
    print(starting_numbers)
    spoken = []
    turn = 0
    ignore = False
    while True:
        if not ignore:
            number = starting_numbers[turn % len(starting_numbers)]
        else:
            number = spoken[-1]
        # If that was the first time the number has been spoken, the current player says 0.
        if spoken.count(number) == 1:
            spoken.append(0)
            ignore = True
        # the current player announces how many turns apart the number is from when it was previously spoken.
        elif spoken.count(number) > 1:
            number_spoken_turn = [i + 1 for i, num in enumerate(spoken) if num == number]
            prev_number_spoken_turn = number_spoken_turn[-2]
            last_number_spoken_turn = number_spoken_turn[-1]
            spoken.append(abs(prev_number_spoken_turn - last_number_spoken_turn))
        elif starting_numbers[turn] not in spoken:
            spoken.append(starting_numbers[turn])
        turn += 1
        # print(turn)
        if turn >= 2020:
            break
    print("ans:", spoken[-1])

    print("-----------------------------PART2-----------------------------------")


    def play_memory_game(size):
        data = starting_numbers.copy()
        mem = {}
        for i in range(len(data) - 1):
            num = data[i]
            mem[num] = i

        for i in range(len(data) - 1, size - 1):
            num = data[i]
            if num not in mem:
                data.append(0)
                mem[num] = i
            else:
                j = mem[num]
                new_num = i - j
                data.append(new_num)
                mem[num] = i
        return data[-1]


    print("ans:", play_memory_game(2020))
    print("ans:", play_memory_game(30000000))
