import random
from words import computer_names

ATTEMPTS

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Good Luck!" "The game is about to start")


def rules_help():
    """ Displays rules to the user
    """
    rules = ''' \n <------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
    The Hangman is a simple, word game
    where the goal is to find the missing words.
    The theme of the game is 'Computer'\n
    1. From the list of computer-words a random word is generated.
    2. You will be presented with a number of blank spaces/n
    3. You must enter one letter.
    4. You can have only 6 guesses to find out the secret word.
    5. You can only use characters from the latin alphabet.
    6. Use the keyboard to guess the letter. It is better to start with vowels.
    7. You wont be penalized for using symbol or number or for reusing the
    letters.
    \n <------------------------------------------------------------>\n'''
    return rules


play_help = input("Do You want help? y = yes, n = no \n")
if play_help == "y":
    play_rules = rules_help()
    print(play_rules)
else:
    print("Starting Game....!\n Let's play...!")


def main():
    global ATTEMPTS
    global display
    global word
    global already_guessed
    global length
    global play_game
    global original_word
    ATTEMPTS = 0  
    word = random.choice(computer_names)
    original_word = word
    length = len(word)
    display = '-' * length
    already_guessed = []
    play_game = "" 


# A loop to re-execute the game when the first round ends


def game_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:


def hangman():
    global ATTEMPTS
    global display
    global word
    global already_guessed
    global play_game
    max_ATTEMPTS = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Input is Invalid, Try a letter\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
    # Loop as along as there as letters to replace
        while index >= 0:
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            index = word.find(guess, index)

            print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        ATTEMPTS += 1

        if ATTEMPTS == 1:

            print("   ___ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    " _|_\n")
            print("Oops!!Wrong guess. " + str(max_ATTEMPTS - ATTEMPTS) + " guesses remaining\n")

        elif ATTEMPTS == 2:
           
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Oops!!Wrong guess. " + str(max_ATTEMPTS - ATTEMPTS) + " guesses remaining\n")

        elif ATTEMPTS == 3:
           
           print("   ___ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "_|_\n")
           print("Oops!!Wrong guess. " + str(max_ATTEMPTS - ATTEMPTS) + " guesses remaining\n")

        elif ATTEMPTS == 4:
            
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "_|_\n")
            print("Oops!!Wrong guess. " + str(max_ATTEMPTS - ATTEMPTS) + " last guess remaining\n")

        elif ATTEMPTS == 5:
           
            print("   ___ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "_|_\n")
            print("Sorry!! You have lost this game. You are hanged!!!\n")
            # print the correct word
            print ("The word was:",original_word)
            game_loop()

    if word == '_' * length:
        print("Congrats! You have won this game!")
        game_loop()
    elif ATTEMPTS != max_ATTEMPTS:
        hangman()

main()

hangman()