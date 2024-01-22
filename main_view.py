# main_view.py
"""
Main view for the String Reverser application.

This module contains functions responsible for handling user interactions,
such as displaying welcome messages and managing the application loop.
"""
from reverser import reverse_string
from utils import messages
from utils.sound_controller import play_sound
from utils.utils import color_picker


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
    while True:
        input_string = input(messages.input_str)  # Use the imported message
        if input_string.lower() == messages.exit_input:
            print(messages.exit_message)
            break

        try:
            play_sound(messages.btn_click_path)  # Play sound
        except Exception as e:
            print(messages.sound_error.format(e))
            play_sound(messages.warning_path, is_warning=True)

        reversed_string = reverse_string(input_string)
        print(messages.reversed_str, color_picker(messages.yellow) + reversed_string + color_picker(messages.reset))
        print()


def welcome_interface():
    """
    Displays the welcome interface for the application.

    This function prints the welcome message and instructions for the user.
    It utilizes ANSI escape codes for coloring the text, which are obtained
    from the color_picker function.
    """
    print(color_picker(messages.blue) + messages.welcome_message + color_picker(messages.reset))
    print(color_picker(messages.blue) + messages.instruction_message + color_picker(messages.reset))
    print(color_picker(messages.blue) + messages.exit_instruction + color_picker(messages.reset))
