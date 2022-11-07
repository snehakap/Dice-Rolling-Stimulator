import random
a="y"
a=input("Press y to roll the dice and n to discontinue: ")

while a=="y":
    x= random.randint(1,6)
    print(x)
    if x==1:
        print("-------")
        print("|     |")
        print("|  *  |")
        print("|     |")
        print("-------")
    if x==2:
        print("-------")
        print("|     |")
        print("| * * |")
        print("|     |")
        print("-------")
    if x==3:
        print("-------")
        print("|     |")
        print("|* * *|")
        print("|     |")
        print("-------")
    if x==4:
        print("-------")
        print("|*   *|")
        print("|     |")
        print("|*   *|")
        print("-------")
    if x==5:
        print("-------")
        print("|*   *|")
        print("|  *  |")
        print("|*   *|")
        print("-------")
    if x==6:
        print("-------")
        print("|* * *|")
        print("|     |")
        print("|* * *|")
        print("-------")
    a=input("To roll the dice again press y and to discontinue press n: ")