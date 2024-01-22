# reverser.py
"""
String reverser module.

This module contains the logic for reversing a given string. It uses recursion
to reverse the characters of the string.
"""
import sys

from utils.messages import animation_sleep_time, total_width, green, complete_path, reversing_str, reset, \
    reversing_str_complete
from utils.sound_controller import play_sound
from utils.utils import wait, color_picker


def reverse_string(s, animation_str='', first_call=True):
    """
    Reverse a given string with an animated display using recursion.

    This function manages the recursive process of string reversal. It handles
    the initial setup for the animation, delegates the animation tasks, and
    ultimately returns the reversed string.

    Parameters:
    s (str): The string to be reversed.
    animation_str (str): The accumulated part of the reversed string during the animation.
    first_call (bool): Flag indicating if this is the first call of the recursion.

    Returns:
    str: The fully reversed string.
    """
    first_call = check_first_call(first_call)

    if len(s) <= 1:
        reverser_animation_ui(animation_str, s)  # Reversal Animation
        clear_after_animation_complete()  # Clear the animation and print completion message
        return s
    else:
        next_animation_str = reversing_with_animation(animation_str, s)  # Reversal Animation
        return s[-1] + reverse_string(s[:-1], next_animation_str, first_call)


def reversing_with_animation(animation_str, s):
    """
    Perform the animated string reversal at each recursive step.

    This function updates the animation string with the next character from the
    end of the input string, centering it for display.

    Parameters:
    animation_str (str): The accumulated part of the reversed string in the animation.
    s (str): The remaining part of the string to be reversed.

    Returns:
    str: The updated animation string including the next character.
    """
    next_animation_str = animation_str + s[-1]
    centered_str = next_animation_str
    padding = (total_width - len(centered_str)) // 2
    sys.stdout.write('\r' + ' ' * padding + centered_str)  # Center the string
    sys.stdout.flush()
    wait(animation_sleep_time)
    return next_animation_str


def check_first_call(first_call):
    """
    Check and handle the first call in the recursive string reversal.

    This function prints the initial message for the reversal animation if it's
    the first call in the recursion.

    Parameters:
    first_call (bool): Flag indicating if this is the first call of the recursion.

    Returns:
    bool: Updated state of the first_call flag.
    """
    if first_call:
        print(color_picker(green) + reversing_str + color_picker(reset))
        first_call = False
    return first_call


def clear_after_animation_complete():
    """
    Clear the console line after the reversal animation is complete and play completion sound.

    This function overwrites the console line used for the animation with spaces
    and prints the completion message. It also plays a sound indicating the
    completion of the reversal process.
    """
    sys.stdout.write('\r' + ' ' * total_width + '\r')
    sys.stdout.flush()
    print(color_picker(green) + reversing_str_complete + color_picker(reset))
    play_sound(complete_path)


def reverser_animation_ui(animation_str, s):
    """
    Update the console UI for the reversal animation.

    This function is responsible for the UI aspect of the animation,
    displaying the current state of the reversed string.

    Parameters:
    animation_str (str): The accumulated part of the reversed string in the animation.
    s (str): The current character being added to the reversed string.
    """
    centered_str = animation_str + s
    padding = (total_width - len(centered_str)) // 2
    sys.stdout.write('\r' + ' ' * padding + centered_str)  # Center the string
    sys.stdout.flush()
    wait(animation_sleep_time)


def is_palindrome(s):
    """
    Check if a given string is a palindrome.

    This function compares the string to its reverse and determines if it is a palindrome.
    It ignores spaces, punctuation, and capitalization.

    Parameters:
    s (str): The string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    clean_str = ''.join(char.lower() for char in s if char.isalnum())
    return clean_str == clean_str[::-1]
