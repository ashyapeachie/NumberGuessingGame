# creation of file for game
# skills practiced: random, input, if-else statements, looops

import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    #this function generates a random int between 1 and 100

    #printed intro and prompt to guess the right # til correct to the user

    while guess != number_to_guess:
        try:
            guess = int(input("Guess a number: "))
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else: 
                print("You guess the correct number- YAY!")
        except ValueError:
            print("Please enter a valid number: ")
    #feedback is given to the user after each guess (too high, too low)
        #may add a "getting closer" feedback option

guess_the_number()
#running the progrom(game)