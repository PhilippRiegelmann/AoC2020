def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            row = []
            for i in line.rstrip():
                row.append(i)
            input.append(row)
    return input


def main():
    print(read_file("C:/Users/Phili/Documents/Projects/AoC_2020/11/input.txt"))


if __name__ == "__main__":
    main()