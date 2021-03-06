""" Importing libraries to use in system.
Import random allows access to the random modules,
creates random number generation.
Hangman words are imported from file words.py
Hangman stages are imported from status.py
Import time represents time in code
Os module provides functions for creating
and removing directory.
"""

import os
import random
import time

from status import HANGMAN_STAGE
from words import computer_names

ATTEMPTS = "global"
DISPLAY = "global"
WORD = "global"
ALREADY_GUESSED = "global"
LENGTH = "global"
PLAY_GAME = "global"
ORIGINAL_WORD = "global"
MAX_ATTEMPTS = 5
USERNAME = None


def get_user_detail():
    """
    get user name and store it in the username
    """
    global USERNAME
    # Initial Steps to invite in the game:
    print("\nWelcome to Hangman game\n")
    USERNAME = input("Please enter your name: ")
    print("Hello " + USERNAME + "! Good Luck!" "The game is about to start")


def rules_help():
    """Displays rules to the user"""
    print(
        """ \n <------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
    The Hangman is a simple, WORD game
    where the goal is to find the missing words.
    The theme of the game is 'Computer'\n
    1. From the list of computer-words a random WORD is generated.
    2. You will be presented with a number of blank spaces/n
    3. You must enter one letter.
    4. You can have only 5 guesses to find out the secret WORD.
    5. You can only use characters from the latin alphabet.
    6. Use the keyboard to guess the letter. It is better to start with vowels.
    7. You wont be penalized for using symbol or number or for reusing the
    letters.
    \n <------------------------------------------------------------>\n"""
    )
    input("Press Enter to continue...")


# Initializing all the conditions required for the game:
def initialize_game():
    """Displays the parameters used in the game"""
    global ATTEMPTS
    global DISPLAY
    global WORD
    global ALREADY_GUESSED
    global LENGTH
    global PLAY_GAME
    global ORIGINAL_WORD
    global MAX_ATTEMPTS
    ATTEMPTS = 0
    WORD = random.choice(computer_names)
    ORIGINAL_WORD = WORD
    LENGTH = len(WORD)
    DISPLAY = "-" * LENGTH
    ALREADY_GUESSED = []
    PLAY_GAME = ""
    MAX_ATTEMPTS = 5
    get_user_detail()


# A loop to re-execute the game when the first round ends


def user_wants_to_play_again():
    """This function will be executed when the first round of the game ends"""
    global PLAY_GAME
    PLAY_GAME = input(
        "Do you want to play? y = yes, n = no, h = help \n").lower()
    while PLAY_GAME not in ["y", "n", "h"]:
        PLAY_GAME = input(
            "Do You want to play again? y = yes, n = no, h = help menu \n"
        )
    if PLAY_GAME == "h":
        rules_help()
        return False
    if PLAY_GAME == "y":
        os.system("clear")
        return True
    elif PLAY_GAME == "n":
        print("Thank you for Playing! We expect you back again!")
        exit()


def is_guess_included_in_word(guess):
    """This function checks if the guess entered by user is
    present in the word or not. If present, the guess will
    be displayed in the blank spaces.
    """
    global WORD, DISPLAY

    ALREADY_GUESSED.extend([guess])
    index = WORD.find(guess)
    # print(f"ALREADY_GUESSED: {ALREADY_GUESSED}")
    # print(f"WORD: {WORD}")

    if index < 0:
        return False
    # Loop as along as there as letters to replace
    while index >= 0:
        WORD = WORD[:index] + "_" + WORD[index + 1:]
        DISPLAY = DISPLAY[:index] + guess + DISPLAY[index + 1:]
        index = WORD.find(guess, index)
    return True


def increase_attempts():
    """This function is to count increased attempts"""

    global ATTEMPTS, MAX_ATTEMPTS
    ATTEMPTS += 1


def display_remaining_attemts():
    """Displays remaining attempts="""
    global MAX_ATTEMPTS, ATTEMPTS
    if ATTEMPTS >= MAX_ATTEMPTS:
        print("Sorry!! You have lost this game. You are hanged!!!\n")
        print("The WORD was:", ORIGINAL_WORD)
    elif ATTEMPTS < MAX_ATTEMPTS:
        print("You have", MAX_ATTEMPTS - ATTEMPTS, "attempts left")
    else:
        print("You have won this game!")
        print("Congratulations!! You have won this game. You are saved!!!\n")


def display_hangman_status():
    """Displays hangman status on screen"""

    global MAX_ATTEMPTS, ATTEMPTS

    print(HANGMAN_STAGE[ATTEMPTS-1])


def clear_screen():
    """This function to clear the screen and delay execution time"""
    time.sleep(2)
    os.system("clear")


def is_winner():
    """This function checks whether all the guesses entered by the user
    are actually present in original word. If all the guesses are correct,
    the player wins the game.
    """
    global WORD, LENGTH, ATTEMPTS, MAX_ATTEMPTS
    if WORD == "_" * LENGTH:
        print("Congrats! You have won this game!")
        return True
    elif ATTEMPTS != MAX_ATTEMPTS:
        return False


def play_game():
    """Play_game function is the core part of the game.
    This is responsible for initializing all the conditions
    required to guess, DISPLAY letters and formation of
    hangman structure
    """
    global ATTEMPTS
    global DISPLAY
    global WORD
    global ALREADY_GUESSED
    global MAX_ATTEMPTS

    while ATTEMPTS < MAX_ATTEMPTS:

        guess = input(
            "This is the Hangman WORD: " + DISPLAY + "\nEnter your guess: \n"
        ).strip()

        if len(guess.strip()) > 1 or not guess.isalpha():
            print("Input is Invalid, Try a letter\n")
        elif guess in ALREADY_GUESSED:
            print("Try another letter.\n")
        elif is_guess_included_in_word(guess):
            # print("iDebug-> is included")
            display_remaining_attemts()
            display_hangman_status()
            clear_screen()
        else:
            # print("Debug-> invalid choice made")
            increase_attempts()
            display_remaining_attemts()
            if ATTEMPTS <= MAX_ATTEMPTS:
                display_hangman_status()
            clear_screen()
        if is_winner():
            break


def init_game_engine():
    """
    This function intializes game again
    """
    initialize_game()
    print("Starting Game...Let's play...!")
    clear_screen()
    play_game()


if __name__ == "__main__":
    input("Press Enter to start the game")
    while True:
        if user_wants_to_play_again():
            init_game_engine()
