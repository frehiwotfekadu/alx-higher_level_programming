#!/usr/bin/python3
# 12-roman_to_int.py


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    if roman_string is None or type(roman_string) != str:
        return 0
    ns = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [ns[x] for x in roman_string] + [0]
    rep = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            rep += numbers[i]
        else:
            rep -= numbers[i]

    return rep
