import time

input = []

with open("C:/Users/Phili/Documents/Projects/AoC_2020/2/input.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())


def sort(list):
    sorted = []
    for i in range(len(list)):
        sorted.append(list[i].split(" "))
        sorted[-1][0] = sorted[-1][0].split("-")
        sorted[-1][0][0] = int(sorted[-1][0][0])
        sorted[-1][0][1] = int(sorted[-1][0][1])
        sorted[-1][1] = sorted[-1][1][0]
    return sorted


def number_valid1(list):
    amount_valid = 0
    for i in range(len(list)):
        number = 0
        for letter in list[i][2]:
            if letter in list[i][1]:
                number += 1
        if number >= list[i][0][0] and number <= list[i][0][1]:
            amount_valid += 1
    return amount_valid


def number_valid2(list):
    amount_valid = 0
    for i in range(len(list)):
        number = 0
        if (
            list[i][2][list[i][0][0] - 1] == list[i][1]
            and list[i][2][list[i][0][1] - 1] != list[i][1]
        ) or (
            list[i][2][list[i][0][0] - 1] != list[i][1]
            and list[i][2][list[i][0][1] - 1] == list[i][1]
        ):
            amount_valid += 1
    return amount_valid


input = sort(input)
start = time.perf_counter()
print(number_valid1(input), time.perf_counter() - start)
start = time.perf_counter()
print(number_valid2(input), time.perf_counter() - start)
