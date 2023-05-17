#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for roman_numeral in roman_string:
        if roman_map[roman_numeral] > roman_map[roman_string[result]]:
            result += roman_map[roman_numeral] - 2 * roman_map[roman_string[result]]
        else:
            result += roman_map[roman_numeral]
        return result
