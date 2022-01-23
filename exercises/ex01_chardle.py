"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730501608"

five_character_word: str = input("Enter a 5-character word: ")

if int(len(five_character_word)) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")

if int(len(single_character)) != 1:
    print("Error: Character must be a single character.")
    exit()

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

frequency = int(five_character_word.count(single_character))

if frequency == 0:
    print("No instances of " + single_character + " found in " + five_character_word)
else: 
    if frequency == 1:
        print("1 instance of " + single_character + " found in " + five_character_word)
    if frequency == 2:
        print("2 instances of " + single_character + " found in " + five_character_word)
    if frequency == 3:
        print("3 instances of " + single_character + " found in " + five_character_word)
    if frequency == 4:
        print("4 instances of " + single_character + " found in " + five_character_word)
    if frequency == 5:
        print("5 instances of " + single_character + " found in " + five_character_word)