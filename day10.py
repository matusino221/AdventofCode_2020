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
    input_data = read_file("day10input.txt")
    data = input_data.copy()
    data = [int(i) for i in data]
    data.append(0)
    data = sorted(data)
    data.append(max(data) + 3)
    # data.append("")
    print("-----------------------------PART1-----------------------------------")
    n1 = 0
    n3 = 0
    for i in range(0, len(data) - 1):
        d = data[i + 1] - data[i]
        if d == 1:
            n1 += 1
        if d == 3:
            n3 += 1
    print(n1 * n3)
    print("-----------------------------PART2-----------------------------------")
    DP = {}


    def dp(i):
        if i == len(data) - 1:
            return 1
        if i in DP:
            return DP[i]
        ans = 0
        for j in range(i + 1, len(data)):
            if data[j] - data[i] <= 3:
                ans += dp(j)
        DP[i] = ans
        return ans


    print(dp(0))

    print()
    print()
    print()
