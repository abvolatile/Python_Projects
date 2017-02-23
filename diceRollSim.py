# 
# PYTHON:   2.7.13
#
# AUTHOR:   Annie M Bowman
#
# PURPOSE:  Random Dice Roll Generator
#           Just for fun :)
#


def rollDie():
    print "Let's roll!"
    from random import randint
    roll = randint(1,6)
    print("\nYou've rolled a {}!".format(roll))
    rollAgain()


def rollAgain():
    ask = True
    while ask:
        again = raw_input("\nWould you like to roll again? (y/n): ")
        if again == "y":
            print("Great, here we go...")
            rollDie()
        elif again == "n":
            print("Ok, fine. Don't then.")
            ask = False
            exit()
        else:
            print("So... just type a 'y' for YES or an 'n' for NO and hit enter...")
            



if __name__ == "__main__":
    rollDie()
