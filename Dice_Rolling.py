import random

print("This is a dice simulator")
x = "y"

while x == "y":
    number = random.randint(1, 6)

    if number == 1:
        print("_____________")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("_____________")
    if number == 2:
        print("_____________")
        print("|           |")
        print("|   0    0  |")
        print("|           |")
        print("_____________")
    if number == 3:
        print("_____________")
        print("|     0     |")
        print("|     0     |")
        print("|     0     |")
        print("_____________")
    if number == 4:
        print("_____________")
        print("| 0       0 |")
        print("|           |")
        print("| 0       0 |")
        print("_____________")
    if number == 5:
        print("_____________")
        print("| 0       0 |")
        print("|     0     |")
        print("| 0       0 |")
        print("_____________")
    if number == 6:
        print("_____________")
        print("| 0       0 |")
        print("| 0       0 |")
        print("| 0       0 |")
        print("_____________")
    x = input("Press y to roll again.\n")