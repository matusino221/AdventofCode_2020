import itertools
import re
import sys


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
    input_data = read_file("day9input.txt")
    # input_data = ["35",
    #               "20",
    #               "15",
    #               "25",
    #               "47",
    #               "40",
    #               "62",
    #               "55",
    #               "65",
    #               "95",
    #               "102",
    #               "117",
    #               "150",
    #               "182",
    #               "127",
    #               "219",
    #               "299",
    #               "277",
    #               "309",
    #               "576", ]
    input_data = [int(i) for i in input_data]
    data = input_data.copy()
    data.append("")
    print("-----------------------------PART1-----------------------------------")
    preamble = 25
    # preamble = 5
    for index in range(preamble, len(data)):
        ok = True
        previous = data[index - preamble:index]
        assert len(previous) == preamble
        for i, j in itertools.combinations(previous, 2):
            if i + j == data[index]:
                ok = False
        if ok:
            GOAL = data[index]
            print(data[index])
            break

    print("-----------------------------PART2-----------------------------------")
    for i in range(0, len(input_data)):
        sum_ = data[i]
        min_ = data[i]
        max_ = data[i]
        for j in range(i + 1, len(input_data)):
            sum_ += data[j]
            min_ = min(data[j], min_)
            max_ = max(data[j], max_)
            if sum_ == GOAL:
                print(min_ + max_)
    print()
    print()
    print()
