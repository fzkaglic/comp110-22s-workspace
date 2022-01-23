"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730501608"

five_character_word: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character: ")
print("Enter a 5-character word: ")
print("Enter a single character: ")
print("Searching for " + single_character + " in " + five_character_word)

if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")

frequency: int = 0
