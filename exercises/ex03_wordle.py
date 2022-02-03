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
