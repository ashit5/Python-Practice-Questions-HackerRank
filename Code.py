#Initialize an empty list. Read an integer N representing the number of commands.
#For each of the N commands, perform the specified list operation (insert, append, remove, sort, pop, reverse, or print) in the given order. 
#Print the list only when the command is print.


if __name__ == '__main__':

    N = int(input())      # number of commands
    l = []                # empty list

    for i in range(N):    # loop N times
        command = input()        # read one command
        parts = command.split()  # split command into words

        if parts[0] == "insert":
            l.insert(int(parts[1]), int(parts[2]))

        elif parts[0] == "append":
            l.append(int(parts[1]))

        elif parts[0] == "remove":
            l.remove(int(parts[1]))

        elif parts[0] == "sort":
            l.sort()

        elif parts[0] == "pop":
            l.pop()

        elif parts[0] == "reverse":
            l.reverse()

        elif parts[0] == "print":
            print(l)
