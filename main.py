from manager import Manager


if __name__ == '__main__':
    manager = Manager()

    while True:
        cmd = input(">>> ").split(" ")

        if cmd[0] == "exit":
            break
        else:
            if len(cmd) > 1:
                manager.command(cmd[0], cmd[1])
            else:
                manager.command(cmd[0])
