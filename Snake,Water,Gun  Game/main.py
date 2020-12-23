import random


def gameWin(comp, you):

    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False


print("Comp Turn: Snake(s),Water(w),Gun(g): ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"
you = input("Your Turn: Snake(s), Water(w), Gun(g)?: ")
a = gameWin(comp, you)

print(f"Comp choose {comp}")
print(f"You choose {you}")

if a == None:
    print("This is a TIE!")
elif a:
    print("You WIN!")
else:
    print("You LOSE!")
