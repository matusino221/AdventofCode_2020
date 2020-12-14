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


def indices(new_mem_number, floating):
    if len(floating) == 0:
        return [new_mem_number]
    else:
        b0 = floating.pop(0)
        ans = indices(new_mem_number, list(floating)) + indices(new_mem_number + 2 ** b0, list(floating))
        return ans


if __name__ == "__main__":
    input_data = read_file("day14input.txt")
    data = input_data.copy()
    # data = [
    #     "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    #     "mem[8] = 11",
    #     "mem[7] = 101",
    #     "mem[8] = 0",
    # ]
    # data.append("")
    print("-----------------------------PART1-----------------------------------")
    mem = dict()
    mask = b""
    for line in data:
        if 'mask' in line:
            mask = line.strip().split('=')[1].strip()
        if 'mem' in line:
            mem_number = int(line.strip().split('=')[0][4:-2])
            number = int(line.strip().split('=')[1])
            new_number = 0
            for i, bit in enumerate(reversed(mask)):
                vbit = number & (2 ** i)
                if bit == 'X':
                    new_number += vbit
                elif bit == '1':
                    new_number += 2 ** i
                elif bit == '0':
                    pass
                else:
                    assert False
            mem[mem_number] = new_number
    print(sum(mem.values()))
    print("-----------------------------PART2-----------------------------------")

    # data = [
    #     "mask = 000000000000000000000000000000X1001X",
    #     "mem[42] = 100",
    #     "mask = 00000000000000000000000000000000X0XX",
    #     "mem[26] = 1",
    # ]
    mem = dict()
    mask = b""
    for line in data:
        if 'mask' in line:
            mask = line.strip().split('=')[1].strip()
        if 'mem' in line:
            mem_number = int(line.strip().split('=')[0][4:-2])
            number = int(line.strip().split('=')[1])
            new_mem_number = 0
            floating = []
            for i, bit in enumerate(reversed(mask)):
                ibit = mem_number & (2 ** i)
                if bit == 'X':
                    floating.append(i)
                elif bit == '1':
                    new_mem_number += 2 ** i
                elif bit == '0':
                    new_mem_number += ibit
                    pass
                else:
                    assert False
            for idx in indices(new_mem_number, list(floating)):
                mem[idx] = number
    print(sum(mem.values()))
