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
    read_from_file = read_file("day2input.txt")
    # read_from_file = ["1-3 a: abcde",
    #                   "1-3 b: cdefg",
    #                   "2-9 c: ccccccccc"]

    print("-----------------------------PART1-----------------------------------")
    number_of_passwords = 0
    for line in read_from_file:
        line = line.split(' ')
        num_min, num_max = [int(x) for x in line[0].split('-')]
        char = line[1].split(':')[0]
        passwords = line[2]
        # if ((char in passwords[num1]) and (char in passwords[num2])):
        if (passwords.count(char) >= num_min) and (passwords.count(char) <= num_max):
            number_of_passwords += 1
    print(number_of_passwords)
    print("-----------------------------PART2-----------------------------------")
    number_of_passwords = 0
    for line in read_from_file:
        line = line.split(' ')
        num1, num2 = [int(x) - 1 for x in line[0].split('-')]
        char = line[1].split(':')[0]
        passwords = line[2]
        if ((not (char in passwords[num1]) and (char in passwords[num2])) or (
                (char in passwords[num1]) and not (char in passwords[num2]))):
            number_of_passwords += 1
    print(number_of_passwords)
