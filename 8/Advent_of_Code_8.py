def read_file(txt):
    list_of_instructions = []
    with open(txt, "r") as f:
        for line in f:
            instruction = []
            instruction = (line.rstrip()).split(" ")
            instruction.append(False)
            list_of_instructions.append(instruction)
    return list_of_instructions


def work_off(instructions, Try):
    work_off_instructions = instructions
    Round = 0
    accumulator = 0
    i = 0
    while i >= 0 and i < len(work_off_instructions):
        if work_off_instructions[i][2] == False:
            if (work_off_instructions[i][0]) == "acc":
                work_off_instructions[i][2] = True
                accumulator += int(work_off_instructions[i][1])
                i += 1
            elif (work_off_instructions[i][0]) == "jmp":
                if Try == Round:
                    work_off_instructions[i][2] = True
                    i += 1
                    Round += 1
                else:
                    work_off_instructions[i][2] = True
                    i += int(work_off_instructions[i][1])
                    Round += 1
            elif (work_off_instructions[i][0]) == "nop":
                if Try == Round:
                    work_off_instructions[i][2] = True
                    i += int(work_off_instructions[i][1])
                    Round += 1
                else:
                    work_off_instructions[i][2] = True
                    i += 1
                    Round += 1
        else:
            i = -1
    return accumulator, i


def amount_nop_in_instructions(list_of_instructions):
    amount = 0
    for i in range(len(list_of_instructions)):
        if (list_of_instructions[i][0]) == "nop":
            amount += 1
    return amount


def amount_jmp_in_instructions(list_of_instructions):
    amount = 0
    for i in range(len(list_of_instructions)):
        if (list_of_instructions[i][0]) == "jmp":
            amount += 1
    return amount


def main():
    list_of_instructions = read_file(
        "C:/Users/Phili/Documents/Projects/AoC_2020/8/input.txt"
    )
    acc, x = work_off(list_of_instructions, -1)
    print(acc)

    amount_options = amount_nop_in_instructions(
        list_of_instructions
    ) + amount_jmp_in_instructions(list_of_instructions)

    list_of_instructions = read_file(
        "C:/Users/Phili/Documents/Projects/AoC_2020/8/input.txt"
    )

    values = []
    for i in range(amount_options):
        acc, x = work_off(list_of_instructions, i)
        values.append(acc)
        if x == len(list_of_instructions):
            break
        list_of_instructions = read_file(
            "C:/Users/Phili/Documents/Projects/AoC_2020/8/input.txt"
        )

    print(values[-1])

    list_of_instructions = read_file(
        "C:/Users/Phili/Documents/Projects/AoC_2020/8/input.txt"
    )

    print(list_of_instructions[0])
    print(work_off(list_of_instructions, -1))
    print(list_of_instructions[0])
    print(work_off(list_of_instructions, -1))


if __name__ == "__main__":
    main()