import random

def choose_word():
    words = ["hangman", "python", "programming", "challenge", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman_game():
    print("Welcome to Hangman!")

    word_to_guess = choose_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"\nWord: {current_display}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"Incorrect guess! {max_attempts - attempts} attempts remaining.")
        else:
            print("Correct guess!")

        if set(word_to_guess) == guessed_letters:
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            break

    if set(word_to_guess) != guessed_letters:
        print(f"\nSorry, you ran out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman_game()
