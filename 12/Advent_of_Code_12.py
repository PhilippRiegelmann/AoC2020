def read_file(txt):
    input = []
    with open(txt, "r") as f:
        for line in f:
            action = []
            action.append(line.rstrip()[0])
            action.append(int(line.rstrip()[1:]))
            input.append(action)
    return input


def change_view(actual_view, turnangle):
    if actual_view == "E":
        actual_angle = 0
    elif actual_view == "S":
        actual_angle = 90
    elif actual_view == "W":
        actual_angle = 180
    elif actual_view == "N":
        actual_angle = 270
    new_angle = actual_angle + turnangle
    if new_angle >= 360:
        new_angle -= 360
    elif new_angle < 0:
        new_angle += 360
    if new_angle == 0:
        new_view = "E"
    elif new_angle == 90:
        new_view = "S"
    elif new_angle == 180:
        new_view = "W"
    elif new_angle == 270:
        new_view = "N"
    return new_view


def change_view_b(angle, Pos_NS_Waypoint, Pos_EW_Waypoint):

    if angle == -270 or angle == 90:
        new_Pos_NS_Waypoint = -Pos_EW_Waypoint
        new_Pos_EW_Waypoint = Pos_NS_Waypoint
    elif angle == -180 or angle == 180:
        new_Pos_NS_Waypoint = -Pos_NS_Waypoint
        new_Pos_EW_Waypoint = -Pos_EW_Waypoint
    elif angle == 270 or angle == -90:
        new_Pos_NS_Waypoint = Pos_EW_Waypoint
        new_Pos_EW_Waypoint = -Pos_NS_Waypoint
    return new_Pos_NS_Waypoint, new_Pos_EW_Waypoint


def run_action_a(action, View, NS, EW):
    if action[0] == "N":
        NS += action[1]
    elif action[0] == "S":
        NS -= action[1]
    elif action[0] == "E":
        EW += action[1]
    elif action[0] == "W":
        EW -= action[1]
    elif action[0] == "L":
        View = change_view(View, -action[1])
    elif action[0] == "R":
        View = change_view(View, action[1])
    elif action[0] == "F":
        View, NS, EW = run_action_a([View, action[1]], View, NS, EW)
    return View, NS, EW


def run_action_b(action, Pos_NS_Boat, Pos_EW_Boat, Pos_NS_Waypoint, Pos_EW_Waypoint):
    if action[0] == "N":
        Pos_NS_Waypoint += action[1]
    elif action[0] == "S":
        Pos_NS_Waypoint -= action[1]
    elif action[0] == "E":
        Pos_EW_Waypoint += action[1]
    elif action[0] == "W":
        Pos_EW_Waypoint -= action[1]
    elif action[0] == "L":
        Pos_NS_Waypoint, Pos_EW_Waypoint = change_view_b(
            -action[1], Pos_NS_Waypoint, Pos_EW_Waypoint
        )
    elif action[0] == "R":
        Pos_NS_Waypoint, Pos_EW_Waypoint = change_view_b(
            action[1], Pos_NS_Waypoint, Pos_EW_Waypoint
        )
    elif action[0] == "F":
        Pos_NS_Boat += Pos_NS_Waypoint * action[1]
        Pos_EW_Boat += Pos_EW_Waypoint * action[1]

    return Pos_NS_Boat, Pos_EW_Boat, Pos_NS_Waypoint, Pos_EW_Waypoint


def main():
    list_of_actions = read_file(
        "C:/Users/Phili/Documents/Projects/AoC_2020/12/input.txt"
    )
    NS = 0
    EW = 0
    View = "E"
    for i in list_of_actions:
        View, NS, EW = run_action_a(i, View, NS, EW)

    print(abs(NS) + abs(EW))

    Pos_NS_Boat = 0
    Pos_EW_Boat = 0
    Pos_NS_Waypoint = 1
    Pos_EW_Waypoint = 10

    for i in list_of_actions:
        Pos_NS_Boat, Pos_EW_Boat, Pos_NS_Waypoint, Pos_EW_Waypoint = run_action_b(
            i, Pos_NS_Boat, Pos_EW_Boat, Pos_NS_Waypoint, Pos_EW_Waypoint
        )

    print(abs(Pos_NS_Boat) + abs(Pos_EW_Boat))


if __name__ == "__main__":
    main()