# utils.py
"""
Utility functions for the String Reverser application.

This module provides utility functions such as color_picker which are used
across the application for various purposes like styling terminal output.
"""
from utils.messages import blue, blue_code, yellow, yellow_code, red_code, red, green, green_code, purple_code, \
    purple, reset, reset_code


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
        reset: reset_code
    }
    return colors.get(color_name, colors[reset])
