input = []

with open("C:/Users/Phili/Documents/Projects/AoC_2020/3/input.txt", "r") as f:
    for line in f:
        input.append(line.rstrip())


def count_number_items(List, item, Right, Down):
    counter = 0
    n = 0
    for i in range(0, len(List), Down):
        if n > 30:
            n -= 31
        if List[i][n] == item:
            counter += 1
        n += Right
    return counter


Answer1 = count_number_items(input, "#", 3, 1)
Answer2 = (
    count_number_items(input, "#", 1, 1)
    * count_number_items(input, "#", 3, 1)
    * count_number_items(input, "#", 5, 1)
    * count_number_items(input, "#", 7, 1)
    * count_number_items(input, "#", 1, 2)
)

print(Answer1)
print(Answer2)
