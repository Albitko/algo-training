t_room, t_cond = map(int, input().split(" "))
working_mode = input()

match working_mode:
    case "freeze":
        if t_room <= t_cond:
            print(t_room)
        else:
            print(t_cond)
    case "heat":
        if t_room >= t_cond:
            print(t_room)
        else:
            print(t_cond)
    case "auto":
        print(t_cond) 
    case "fan":
        print(t_room)