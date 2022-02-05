"""EX03 - Wordle."""

__author__ = "730501608"

        
def contains_char(search_word: str, single_character: str) -> bool:
    """Scan to see if the second parameter is contained in the first."""
    assert len(single_character) == 1
    search_test: bool = False
    i: int = 0
    while search_test is not True and i < int(len(search_word)):
        if single_character == search_word[i]:
            search_test = True
        else:
            search_test = False
        i = i + 1
    if search_test is True:
        return True
    else:
        return False


# contains_char is a function that tests whether the single character
# of the second parameter is found within the search word of the first parameter
# if so, the function will return True
# if not, the function will return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis that shows the relations between indices of guess and secret."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji: str = ""
    while i < int(len(guess)) and int(len(secret)):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji


# green boxes indicate that the index of the guess matches that of the secret
# yellow boxes indicate that the index of the guess is found at a different index of the secret
# white boxes indicate that the index of the guess is not found within the secret


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while int(len(guess)) != expected_length:
        guess = input(f"That was not {expected_length} chars! Try again: ")
    return guess


# input_guess is a function that will prompt the user for a guess that matches
# expected_length, and it will continue to do so until the user gets it right


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 1
    victory: bool = False
    while victory is not True and turn_number <= 6:
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret))
        emojis: str = emojified(guess, secret)
        print(emojis)
        if guess == secret:
            victory = True
        else:
            victory = False
            turn_number += 1
    if victory is True:
        print(f"You won in {turn_number}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")

        
# the previously defined functions (contains_char, emojified, and input_guess)
# serve as the building blocks of the main function that governs the wordle game


if __name__ == "__main__":
    main()
