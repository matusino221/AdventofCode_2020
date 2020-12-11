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


# field_conditions = {'byr': lambda val: 1920 <= int(val) <= 2002,
#                     'iyr': lambda val: 2010 <= int(val) <= 2020,
#                     'eyr': lambda val: 2020 <= int(val) <= 2030,
#                     'hgt': lambda val: re.search('^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$', val),
#                     'hcl': lambda val: re.search('^#([a-f]|[0-9]){6}$', val),
#                     'ecl': lambda val: val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
#                     'pid': lambda val: re.search('^[0-9]{9}$', val)}
#
#
# def is_valid2(f):
#     for field, condition in field_conditions.items():
#         if field not in f or not condition(f[field]):
#             return False
#     return True

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
    input_data = read_file("day4input.txt")
    must_keys = [
        'byr',  # (Birth Year)
        'ecl',  # (Eye Color)
        'eyr',  # (Expiration Year)
        'hcl',  # (Hair Color)
        'hgt',  # (Height)
        'iyr',  # (Issue Year)
        'pid',  # (Passport ID)
        # 'cid',   (Country ID)
    ]
    # 250
    print("-----------------------------PART1-----------------------------------")
    passport_valid = []
    passport = dict()
    count_valid_passports = 0
    for line in input_data:
        if line != '':
            for item in line.split(' '):
                key, value = item.split(':')
                passport[key] = value
        else:
            keys_sorted = sorted(passport, key=str.lower)
            keys = [key for key in keys_sorted if key != 'cid']
            if set(must_keys) == set(keys):
                count_valid_passports += 1
            passport_valid.append(passport)
            passport = dict()
    if passport != {}:
        keys_sorted = sorted(passport, key=str.lower)
        keys = [key for key in keys_sorted if key != 'cid']
        if set(must_keys) == set(keys):
            count_valid_passports += 1
        passport_valid.append(passport)

    print(count_valid_passports)
    # 158
    print("-----------------------------PART2-----------------------------------")
    passport_valid = []
    passport = dict()
    count_valid_passports = 0
    for line in input_data:
        if line != '':
            for item in line.split(' '):
                key, value = item.split(':')
                passport[key] = value
        else:
            keys_sorted = sorted(passport, key=str.lower)
            keys = [key for key in keys_sorted if key != 'cid']
            if set(must_keys) == set(keys) and is_valid(passport):
                count_valid_passports += 1
            passport_valid.append(passport)
            passport = dict()
    if passport != {}:
        keys_sorted = sorted(passport, key=str.lower)
        keys = [key for key in keys_sorted if key != 'cid']
        if set(must_keys) == set(keys) and is_valid(passport):
            count_valid_passports += 1
        passport_valid.append(passport)

    print(count_valid_passports)
