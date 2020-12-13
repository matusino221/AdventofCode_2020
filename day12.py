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
    input_data = read_file("day12input.txt")
    data = input_data.copy()
    # data = [
    #     "F10",
    #     "N3",
    #     "F7",
    #     "R90",
    #     "F11",
    # ]
    compass = ['E', 'S', 'W', 'N']
    map = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    compass_index = 0
    # data.append("")
    print("-----------------------------PART1-----------------------------------")
    for instruction in data:
        action = instruction[:1]
        number = int(instruction[1:])

        if "N" in instruction:
            map[action] += number
        if "S" in instruction:
            map[action] += number
        if "E" in instruction:
            map[action] += number
        if "W" in instruction:
            map[action] += number
        if "L" in instruction:
            degrees = int(number / 90)
            for i in range(0, degrees):
                compass_index = ((compass_index - 1) % len(compass))
        if "R" in instruction:
            degrees = int(number / 90)
            for i in range(0, degrees):
                compass_index = ((compass_index + 1) % len(compass))
        if "F" in instruction:
            direction = compass[compass_index]
            map[direction] += number

    manhattan_distance_list = []
    manhattan_distance_list.append(abs(map['E'] - map['W']))
    manhattan_distance_list.append(abs(map['N'] - map['S']))
    manhattan_distance = sum(manhattan_distance_list)
    print("manhattan distance", manhattan_distance)
    print("manhattan distance", manhattan_distance, manhattan_distance_list)
    print("-----------------------------PART2-----------------------------------")

    compass = ['E', 'S', 'W', 'N']
    map = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    waypoint = {'E': 10, 'S': 0, 'W': 0, 'N': 1}
    for instruction in data:
        action = instruction[:1]
        number = int(instruction[1:])

        if "N" in instruction:
            waypoint[action] += number
        if "S" in instruction:
            waypoint[action] += number
        if "E" in instruction:
            waypoint[action] += number
        if "W" in instruction:
            waypoint[action] += number
        if "L" in instruction:
            # before waypoint {'E': 10, 'S': 0, 'W': 0, 'N': 4}
            degrees = int(number / 90)
            for i in range(0, degrees):
                waypoint['E'], waypoint['S'], waypoint['W'], waypoint['N'] = waypoint['S'], waypoint['W'], waypoint[
                    'N'], waypoint['E']
            # after waypoint {'E': 0, 'S': 0, 'W': 4, 'N': 10}
        if "R" in instruction:
            # before waypoint {'E': 10, 'S': 0, 'W': 0, 'N': 4}
            degrees = int(number / 90)
            for i in range(0, degrees):
                waypoint['E'], waypoint['S'], waypoint['W'], waypoint['N'] = waypoint['N'], waypoint['E'], waypoint[
                    'S'], waypoint['W']
            # after waypoint {'E': 4, 'S': 10, 'W': 0, 'N': 0}
        if "F" in instruction:
            for key, value in waypoint.items():
                map[key] += value * number

    manhattan_distance_list = []
    manhattan_distance_list.append(abs(map['E'] - map['W']))
    manhattan_distance_list.append(abs(map['N'] - map['S']))
    manhattan_distance = sum(manhattan_distance_list)
    print("manhattan distance", manhattan_distance)
    print("manhattan distance", manhattan_distance, manhattan_distance_list)
