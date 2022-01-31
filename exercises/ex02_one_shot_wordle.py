"""EX02 - One Shot Wordle."""

__author__ = "730501608"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ") 
# the user is prompted for input

while int(len(guess)) != int(len(secret_word)):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")
# if the user inputs a word with the incorrect number of letters
# the while loop will continue prompting the user for input until
# they enter a word with the correct letter length

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji: str = ""

while i < int(len(secret_word)):
    if guess[i] == secret_word[i]:
        emoji = emoji + GREEN_BOX
    else:
        contains_character: bool = False
        alt_i: int = 0
        while contains_character is not True and alt_i < int(len(secret_word)):
            if secret_word[alt_i] == guess[i]:
                contains_character = True
            alt_i = alt_i + 1
        if contains_character is True:
            emoji = emoji + YELLOW_BOX
        else: 
            emoji = emoji + WHITE_BOX
    i = i + 1

# the while loop tests whether the index of the guess
# match the index of the secret word
# a green box will print if the index of the guess
# matches the corresponding index of the secret word
# a yellow box will print if the index of the guess
# appears in the secret word at a different index
# a white box will print if the index of the guess
# does not appear at all within the secret word

print(emoji)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
