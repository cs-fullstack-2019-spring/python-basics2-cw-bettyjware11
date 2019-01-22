import random

def main():
    #Problem1()
    #Problem2()
    #Problem3()
    Problem4()
#Problem 1:
#Create a random number. Print the number.
#Hint:
#import random
#randomNumber = random.randint(0,9)

def Problem1():
    for x in range (10):
        print (random.randint(0,9))

#Problem 2:
#We will keep having this problem until EVERYONE gets it right without help
#Create a function that has a loop that quits with ‘q’.
# #If the user doesn't enter 'q', ask them to input another string.
def Problem2():
    while (True):
        userInput1 = input("Enter password")
        userInput2 = input("Re-enter password")
        if userInput2 == userInput1:
            print("Access granted")
        elif (userInput2 != userInput1):
            print("Enter another")
        elif userInput2: "q"
        break

#Problem 3:
#Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
#Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.

def Problem3():
    varNum1 = input("Enter positive integer")
    varNum2 = input("Enter positive integer")
    for x in range(0, int(varNum2)):
        print(x)
        if input == 0:
            break

#Problem 4:
#Create a function that creates a random number. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.
def Problem4():
    secretNum = random.randint(0,9)
    while (True):
        guessNum1 = int(input("Enter guess \n"))
        if (guessNum1 == secretNum):
            print("Correct")
            break
        elif (guessNum1 > secretNum):
            print("Guess lower")
        elif (guessNum1 < secretNum):
            print("Guess higher")



















if __name__ == '__main__':
    main()