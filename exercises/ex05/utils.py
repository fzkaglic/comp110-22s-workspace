"""EX05 - Function Skeletons and Implementations."""

__author__ = "730501608"


def only_evens(input: list[int]) -> list[int]:
    """Returns only the even numbers within the input list."""
    i: int = 0 
    even_numbers: list[int] = list()
    while i < len(input):
        if input[i] % 2 == 0:
            even_numbers.append(input[i])
        i = i + 1
    return even_numbers
