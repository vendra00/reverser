# utils.py
"""
Utility functions for the String Reverser application.

This module provides utility functions such as color_picker which are used
across the application for various purposes like styling terminal output.
"""
import time

from utils.messages import blue, blue_code, yellow, yellow_code, red_code, red, green, green_code, purple_code, \
    purple, reset, reset_code, teal, teal_code


def color_picker(color_name):
    """
    Provides ANSI escape codes for a specified text color.

    This function takes a color name as input and returns the corresponding
    ANSI escape code. If the color name is not recognized, it defaults to
    the reset (default) color code.

    Parameters:
    color_name (str): Name of the color. Accepted values are 'blue', 'reset', and 'yellow'.

    Returns:
    str: ANSI escape code for the specified color.
    """
    colors = {
        blue: blue_code,
        yellow: yellow_code,
        red: red_code,
        green: green_code,
        purple: purple_code,
        teal: teal_code,
        reset: reset_code
    }
    return colors.get(color_name, colors[reset])


def wait(time_period):
    """
    Pauses the execution of the program for a specified duration.

    This function uses the time.sleep() method to halt the program's execution.
    It can be used to create a delay for a certain number of seconds, which is
    useful in scenarios where a pause in processing is required, such as waiting
    for a sound to finish playing or implementing a countdown.

    Parameters:
    time_period (float or int): The duration of time, in seconds, for which the
                                program execution should be paused.
    """
    time.sleep(time_period)
