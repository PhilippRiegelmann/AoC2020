def read_file(txt):
    input = []
    with open(txt, "r") as f:
        input.append([0, ""])
        for line in f:
            if len(line) > 1:
                input[-1][1] = input[-1][1] + line.rstrip()
                input[-1][0] += 1
            else:
                input.append([0, ""])
    return input


def delete_duplications(input):
    without_duplications = []
    for i in range(len(input)):
        without_duplications.append("")
        for n in range(len(input[i][1])):
            if input[i][1][n] not in without_duplications[-1]:
                without_duplications[-1] = without_duplications[-1] + input[i][1][n]
    return without_duplications


def sum_answer_yes(input):
    sum = 0
    for i in range(len(input)):
        sum = sum + len(input[i])
    return sum


def count_votes(letter, input):
    count = 0
    for i in range(len(input)):
        if input[i] == letter:
            count += 1
    return count


def sum_all_yes(input):
    different_answers = delete_duplications(input)
    sum = 0
    for i in range(len(input)):
        for n in range(len(different_answers[i])):
            if count_votes(different_answers[i][n], input[i][1]) == input[i][0]:
                sum += 1
    return sum


def main():
    print(
        sum_answer_yes(
            delete_duplications(
                read_file("C:/Users/Phili/Documents/Projects/AoC_2020/6/input.txt")
            )
        )
    )
    print(
        sum_all_yes(read_file("C:/Users/Phili/Documents/Projects/AoC_2020/6/input.txt"))
    )


if __name__ == "__main__":
    main()