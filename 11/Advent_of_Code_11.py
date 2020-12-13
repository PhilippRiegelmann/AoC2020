def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            row = []
            for i in line.rstrip():
                row.append(i)
            input.append(row)
    return input


def check_if_surrounding_empty(input, row, column):
    surrounding_empty = True
    seats_surrounding = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for pos in seats_surrounding:
        new_row = row + pos[0]
        new_column = column + pos[1]
        if (
            new_row >= 0
            and new_row < len(input)
            and new_column >= 0
            and new_column < len(input[0])
        ):
            if input[new_row][new_column] == "#":
                surrounding_empty = False
                break
    return surrounding_empty


def check_if_less_than_four_surrounding_occupied(input, row, column):
    surronding_occupied = 0
    surrounding_empty = True
    seats_surrounding = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for pos in seats_surrounding:
        new_row = row + pos[0]
        new_column = column + pos[1]
        if (
            new_row >= 0
            and new_row < len(input)
            and new_column >= 0
            and new_column < len(input[0])
        ):
            if input[new_row][new_column] == "#":
                surronding_occupied += 1
                if surronding_occupied > 3:
                    surrounding_empty = False
                    break
    return surrounding_empty


def check_if_changing_neccesarry(input, row, column):
    changing_neccesarry = False
    if input[row][column] == "L":
        if check_if_surrounding_empty(input, row, column):
            changing_neccesarry = True
    elif input[row][column] == "#":
        if not check_if_less_than_four_surrounding_occupied(input, row, column):
            changing_neccesarry = True
    return changing_neccesarry


def change_status(input, row, column):
    if input[row][column] == "L":
        input[row][column] = "#"
    else:
        input[row][column] = "L"
    return input[row][column]


def process(input):
    changing_list = []
    for i in range(len(input)):
        for n in range(len(input[i])):
            if check_if_changing_neccesarry(input, i, n):
                changing_list.append([i, n])
    if len(changing_list) > 0:
        for i in changing_list:
            input[i[0]][i[1]] = change_status(input, i[0], i[1])
    return input, len(changing_list)


def count_occupied(input):
    num_occupied = 0
    for i in range(len(input)):
        for n in range(len(input[i])):
            if input[i][n] == "#":
                num_occupied += 1
    return num_occupied


def main():
    seatplan = read_file("C:/Users/Phili/Documents/Projects/AoC_2020/11/input.txt")
    x = 1
    while x > 0:
        seatplan, x = process(seatplan)
    print(count_occupied(seatplan))


if __name__ == "__main__":
    main()