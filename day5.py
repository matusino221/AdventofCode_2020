import math
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


def is_valid(content):
    result = True
    try:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = re.search("[0-9]{4}", content['byr'])
        # if (int(byr.group()) < 1920) or (int(byr.group()) > 2002):
        if not 1920 <= int(byr.group()) <= 2002:
            result = False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = re.search("[0-9]{4}", content['iyr'])
        # if (int(iyr.group()) < 2010) or (int(iyr.group()) > 2020):
        if not 2010 <= int(iyr.group()) <= 2020:
            result = False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = re.search("[0-9]{4}", content['eyr'])
        # if (int(eyr.group()) < 2020) or (int(eyr.group()) > 2030):
        if not 2020 <= int(eyr.group()) <= 2030:
            result = False
        # hgt (Height) - a number followed by either cm or in:
        hgt = re.search("^[0-9]+(cm|in)$", content['hgt'])
        # If cm, the number must be at least 150 and at most 193.
        if hgt:
            if "cm" in hgt.group():
                hgt_ = hgt.group()[:-2]
                # if (int(hgt_) <= 150) or (int(hgt_) >= 193):
                if not 150 <= int(hgt_) <= 193:
                    result = False
            # If in, the number must be at least 59 and at most 76.
            if "in" in hgt.group():
                hgt_ = hgt.group()[:-2]
                # if (int(hgt_) <= 59) or (int(hgt_) >= 76):
                if not 59 <= int(hgt_) <= 76:
                    result = False
        else:
            result = False
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        hcl = re.search("^#([a-f]|[0-9]){6}$", content['hcl'])
        if not hcl:
            result = False

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        ecl = re.search("(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)", content['ecl'])
        if not ecl:
            result = False
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid = re.search("^[0-9]{9}$", content['pid'])
        if not pid:
            result = False
        # cid (Country ID) - ignored, missing or not.
        # ignored
    except:
        result = False

    return result


if __name__ == "__main__":
    input_data = read_file("day5input.txt")
    # F means "front"
    # B means "back"
    # L means "left"
    # R means "right"
    print("-----------------------------PART1-----------------------------------")
    # first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127)

    boarding_pass = []
    for seat in input_data:
        row = [0, 127]
        column = [0, 7]
        for char in seat:
            if char == 'F':
                row[1] = row[0] + ((row[1] - row[0]) // 2)
            if char == "B":
                row[0] = row[1] - ((row[1] - row[0]) // 2)
            if char == 'R':
                column[0] = column[1] - ((column[1] - column[0]) // 2)
            if char == 'L':
                column[1] = column[0] + ((column[1] - column[0]) // 2)
        seat_id = row[0] * 8 + column[0]
        boarding_pass.append(seat_id)
    print(max(boarding_pass))
    print("-----------------------------PART2-----------------------------------")
    free_seats = list(range(0, 128 * 8 - 1))
    [free_seats.remove(seat) for seat in boarding_pass]
    [print(free_seat) for free_seat in free_seats if
     not free_seat - 1 in free_seats and not free_seat + 1 in free_seats]
