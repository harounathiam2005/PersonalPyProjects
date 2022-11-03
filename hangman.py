import random

# Pseudocode for word retrieval system located in noun_webcrawler.py
from noun_webcrawler import *

# Player select settings
mode = input(print("Select difficulty: Enter '1' for easy mode; Enter '2' for hard mode."))
print(mode)

# Using module 'random', select a random word from "spltext" depending on mode chosen
if int(mode) == 1:
    print("Items:", len(spltext))
    print(spltext)
    select = random.randrange(1, 97)
    print("From", 97, "items...")
    print("Item", select, "selected")
elif int(mode) == 2:
    print("Items:", len(spltext))
    print(spltext)
    select = random.randrange(98, len(spltext))
    print("From", len(spltext), "items...")
    print("Item", select, "selected")
else:
    print("Please enter '1' or '2'.")

# Place selected word into a variable and capitalize
# noinspection PyUnboundLocalVariable
lword = spltext[select]
str(lword)
word = lword.upper()

# Get number of letters, make a list of empty spaces representing each letter.
print(len(word), "characters")
blanks = list('_' * len(word))
print((" ".join(blanks)))


# Victory visual
def stickmanv():
    print("_\|/^")
    print(" (_oo /")
    print("/-|--/")
    print("\ |")
    print("  /--i")
    print(" /   L")
    print(" L")


lives = 6
guessblanks = []


# Stickman life visual
def stickman():
    if lives == 6:
        print("   O   ")
        print("-- | --")
        print("   |   ")
        print("  / \  ")
    elif lives == 5:
        print("   O   ")
        print("-- |   ")
        print("   |   ")
        print("  / \  ")
    elif lives == 4:
        print("   O   ")
        print("   |   ")
        print("   |   ")
        print("  / \  ")
    elif lives == 3:
        print("   O   ")
        print("   |   ")
        print("   |   ")
        print("  /    ")
    elif lives == 2:
        print("   O   ")
        print("   |   ")
        print("   |   ")
        print("       ")
    elif lives == 1:
        print("   O   ")
        print("       ")
        print("       ")
        print("       ")


stickman()

# Game start
while True:

    # Check if word is complete. If yes, end game.
    if '_' not in blanks:
        print("Congratulations!")
        stickmanv()
        stickman()
        print(word)
        break
    elif lives == 0:
        print("You lose!")
        print(word)
        break
    else:

        # Get player input, place input inside variable.
        guess = input("Take a guess!").upper()

        # If guess in part of selected word...
        if guess in word:

            # Check for errors.
            if guess in blanks:
                print("You already guessed that!")
                lives -= 1
                print("Lives: ", lives)
                if guess not in guessblanks:
                    guessblanks.append(guess)
                    print(guessblanks)
                stickman()

            elif guess == "":
                print("Please enter a letter.")
            elif len(guess) != 1:
                print("Guess one letter.")

            # If no errors, add guessed letter to blanks.
            else:
                print("Letter correct!", guess)
                wordlist = list(word)
                for i, j in enumerate(word):
                    if j == guess:
                        blanks[i] = j
            print(" ".join(blanks))
            print(guessblanks)
            stickman()
            print("")

        # If guess is not in word, restart loop.
        elif guess not in word:

            # Error check
            if len(guess) != 1:
                print("Guess one letter.")
            print("Incorrect!", guess)
            if guess not in guessblanks:
                guessblanks.append(guess)
                print(guessblanks)
            else:
                print("Already guessed!")
                print(guessblanks)
            print(' '.join(blanks))
            lives -= 1
            print("Lives: ", lives)
            stickman()
            print("")
            
