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
    input_data = read_file("day13input.txt")
    data = input_data.copy()
    # data = [
    #     "939",
    #     "7,13,x,x,59,x,31,19",
    # ]
    # data.append("")
    print("-----------------------------PART1-----------------------------------")
    timestamp = int(data[0])
    bus_ids = [int(i) for i in data[1].split(',') if 'x' != i and ',' != i]
    schedule = dict()
    for bus_id in bus_ids:
        time = 0
        while time < timestamp:
            time += bus_id
        schedule[bus_id] = time
    print(schedule)
    print("{:<8} {:<15}".format('bus id', 'time'))
    [print("{:<8} {:<15}".format(k, v)) for k, v in schedule.items()]
    schedule = dict(sorted(schedule.items(), key=lambda x: x[1]))
    early_bus_id = list(schedule.keys())[0]
    early_timestamp = list(schedule.values())[0]
    print("ans:", (early_timestamp - timestamp) * early_bus_id)

    from sympy.ntheory.modular import crt

    # helped by https://www.youtube.com/watch?v=Cbqhp0S2BEw
    print("-----------------------------PART2-----------------------------------")
    bus_ids = [i for i in data[1].split(',') if ',' != i]
    modulos = []
    remainders = []
    for i in range(0, len(bus_ids)):
        if bus_ids[i].isnumeric():
            modulos.append(int(bus_ids[i]))
            remainders.append((-i) % modulos[-1])
    ans = crt(modulos, remainders)

    print(ans)
