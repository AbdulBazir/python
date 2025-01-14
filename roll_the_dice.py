import random

def roll_dice():
    dice = (1,2,3,4,5,6)
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    print(f"({die1},{die2})")

def main():
    while True:
        user = input("Do You Want To roll the Dice (y/n): ").lower()
        if user=="y":
            roll_dice()
        elif user=="n":
            print("thank you see you later")
            break
        else:
            print("invalid choice")
    return 0

main()
