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


def get_acc_eof(input_data):
    data = input_data.copy()
    # data.append("")
    accumulator = 0
    all_index = [i for i in range(0, len(input_data))]
    index = 0
    commands = []
    commands_ids = []
    while index in all_index:
        commands_ids.append(index)
        command = data[index]
        all_index.remove(index)
        if 'nop' in command:
            commands.append(command)

        if 'acc' in command:
            commands.append(command)
            argument = command.split()[1]
            if '+' in argument:
                accumulator += int(argument[1:])
            if '-' in argument:
                accumulator -= int(argument[1:])

        if 'jmp' in command:
            commands.append(command)
            argument = command.split()[1]
            if '+' in argument:
                index += int(argument[1:])
                continue
            if '-' in argument:
                index -= int(argument[1:])
                continue
        index += 1

        if index >= len(input_data) - 1:
            return accumulator, True

    return accumulator, False


def get_acc_eof_(data):
    acc = 0
    line = 0
    instruction = []
    while line not in instruction:
        instruction.append(line)

        current_instruction = data[line]
        current_instruction = current_instruction.split()
        cmd = current_instruction[0]
        num = current_instruction[1]
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(num)

        if cmd == 'acc':
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1

        if line >= len(data) - 1:
            return acc, True, line
    return acc, False, line


if __name__ == "__main__":
    input_data = read_file("day8input.txt")
    # input_data = ["nop +0",
    #               "acc +1",
    #               "jmp +4",
    #               "acc +3",
    #               "jmp -3",
    #               "acc -99",
    #               "acc +1",
    #               "jmp -4",
    #               "acc +6"]
    data = input_data.copy()
    data.append("")
    print("-----------------------------PART1-----------------------------------")
    accumulator = get_acc_eof(input_data)
    print(get_acc_eof_(input_data))
    print(accumulator)
    print("-----------------------------PART2-----------------------------------")
    input_data_ = input_data.copy()
    input_data_[247] = input_data_[247].replace('jmp', 'nop')
    print(get_acc_eof(input_data_))
    input_data_ = input_data.copy()
    for i in range(len(input_data_)):
        if 'jmp' in input_data_[i]:
            input_data_[i] = input_data_[i].replace('jmp', 'nop')
            acc, found = get_acc_eof(input_data_)
            if found:
                print(acc, i)
                break
            else:
                input_data_[i] = input_data_[i].replace('nop', 'jmp')  # revert changes

    input_data_ = input_data.copy()
    for i in range(len(input_data_)):
        if 'nop' in input_data_[i]:
            input_data_[i] = input_data_[i].replace('nop', 'jmp')
            acc, found = get_acc_eof(input_data_)
            if found:
                print(acc, i)
                break
            else:
                input_data_[i] = input_data_[i].replace('jmp', 'nop')  # revert changes

    print()
    print()
    print()
