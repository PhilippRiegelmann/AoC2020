def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            input.append(line.rstrip())
    return input


def in_service(input_string):
    list_in_service = []
    for BusID in input_string.split(","):
        if BusID != "x":
            list_in_service.append(int(BusID))
    return list_in_service


def in_service_and_offset(input_string):
    list_in_service = []
    input_string_list = input_string.split(",")
    for i in range(len(input_string_list)):
        ID_and_offset = []
        if input_string_list[i] != "x":
            list_in_service.append([int(input_string_list[i]), i])
    return list_in_service


def min_minutes_to_wait(time, busses_on_service):
    time_to_wait = 100000000000000
    bus_ID_to_take = 0
    for i in busses_on_service:
        time_to_arive = i - (time % i)
        if time_to_arive < time_to_wait:
            time_to_wait = time_to_arive
            bus_ID_to_take = i
    return time_to_wait, bus_ID_to_take


def main():
    input = read_file("C:/Users/Phili/Documents/Projects/AoC_2020/13/input.txt")
    earliest_timestamp = int(input[0])
    available_buses = in_service(input[1])
    time_to_wait, bus_to_take = min_minutes_to_wait(earliest_timestamp, available_buses)
    print(time_to_wait * bus_to_take)
    print("")
    print(in_service_and_offset(input[1]))


if __name__ == "__main__":
    main()