# main.py
"""
Main entry point for the String Reverser application.

This script initializes the application and runs the main loop,
allowing users to input strings and receive their reversed versions.
"""
from main_view import welcome_interface, app_runner


def main():
    """
    Main function to run the string reverser application.

    This function runs an interactive loop that allows the user
    to input strings and get their reversed versions. The user
    can exit the loop and the program by typing 'exit'.
    """
    welcome_interface()

    app_runner()


if __name__ == "__main__":
    main()
