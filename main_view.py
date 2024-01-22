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
    Initialize and start the main application loop.

    This function is responsible for initiating the application. It starts by playing
    the background sound and then calls the main application loop function. This is the
    entry point for running the String Reverser application.

    The background sound is started using a predefined path, ensuring the sound
    is set up correctly before entering the main loop of the application.
    """
    # Start playing background sound
    start_background_sound(background_path)  # Ensure this is the correct path
    app_runner_loop()


def app_runner_loop():
    """
    Run the main loop of the application.

    This function manages the core loop where the application handles user input.
    It processes commands for muting background sound, exiting the application,
    checking for palindromes, and reversing strings. The loop continues until
    the user decides to exit.

    Inside the loop, it listens for user input and calls appropriate functions based
    on the input. This includes handling internal commands like muting/unmuting and exiting,
    as well as triggering string reversal and palindrome checking processes.
    """
    while True:
        input_string = input(color_picker(teal) + input_str + color_picker(reset))  # Use the imported message
        if input_string.lower() == exit_input:
            exit_app()
            break
        if input_string.lower() == mute_input:
            mute_background()
            continue
        check_palindrome(input_string)
        try:
            play_sound(btn_click_path)
        except Exception as e:
            print(sound_error.format(e))
            play_sound(error_path)
        start_reversing(input_string)


def start_reversing(input_string):
    """
    Handle the process of reversing a given string.

    This function takes an input string, reverses it using the reverse_string
    function, and then prints the reversed string. The output is color-formatted
    for better visibility.

    Parameters:
    input_string (str): The string to be reversed.
    """
    reversed_string = reverse_string(input_string)
    print(color_picker(teal) + reversed_str + color_picker(reset),
          color_picker(yellow) + reversed_string + color_picker(reset))
    print()


def check_palindrome(input_string):
    """
    Check and handle if the given string is a palindrome.

    This function determines if the input string is a palindrome, excluding
    internal commands like 'mute' and 'exit'. If the string is a palindrome,
    it triggers the palindrome notification process.

    Parameters:
    input_string (str): The string to be checked for palindrome.
    """
    if input_string.lower() not in [mute_input, exit_input]:
        if is_palindrome(input_string):
            palindrome()


def palindrome():
    """
    Notify the user that the input string is a palindrome.

    This function is called when an input string is identified as a palindrome.
    It prints a notification message and plays a specific sound, followed by a
    brief pause to allow the user to acknowledge the notification.
    """
    print(color_picker(green) + palindrome_str + color_picker(reset))
    play_sound(palindrome_path)
    wait(palindrome_sleep_time)


def mute_background():
    """
    Toggle the background sound on or off.

    This function is responsible for muting or unmuting the background sound
    of the application. It uses the toggle_background_sound function from the
    sound controller to manage the background sound state.
    """
    toggle_background_sound(background_path)  # Add your background music path


def exit_app():
    """
    Handle the application exit process.

    This function is called when the user decides to exit the application. It
    plays an exit sound, displays an exit message, and stops the background sound.
    There is a brief wait before the application completely shuts down, ensuring
    that all exit processes are completed smoothly.
    """
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
