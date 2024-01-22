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
background_sound_thread = None
background_sound_playing = False


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


def _background_sound_loop(sound_path):
    global background_sound_playing
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(-1)  # Play the music indefinitely
    while background_sound_playing:
        pass
    pygame.mixer.music.stop()


def start_background_sound(sound_path):
    global background_sound_thread, background_sound_playing
    background_sound_playing = True
    if not pygame.mixer.music.get_busy():
        background_sound_thread = threading.Thread(target=_background_sound_loop, args=(sound_path,))
        background_sound_thread.start()


def stop_background_sound():
    global background_sound_playing
    background_sound_playing = False
    pygame.mixer.music.stop()


def toggle_background_sound(sound_path):
    global background_sound_playing
    if background_sound_playing:
        stop_background_sound()
    else:
        start_background_sound(sound_path)
