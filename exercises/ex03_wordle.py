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