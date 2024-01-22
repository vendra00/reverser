# sound_controller.py
"""
Sound controller for the String Reverser application.

This module handles the sound playback functionality using Pygame. It includes
a function to play a sound file, which is used for user interaction feedback.
"""

import os
import threading

import pygame

from utils.messages import reset, red, sound_not_found, warning_path
from utils.utils import color_picker

# Initialize Pygame mixer
pygame.mixer.init()


def _play_sound_thread(sound_path):
    """
    Internal function to play a sound file in a separate thread.
    """
    sound = pygame.mixer.Sound(sound_path)
    sound.play()


def play_sound(sound_path, is_warning=False):
    """
    Play a sound file using Pygame in a separate thread.

    Parameters:
    sound_path (str): The file path to the sound file to be played.
    is_warning (bool): Flag to indicate if this is a warning sound.
    """
    if os.path.exists(sound_path):
        # Create a thread to play the sound
        thread = threading.Thread(target=_play_sound_thread, args=(sound_path,))
        thread.start()
    else:
        if not is_warning:
            print(color_picker(red) + sound_not_found.format(sound_path) + color_picker(reset))
            # Now call play_sound for warning with is_warning set to True
            play_sound(warning_path, is_warning=True)
