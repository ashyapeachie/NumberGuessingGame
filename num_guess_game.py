# main game logic

import random

def get_difficulty():
    print("\nChoose difficulty:")
    print("1 - Easy (1-50, 10 attempts)")
    print("2 - Medium (1-100, 7 attempts)")
    print("3 - Hard (1-200, 5 attempts)") 

    while True: 
        try: 
            choice = int(input("Enter your choice (1, 2, or 3): "))

            if choice == 1:
                return 50, 10
            elif choice == 2:
                return 100, 7
            elif choice == 3:
                return 200, 5
            else:
                print("Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number")

def play_game():
    print("\n🎮 Welcome to Guess the Number!")

def main():
    play_game()

if __name__ == "__main__":
    main()
    #guess = None
    #this function generates a random int between 1 and 100

    #printed intro and prompt to guess the right # til correct to the user

    #while guess != number_to_guess:
        #try:
            #guess = int(input("Guess a number: "))
            #if guess < number_to_guess:
                #print("Too low!")
            #elif guess > number_to_guess:
                #print("Too high!")
            #else: 
                #print("You guess the correct number- YAY!")
        #except ValueError:
            #print("Please enter a valid number: ")
    #feedback is given to the user after each guess (too high, too low)
        #may add a "getting closer" feedback option

#guess_the_number()
#running the progrom(game)