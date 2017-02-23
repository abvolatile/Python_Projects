#
# PYTHON:   2.7.13
#
# AUTHOR:   Annie M Bowman
#
# PURPOSE:  Guess My Number Game 
#           Just for fun :) 
#


def startGame():
    ask = True
    while ask:
        name = raw_input("Please enter your name: ").capitalize()
        if name != "":
            print("\nHello, {}! Here's the deal:".format(name))
            print("I will choose a whole number between 1 and 50, and you have to guess what it is!")
            check = True
            while check:
                go = raw_input("Are you ready to start? (y/n): ".lower())
                if go == "y":
                    print("Awesome! I'm thinking of a number.... OK, got it!")
                    guessNum(name)
                elif go == "n":
                    print("Well, you're not much fun.")
                    exit()
                else:
                    print("Go ahead and type a 'y' for YES or an 'n' for NO...")
            ask = False
        else:
            print("\nJust type any name and press enter. Doesn't even have to be yours.")


def guessNum(name):
    from random import randint
    myNum = randint(1,50)
    print(myNum)
    guessing = True
    while guessing:
        try: #this all works unless input is not a number, so...
            guess = int(raw_input("\nMake your guess now, {}: ".format(name)))
            if guess == myNum:
                print("\nOMGeeeeee, you guessed it!! Nice work, {}!".format(name))
                newGuess(name)
                guessing = False
            elif guess < myNum and guess > 0:
                print("\nNope! Try something a bit higher next time")
            elif guess > myNum and guess < 51:
                print("\nThat's not it! Pssst, it's lower than that...")
            else:
                print("Guess a number between 1 and 50, please!")
        except ValueError: #if input is not a number, this is how to handle it
          print("Is that even a number? Guess a number between 1 and 50, please!")
        
 

def newGuess(name):
    ask = True
    while ask:
        again = raw_input("\nWould you like to try again, {}? (y/n): ".format(name))
        if again == "y":
            print("Great, here we go - I'm thinking of another number.... OK, got it!")
            guessNum(name)
        elif again == "n":
            print("Ok, fine. Whatever...")
            ask = False
            exit()
        else:
            print("Just type a 'y' for YES or a 'n' for NO and hit enter...")
            



if __name__ == "__main__":
    startGame()
