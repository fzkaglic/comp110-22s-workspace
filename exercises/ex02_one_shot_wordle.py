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

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji: str = ""

while i < int(len(secret_word)):
    if guess[i] == secret_word[i]:
        emoji = emoji + GREEN_BOX
    else:
        emoji = emoji + WHITE_BOX
    i = i + 1

print(emoji)