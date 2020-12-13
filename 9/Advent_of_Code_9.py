def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            input.append(int(line))
    return input


def check_if_valid(listinput, length_sum, listinput_index):
    sum_numbers = []
    valid = False
    for i in range(listinput_index - length_sum, listinput_index):
        sum_numbers.append(listinput[i])
    for i in sum_numbers:
        if (listinput[listinput_index] - i) in sum_numbers and i != listinput[
            listinput_index
        ] / 2:
            valid = True
            break
    return valid


def find_invalid_number(length_sum, numbers):
    for i in range(length_sum + 1, len(numbers)):
        if not check_if_valid(numbers, length_sum, i):
            invalid_number = numbers[i]
            invalid_number_index = i
            break
    return invalid_number, invalid_number_index


def find_set(listinput, index_invalid_number):
    sum_numbers = []
    for i in range(index_invalid_number - 1, -1, -1):
        sum_numbers.append(listinput[i])
        if sum(sum_numbers) == listinput[index_invalid_number]:
            break
        elif sum(sum_numbers) > listinput[index_invalid_number]:
            sum_numbers.pop(0)
    return sum_numbers


def main():
    numbers = read_file("C:/Users/Phili/Documents/Projects/AoC_2020/9/input.txt")
    print(find_invalid_number(25, numbers)[0])
    set_sum_invalid = find_set(numbers, find_invalid_number(25, numbers)[1])
    print(max(set_sum_invalid) + min(set_sum_invalid))


if __name__ == "__main__":
    main()