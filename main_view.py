# main_view.py
"""
Main view for the String Reverser application.

This module contains functions responsible for handling user interactions,
such as displaying welcome messages and managing the application loop.
"""

from reverser import reverse_string, is_palindrome
from utils.messages import (yellow, reversed_str, sound_error, btn_click_path, reset, blue, welcome_message,
                            instruction_message, exit_instruction, input_str, exit_input, exit_message,
                            exit_path,
                            exit_sleep_time, purple, teal, error_path, bar, green, background_path, mute_input,
                            sound_option, palindrome_str,
                            palindrome_path, palindrome_sleep_time)
from utils.sound_controller import play_sound, toggle_background_sound, start_background_sound, stop_background_sound
from utils.utils import color_picker, wait


def app_runner():
    """
    Runs the main application loop.

    This function manages the main loop of the application, where the user
    is prompted to enter strings to reverse. It handles user input, calls
    the string reversal function, and displays the reversed string. The loop
    continues until the user types 'exit'.

    The colors for the output text are set using ANSI escape codes obtained
    from the color_picker function.
    """
    # Start playing background sound
    start_background_sound(background_path)  # Ensure this is the correct path
    while True:
        input_string = input(color_picker(teal) + input_str + color_picker(reset))  # Use the imported message
        if input_string.lower() == exit_input:
            exit_app()
            break
        if input_string.lower() == mute_input:
            mute_background()
            continue
        if input_string.lower() not in [mute_input, exit_input]:
            if is_palindrome(input_string):
                print(color_picker(green) + palindrome_str + color_picker(reset))
                play_sound(palindrome_path)
                wait(palindrome_sleep_time)

        try:
            play_sound(btn_click_path)
        except Exception as e:
            print(sound_error.format(e))
            play_sound(error_path)
        reversed_string = reverse_string(input_string)
        print(color_picker(teal) + reversed_str + color_picker(reset),
              color_picker(yellow) + reversed_string + color_picker(reset))
        print()


def mute_background():
    toggle_background_sound(background_path)  # Add your background music path


def exit_app():
    play_sound(exit_path)
    print(color_picker(purple) + exit_message + color_picker(reset))
    stop_background_sound()
    wait(exit_sleep_time)


def welcome_interface():
    """
    Displays the welcome interface for the application.

    This function prints the welcome message and instructions for the user.
    It utilizes ANSI escape codes for coloring the text, which are obtained
    from the color_picker function.
    """
    print()
    print(color_picker(green) + bar + color_picker(reset))
    print(color_picker(blue) + welcome_message + color_picker(reset))
    print(color_picker(blue) + instruction_message + color_picker(reset))
    print(color_picker(blue) + sound_option + color_picker(reset))
    print(color_picker(blue) + exit_instruction + color_picker(reset))
    print(color_picker(green) + bar + color_picker(reset))
    print()
