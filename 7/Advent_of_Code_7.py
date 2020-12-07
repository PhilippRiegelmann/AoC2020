import re
from typing import Literal


def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            input.append(line)
    return input


def find_rules(input):
    list_of_rules = []
    find_container = re.compile("([^\/]*) bags contain")
    find_content = re.compile("(\d) (\D*) bag")
    for i in range(len(input)):
        rule = []
        for match in re.finditer(find_container, input[i]):
            container = match.groups()[0]
            rule.append(container)
        content = {}
        for match in re.finditer(find_content, input[i]):
            content[match.groups()[1]] = match.groups()[0]
        rule.append(content)
        list_of_rules.append(rule)
    return list_of_rules


def bags_carry(rules, bags):
    bags_which_contains_bags = []
    for i in range(len(bags)):
        for n in range(len(rules)):
            if bags[i] in rules[n][1]:
                bags_which_contains_bags.append(rules[n][0])
    return bags_which_contains_bags


def delete_duplicates(input):
    without_duplicates = []
    for i in range(len(input)):
        if input[i] not in without_duplicates:
            without_duplicates.append(input[i])
    return without_duplicates


def main():
    rules = find_rules(
        read_file("C:/Users/Phili/Documents/Projects/AoC_2020/7/input.txt")
    )
    bags = bags_carry(rules, ["shiny gold"])
    i = 1
    while i != 0:
        before = len(bags)
        bags = delete_duplicates(bags + bags_carry(rules, bags))
        after = len(bags)
        i = after - before
    print(len(bags))

    test = find_rules(
        read_file("C:/Users/Phili/Documents/Projects/AoC_2020/7/input.txt")
    )
    print(test[1])


# )


if __name__ == "__main__":
    main()