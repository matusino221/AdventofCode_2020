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
    read_from_file_basic = read_file("day3input.txt")
    # read_from_file = ["""
    #                 ..##.......
    #                 #...#...#..
    #                 .#....#..#.
    #                 ..#.#...#.#
    #                 .#...##..#.
    #                 ..#.##.....
    #                 .#.#.#....#
    #                 .#........#
    #                 #.##...#...
    #                 #...##....#
    #                 .#..#...#.#
    #                     """]
    read_from_file = [row * 35 for row in read_from_file_basic]

    print("-----------------------------PART1-----------------------------------")
    read_from_file = [row * 35 for row in read_from_file_basic]
    pos = 0
    for index, row in enumerate(read_from_file):
        if index == 0:
            continue
        pos += 3
        if row[pos] == "#":
            read_from_file[index] = row[:pos] + "X" + row[pos + 1:]
        if row[pos] == ".":
            read_from_file[index] = row[:pos] + "O" + row[pos + 1:]

    for row in read_from_file:
        print(row * 1)

    print(sum([row.count("X") for row in read_from_file]))
    print("-----------------------------PART2-----------------------------------")
    print("Right 1, down 1.")
    read_from_file = [row * 35 for row in read_from_file_basic]
    pos = 0
    for index, row in enumerate(read_from_file):
        if index == 0:
            continue
        pos += 1
        if row[pos] == "#":
            read_from_file[index] = row[:pos] + "X" + row[pos + 1:]
        if row[pos] == ".":
            read_from_file[index] = row[:pos] + "O" + row[pos + 1:]
    num1 = sum([row.count("X") for row in read_from_file])
    print(num1)
    print("Right 3, down 1.")
    read_from_file = [row * 35 for row in read_from_file_basic]
    pos = 0
    for index, row in enumerate(read_from_file):
        if index == 0:
            continue
        pos += 3
        if row[pos] == "#":
            read_from_file[index] = row[:pos] + "X" + row[pos + 1:]
        if row[pos] == ".":
            read_from_file[index] = row[:pos] + "O" + row[pos + 1:]
    num2 = sum([row.count("X") for row in read_from_file])
    print(num2)
    print("Right 5, down 1.")
    read_from_file = [row * 500 for row in read_from_file_basic]
    pos = 0
    for index, row in enumerate(read_from_file):
        if index == 0:
            continue
        pos += 5
        if row[pos] == "#":
            read_from_file[index] = row[:pos] + "X" + row[pos + 1:]
        if row[pos] == ".":
            read_from_file[index] = row[:pos] + "O" + row[pos + 1:]
    num3 = sum([row.count("X") for row in read_from_file])
    print(num3)
    print("Right 7, down 1.")
    read_from_file = [row * 500 for row in read_from_file_basic]
    pos = 0
    for index, row in enumerate(read_from_file):
        if index == 0:
            continue
        pos += 7
        if row[pos] == "#":
            read_from_file[index] = row[:pos] + "X" + row[pos + 1:]
        if row[pos] == ".":
            read_from_file[index] = row[:pos] + "O" + row[pos + 1:]
    num4 = sum([row.count("X") for row in read_from_file])
    print(num4)
    print("Right 1, down 2.")
    read_from_file = [row * 35 for row in read_from_file_basic]
    pos = 0
    for index in range(0, len(read_from_file), 2):
        if index == 0:
            continue
        pos += 1
        if read_from_file[index][pos] == "#":
            read_from_file[index] = read_from_file[index][:pos] + "X" + read_from_file[index][pos + 1:]
        if read_from_file[index][pos] == ".":
            read_from_file[index] = read_from_file[index][:pos] + "O" + read_from_file[index][pos + 1:]
    num5 = sum([row.count("X") for row in read_from_file])
    print(num5)
    print(num1 * num2 * num3 * num4 * num5)
