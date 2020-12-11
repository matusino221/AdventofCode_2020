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


def get_num_bags(color, data):
    lines = [line for line in data if color in line and line.index(color) != 0]
    all_colors = list()
    if len(lines) == 0:
        return []
    else:
        colors = [line[:line.index(' bags')] for line in lines]
        colors = [color for color in colors if color not in all_colors]

        for color in colors:
            all_colors.append(color)
            bags = get_num_bags(color, data)

            all_colors += bags

        unique_colors = list()
        for color in all_colors:
            if color not in unique_colors:
                unique_colors.append(color)

        return unique_colors


def get_bag_count(color, data):
    rule = ''
    for line in data:
        if line[:line.index(' bags')] == color:
            rule = line

    if 'no' in rule:
        return 1

    rule = rule[rule.index('contain') + 8:].split()
    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        color = rule[i + 1] + ' ' + rule[i + 2]

        total += count * get_bag_count(color, data)
        i += 4

    return total + 1


if __name__ == "__main__":
    input_data = read_file("day7input.txt")
    # print(input_data)
    # input_data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
    #               "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    #               "bright white bags contain 1 shiny gold bag.",
    #               "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    #               "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    #               "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    #               "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    #               "faded blue bags contain no other bags.",
    #               "dotted black bags contain no other bags."]
    data = input_data.copy()
    data.append("")
    print("-----------------------------PART1-----------------------------------")
    colors = get_num_bags('shiny gold', data)
    print(len(colors))
    # 11311 high # 5655 low
    print("-----------------------------PART2-----------------------------------")
    total = get_bag_count('shiny gold', input_data)
    print(total - 1)
