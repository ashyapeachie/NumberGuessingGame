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

    max_num, attempts_left = get_difficulty()
    number_to_guess = random.randint(1, max_num)
    
    guess = None
    attempt_count = 0

    #print statement

    while guess != number_to_guess and attempts_left > 0:
        try:  

def main():
    play_game()

