def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            input.append(int(line))
    return input


def num_1_and_3_jolt_differences(list_of_adapter):
    num_1_jolt_differences = 0
    num_3_jolt_differences = 0
    for i in range(1, len(list_of_adapter)):
        diff = list_of_adapter[i] - list_of_adapter[i - 1]
        if diff == 1:
            num_1_jolt_differences += 1
        elif diff == 3:
            num_3_jolt_differences += 1
    return num_1_jolt_differences, num_3_jolt_differences


def main():
    adapters = [0] + sorted(
        read_file("C:/Users/Phili/Documents/Projects/AoC_2020/10/input.txt")
    )
    adapters.append(max(adapters) + 3)
    num1, num3 = num_1_and_3_jolt_differences(adapters)
    print(num1 * num3)


if __name__ == "__main__":
    main()