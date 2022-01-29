"""EX02 - One Shot Wordle."""

__author__ = "730501608"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")

while int(len(guess)) != int(len(secret_word)):
    guess: str = input("That was not 6 letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
