from types import SimpleNamespace


def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            input.append(line.strip())
    return input


def upperhalf(num1, num2):
    newnum1 = (num1 + num2 + 1) / 2
    newnum2 = num2
    return newnum1, newnum2


def lowerhalf(num1, num2):
    newnum1 = num1
    newnum2 = (num1 + num2 - 1) / 2
    return newnum1, newnum2


def findrow(binary):
    num1 = 0
    num2 = 127
    for i in range(7):
        if binary[i] == "B":
            num1, num2 = upperhalf(num1, num2)
        if binary[i] == "F":
            num1, num2 = lowerhalf(num1, num2)
    return int(num1)


def findcolumn(binary):
    num1 = 0
    num2 = 7
    for i in range(7, 10):
        if binary[i] == "R":
            num1, num2 = upperhalf(num1, num2)
        if binary[i] == "L":
            num1, num2 = lowerhalf(num1, num2)
    return int(num1)


def calcSeatID(binary):
    row = findrow(binary)
    column = findcolumn(binary)
    SeatID = row * 8 + column
    return SeatID


def findhighestnumber(input):
    highestnumber = 0
    for i in range(len(input)):
        if input[i] > highestnumber:
            highestnumber = input[i]
    return highestnumber


def findlowestnumber(input):
    lowestnumber = 1000
    for i in range(len(input)):
        if input[i] < lowestnumber:
            lowestnumber = input[i]
    return lowestnumber


def findmissingID(input):
    missingID = "Alle IDs vorhanden"
    for i in range(findlowestnumber(input), findhighestnumber(input) + 1):
        if i not in input:
            missingID = i
    return missingID


def main():
    SeatID = []
    input = read_file("C:/Users/Phili/Documents/Projects/Advent of Code/5/input.txt")
    for i in range(len(input)):
        SeatID.append(calcSeatID(input[i]))
    print(findhighestnumber(SeatID))
    print(findmissingID(SeatID))


if __name__ == "__main__":
    main()