import random

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
    The theme of the game is 'Animals'\n
    1. From the list of animals a random word is generated.
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
    global attempts
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    attempts = 0
    display = '-' * length
    already_guessed = []
    play_game = ""             



        







