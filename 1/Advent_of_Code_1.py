numbers = []

with open("C:/Users/Phili/Documents/Projects/AoC_2020/1/input.txt", "r") as f:
    for line in f:
        numbers.append(int(line.rstrip()))
Answer = 0
for i in range(len(numbers)):
    for n in range(len(numbers)):
        if i != n:
            for k in range(len(numbers)):
                if k != n and k != i:
                    if numbers[i] + numbers[n] + numbers[k] == 2020:
                        Answer = numbers[i] * numbers[n] * numbers[k]
                        print(numbers[i])
                        print(numbers[n])
                        print(numbers[k])
                        break
            if Answer != 0:
                break
    if Answer != 0:
        break


print(Answer)