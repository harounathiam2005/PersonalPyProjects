import requests
from bs4 import BeautifulSoup
import random

# Pseudocode for word retrieval system located in webcrawler.py file
url = "https://greenopolis.com/list-of-nouns/"
res = requests.get(url)
content = res.text
soup = BeautifulSoup(content, 'html.parser')
text = soup.find_all('ul')
strtext = str(text)
spltext = strtext.split('</li><li>')
del spltext[0]
last = len(spltext) - 1
del spltext[last]
for i in spltext:
    if "<" "/" in i:
        spltext.remove(i)
for i in spltext:
    if "/" in i:
        spltext.remove(i)

# Using random module, select a word randomly from "spltext"
print("Items:", len(spltext))
print(spltext)
select = random.randrange(1, len(spltext))
print("From", len(spltext), "items...")
print("Item", select, "selected")

# Place selected word into a variable and capitalize
lword = spltext[select]
str(lword)
word = lword.upper()

# Get number of letters using len(), make a list of empty spaces representing each letter.
print(len(word), "characters")
blanks = list('_' * len(word))
print((" ".join(blanks)))


def stickman():
    print("_\|/^")
    print(" (_oo /")
    print("/-|--/")
    print("\ |")
    print("  /--i")
    print(" /   L")
    print(" L")


while True:

    # Check if word is complete. If yes, end game.
    if '_' not in blanks:
        print("Congratulations!")
        stickman()
        print(word)
        break
    else:

        # Get player input, place input inside variable.
        lguess = input("Take a guess!")
        guess = lguess.upper()

        # If guess in part of selected word...
        if guess in word:

            # Check for errors.
            if guess in blanks:
                print("You already guessed that!")
            elif guess == "":
                print("Please enter a letter.")
            elif len(guess) != 1:
                print("Guess one letter.")

            # If no errors, add guessed letter to blanks.
            else:
                print("Letter correct!", guess)
                wordlist = list(word)
                # print(wordlist)
                for i, j in enumerate(word):
                    if j == guess:
                        blanks[i] = j
            print(" ".join(blanks))
            print("")

        # If guess is not in word, restart loop.
        elif guess not in word:
            if len(guess) != 1:
                print("Guess one letter.")
            print("Incorrect!", guess)
            print(' '.join(blanks))
            print("")
