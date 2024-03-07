# Simple Python program for a number guessing game

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!\n")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0

    while True:
        try:
            user_guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Too low. Try again!\n")
            else:
                print("Too high. Try again!\n")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()
