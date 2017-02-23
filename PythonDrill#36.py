#
# PYTHON:   2.7.13
#
# AUTHOR:   Annie Bowman
#
# PURPOSE:  Tech Academy Python Course Drill, Item #36 
#           Write a program demonstrating 13 basic Python concepts 
#


# 1. Assign an integer to a variable
# 2. Assign a string to a variable
# 5. Use each of these operators: +, -, *, /, +=, =, %
number = 47
words = "I am a string!"

print number + 3
print number - 5
print words * 3
print float(number) / 10
print number % 15

number += 53
print number



# 3. Assign a float to a variable
# 4. Use the print function w/ .format() to print out the variable
pi = 3.14159
print("The approximate value of PI is {}".format(pi))



# 6.a Use these logical operators: and, or
# 7. Use conditional statements: if, elif, else
# 8. Use a while loop
go = True
while go:
    troll = raw_input("You come across a troll in the forest - do you FIGHT him, PAY him or RUN? ").upper()
    if troll == "FIGHT":
        strong = raw_input("You seem pretty brave! Are you strong? (y/n) ").lower()
        smart = raw_input("Well, are you smart? (y/n) ").lower()
        if strong == "y" or smart == "y":
            print("Anyone who's strong OR smart can beat a troll - you win!")
            go = False
        else:
            print("You're not strong or smart? No wonder you chose to FIGHT a troll... you're dead!")
            go = False
    elif troll == "PAY":
        money = raw_input("Ok! Do you have any money? (y/n) ").lower()
        tdoll = raw_input("Is it in troll dollars? (y/n) ").lower()
        if money == "n":
            print("Well what did you think you would pay him with!? I'd tell you to try again, but you're dead!")
            go = False
        if money == "y" and tdoll == "y":
            print("Great! Pay him and be on your way!")
            go = False
        elif money == "y" and tdoll == "n":
            print("Sorry, trolls only take troll dollars - you're dead!")
            go = False
        else:
            print("Let's try this again....")
    elif troll == "RUN":
        print("You'd think trolls were slow, being that they're so big... but nope. You're dead!")
        go = False
    else:
        print("I didn't get that, pick either 'FIGHT', 'PAY' or 'RUN' please")
        


# 6.b Use these logical operators: not
# 9. Use a for loop
# 10. Create a list and iterate through it using a for loop to print each item on a new line
number = 3
numList = [2,4,6,8,10,12]
for num in numList:
    if number not in numList:
        print num


# 11. Create a tuple and iterate through it using a for loop to print each item on a new line
myInfo = ("Annie", "Bowman", "8/7/80", "female")
for facts in myInfo:
    print facts

# 12. Define a function that returns a string variable
# 13. Call the function you defined in 12 and print the result to the shell
def myFunction():
    name = raw_input("Please type your name: ").capitalize()
    return ("Hi, {}! How did I do on this drill?".format(name))

print myFunction()



