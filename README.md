# eraseme1

## Hangman Game

A simple command-line implementation of the classic Hangman word guessing game.

### How to Play

Run the game with Python 3:

```bash
python3 hangman.py
```

or make it executable and run directly:

```bash
chmod +x hangman.py
./hangman.py
```

### Game Rules

- The game randomly selects a word from a predefined list
- You have 6 incorrect guesses before you lose
- Guess one letter at a time
- Try to guess the complete word before running out of attempts

### Features

- Visual hangman stages showing game progression
- Input validation (only accepts single letters, no duplicates)
- Win/lose conditions with appropriate messages