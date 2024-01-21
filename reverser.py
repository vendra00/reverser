# reverser.py
"""
String reverser module.

This module contains the logic for reversing a given string. It uses recursion
to reverse the characters of the string.
"""


def reverse_string(s):
    """
    Reverse a given string.

    This function takes a string as input and returns a new string
    which is the reverse of the input string. The function uses
    recursion to reverse the string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Base case: if the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest of the string and append the first character
    return reverse_string(s[1:]) + s[0]
