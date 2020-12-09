import re


def read_file(txt):
    input = []
    with open(txt, "r") as f:
        input.append("")
        for line in f:
            if len(line) > 1:
                input[-1] = input[-1] + line.rstrip() + " "
            else:
                input.append("")
        for i in range(len(input)):
            input[i] = input[i][:-1]
    return input


def sort(input):
    for i in range(len(input)):
        input[i] = dict(x.split(":") for x in input[i].split(" "))
    return input


def number_valid(input):
    valid = []
    for i in range(len(input)):
        if (
            "byr" in input[i]
            and "iyr" in input[i]
            and "eyr" in input[i]
            and "hgt" in input[i]
            and "hcl" in input[i]
            and "ecl" in input[i]
            and "pid" in input[i]
        ):
            valid.append(input[i])

    return valid


def valid_byr(byr):
    return int(byr) >= 1920 and int(byr) <= 2002


def valid_iyr(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020


def valid_eyr(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030


def valid_hgt(hgt):
    hgtcm = 0
    hgtin = 0
    Number_cm = re.compile("(\d*)cm")
    Number_in = re.compile("(\d*)in")
    for match in re.finditer(Number_cm, hgt):
        hgtcm = int(match.groups()[0])
    for match in re.finditer(Number_in, hgt):
        hgtin = int(match.groups()[0])
    return (hgtcm >= 150 and hgtcm <= 193) or (hgtin >= 59 and hgtin <= 76)


def valid_hcl(hcl):
    lennumhcl = 0
    numhcl = re.compile("#([^\/]*)")
    for match in re.finditer(numhcl, hcl):
        lennumhcl = len((match.groups()[0]))
    return lennumhcl == 6


def valid_ecl(ecl):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid


def valid_pid(pid):
    return len(pid) == 9


def information_valid(input):
    valid_passports = []
    for i in range(len(input)):
        if (
            valid_byr(input[i]["byr"])
            and valid_iyr(input[i]["iyr"])
            and valid_eyr(input[i]["eyr"])
            and valid_hgt(input[i]["hgt"])
            and valid_hcl(input[i]["hcl"])
            and valid_ecl(input[i]["ecl"])
            and valid_pid(input[i]["pid"])
        ):
            valid_passports.append(input[i])
    return len(valid_passports)


def main():
    allreqfields = number_valid(
        sort(read_file("C:/Users/Phili/Documents/Projects/AoC_2020/4/input.txt"))
    )
    print(len(allreqfields))
    print(information_valid(allreqfields))


if __name__ == "__main__":
    main()