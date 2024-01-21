# sound_controller.py
"""
Sound controller for the String Reverser application.

This module handles the sound playback functionality using Pygame. It includes
a function to play a sound file, which is used for user interaction feedback.
"""

import os
import pygame
import threading

# Initialize Pygame mixer
pygame.mixer.init()


def _play_sound_thread(sound_path):
    """
    Internal function to play a sound file in a separate thread.
    """
    sound = pygame.mixer.Sound(sound_path)
    sound.play()


def play_sound(sound_path):
    """
    Play a sound file using Pygame in a separate thread.

    This function checks if the sound file exists at the given path and plays it
    in a separate thread. It allows the main program to continue running while
    the sound is playing.

    Parameters:
    sound_path (str): The file path to the sound file to be played.
                      This should be a valid path to a sound file supported by Pygame (e.g., .wav, .mp3).
    """
    if os.path.exists(sound_path):
        # Create a thread to play the sound
        thread = threading.Thread(target=_play_sound_thread, args=(sound_path,))
        thread.start()
    else:
        print(f"Warning: Sound file not found at {sound_path}")
        play_sound("files/warning.wav")
