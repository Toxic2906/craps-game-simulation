import random

def craps():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    print(f"You rolled {die1} + {die2} = {total}")

    if total in (7, 11):
        print("You win")
    elif total in (2, 3, 12):
        print("You lose")
    else:
        point = total
        print("Point is", point)

        while True:
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)

            total = die1 + die2

            print(f"You rolled {die1} + {die2} = {total}")

            if total == point:
                print("You win")
                break
            elif total == 7:
                print("You lose")
                break

craps()