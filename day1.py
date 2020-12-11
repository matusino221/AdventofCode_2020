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
    number_from_file = [int(x) for x in read_file("day1input.txt")]

    print("-----------------------------PART1-----------------------------------")
    for num1 in number_from_file:
        for num2 in number_from_file:
            if ((num1 + num2) == 2020):
                print(num1, num2, num1 * num2)
    print("-----------------------------PART2-----------------------------------")
    for num1 in number_from_file:
        for num2 in number_from_file:
            for num3 in number_from_file:
                if ((num1 + num2 + num3) == 2020):
                    print(num1, num2, num3, num1 * num2 * num3)
