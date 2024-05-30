# PersonalPyProjects

A collection of projects demonstrating language proficiency.

Indludes: Various python programs —— hangman, webcrawler, grade calculator, password generator, number game

number_game.py -- {

  My first documented program (EST. 2020). Utilizing `random` module, this input-based python program generates a random integer. Input "y" when prompted to play. You have three chances to guess the hidden number.

}

grade_calculator.py -- {

One of my first programs (EST. 2020)

 Created a function that takes 2 integers, `x` (number correct) and `y` (total) —— and divides for a quotient. The remaining decimal is the percentage. The code converts the decimal into an array and takes the appropriate values from the tenths and hundreths place (now items in the array), returning a percentage and a Khan Academy link accordingly.

}

password_generator.py -- {

  Utilizing the `random` module, creates a strong, (not cryptographically secure, for this use `secrets` module) password from four strings of uppercase letters, lowercase letters, integers, and symbols. These strings are converted into lists. A random number is generated; determining how many items from each list are to be used. This variable is randomized each time to decrease similarity between generated passwords and to avoid predictablility. This variable is set as the range of for loops that pick random characters from each list `x` number of times. Each list is compiled into one list to create a secure password.

}

noun_webcrawler.py -- {

  Utilizing `requests` and `bs4` modules to extract data from HTML files, this program extracts a long list of words from an online website, i.e. a webcrawler. The program requests access to the URL and when granted, extracts raw HTML from the site. The site chosen contains a long list of nouns nested in list tags. HTML is converted into one long string, then `.split()` based on list tags. A list is created that resembles the structure:

`[ (HTML code) , (desired word) , (desired word) , (desired word) , (desired word) , ... , (HTML code) ]`

Unimportant content is deleted from the array —— `del spltext[0]`, `del spltext[len(spltext) - 1]` —— leaving only desired nouns. Loop through array to remove any item remaining with a list tags.

}

hangman.py -- {

  Works in conjunction with noun_webcrawler.py to create a full terminal-based hangman game. Utilizes web-fetching capabilities of noun_webcrawler.py to host a list of words to choose from as a basis for the game. Difficulty parameter; 1 == easy mode (shorter, more common words selected), 2 == hard mode (Full list of 11109 non-defective words to choose from). Code randomly chooses a word from array of words (using random module), converts it into string, then into a series of blank spaces; "_" times the number of letters in the selected word (`"_" * len(word)`). A `lives` variable is called that determines how many chances you get (6) before losing. This decrements by one every incorrect guess. Game begins with a check to see if _'s are still present in the word. If so, program continues. Else, game end w/ victory message. If player input `guess` is in word, run through a series of conditionals to check for invalid arguments (more than one letter, no letter). If input is valid, replace all instances of letter in blanks with `guess`.

Example: `word` = TREE | `guess` = E | Display: _ _ E E

If all chances are depleted before word is completed; i.e. `lives` = 0, game end w/ lose message. 

}
