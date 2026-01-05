#!/usr/bin/env python3
"""
A simple command-line implementation of the Hangman game.
"""

import random


# Hangman visual stages
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Word list for the game
WORD_LIST = [
    "python", "hangman", "programming", "computer", "keyboard",
    "developer", "algorithm", "function", "variable", "terminal",
    "software", "hardware", "database", "network", "internet"
]

# Maximum number of incorrect guesses allowed
MAX_ATTEMPTS = 6


def get_random_word():
    """Select a random word from the word list."""
    return random.choice(WORD_LIST).upper()


def display_game_state(word, guessed_letters, incorrect_guesses):
    """Display the current state of the game."""
    print("\n" + HANGMAN_STAGES[len(incorrect_guesses)])
    
    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print(f"Word: {display_word}")
    print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses)) if incorrect_guesses else 'None'}")
    print(f"Remaining attempts: {MAX_ATTEMPTS - len(incorrect_guesses)}")


def get_guess(guessed_letters):
    """Get a valid letter guess from the user."""
    while True:
        guess = input("\nEnter a letter: ").upper().strip()
        
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def play_hangman():
    """Main game loop for hangman."""
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = []
    
    print("=" * 50)
    print("Welcome to Hangman!")
    print("=" * 50)
    print(f"\nI'm thinking of a word with {len(word)} letters.")
    
    while True:
        display_game_state(word, guessed_letters, incorrect_guesses)
        
        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print(f"Congratulations! You won! The word was: {word}")
            print("=" * 50)
            break
        
        # Check for lose condition
        if len(incorrect_guesses) >= MAX_ATTEMPTS:
            print("\n" + HANGMAN_STAGES[min(len(incorrect_guesses), len(HANGMAN_STAGES) - 1)])
            print("=" * 50)
            print(f"Game Over! You lost. The word was: {word}")
            print("=" * 50)
            break
        
        # Get user guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses.append(guess)


def main():
    """Main function to run the game with replay option."""
    while True:
        play_hangman()
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Hangman! Goodbye!")
            break


if __name__ == "__main__":
    main()
