# imports
from random import randint


def printBoard(list):
    print(*list[0], *list[1], *list[2], sep="|")
    print("------ ")
    print(*list[3], *list[4], *list[5], sep="|")
    print("------ ")
    print(*list[6], *list[7], *list[8], sep="|")


def checkWin(list, x):
    if list[0] == x and list[1] == x and list[2] == x:
        return True
    if list[3] == x and list[4] == x and list[5] == x:
        return True
    if list[6] == x and list[7] == x and list[8] == x:
        return True
    if list[0] == x and list[3] == x and list[6] == x:
        return True
    if list[1] == x and list[4] == x and list[7] == x:
        return True
    if list[2] == x and list[5] == x and list[8] == x:
        return True
    if list[0] == x and list[4] == x and list[8] == x:
        return True
    if list[2] == x and list[4] == x and list[6] == x:
        return True
    return False


def roboMove(list):
    choices = []
    for i in range(0, 8):
        if list[i] != "x" and list[i] != "o":
            choices.append(i)
    if len(choices) == 0:
        return True
        print("Tie")
    else:
        pick = randint(0, len(choices)-1)
        list[choices[pick]] = "o"
        return False


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Spots are numbered: ")
printBoard(list)
list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win = False
while(not win):
    printBoard(list)
    if (checkWin(list, "x")):
        print("You won")
        win = True
    elif (checkWin(list, "o")):
        print("Your lost")
        win = True
    else:
        x = int(input("A number:"))
        if list[x-1] == "x" or list[x-1] == "o":
            print("That spot has been taken")
        else:
            list[x-1] = "x"
            win = roboMove(list)

# print(list[0], "|", list[1], "|", list[2])
# print("------")
# print(list[3], list[4], list[5])
# print("------")
# print(list[6], list[7], list[8])
