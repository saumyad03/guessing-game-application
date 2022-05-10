import random

#Input Validator
def validate(n):
    #ensures input is an integers
    try:
        n = int(n)
    except:
        return False
    #ensures integer is within range
    if (n > 100 or n < 1):
        return False
    #if valid, the following is returned
    return True

#Main Game Function
def guessingGame():
    num = random.randint(1, 100)
    print("A random number between 1 and 100 inclusve has been chosen. You have 10 guesses.")
    guesses = 10
    while guesses > 0:
        #data validation (uses validator function)
        guessedNum = input("Guess a number: ")
        while (validate(guessedNum) == False):
            guessedNum = input("This is an invalid guess. Try again: ")
        #assessing user's guess
        guessedNum = int(guessedNum)
        if guessedNum > num:
            print(str(guessedNum), "is too high")
            guesses-=1
            print("Remaining Guesses:", guesses,"\n")
        elif guessedNum < num:
            print(str(guessedNum), "is too low")
            guesses-=1
            print("Remaining Guesses:", guesses,"\n")
        else:
            print("You won! The number was", str(num),"\n")
            break
    if (guesses < 1):
        print("You lost! The number was", str(num),"\n")

while True:
    guessingGame()