# PersonalPyProjects

A collection of projects and demonstration of language proficiency.

Indludes: Various python programs —— hangman, webcrawler, grade calculator, password generator, number game

number_game.py -- {

  My first documented program (EST. 2020). Utilizing the random module, this input-based python program generates a random integer. Input "y" when prompted to play. You have three chances to guess the hidden number.

}

grade_calculator.py -- {

  One of my first programs (EST. 2020).  In school, I would recieve a score on an assignment, which was a number correct out of a total denominator. At the time, I wanted to know what the percentage grade would be; but more often than not, I would only recieve a fraction (correct/total). So I decided to create a function that takes an 2 integers, x (number correct) and y (total) —— and divides for a quotient. The remaining decimal is the percentage. The code converts the decimal into an array and takes the appropriate values from the tenths and hundreths place (now indexes in the array), returning a percentage and a Khan Academy link accordingly.

}

password_generator.py -- {

  Creates a strong, secure password from four strings of uppercase letters, lowercase letters, integers, and symbols. These strings are converted into lists. A random number is generated; determining how many items from each list are to be used. This variable is randomized each time to decrease similarity between generated passwords and to avoid predictablility. This variable is set as the range of for loops that pick random characters from each list x number of times. Each list is compiled into one list to create a secure password.

}

noun_webcrawler.py -- {

  Utilizing "requests" and "bs4" modules to extract data from HTML files, this program extracts a long list of words from an online website; i.e. a webcrawler. The program requests access to the URL and when granted, extracts raw HTML from the site. The site chosen contains a long list of nouns nested in list tags. HTML is converted into one long string, then split based on list tags. An array is created that resembles the structure:

[ "HTML code" , "desired word" , "desired word" , "desired word" , "desired word" , ... , "HTML code" ]

Unimportant content is deleted from the array —— (del spltext[0]), (del spltext[len(spltext) - 1]) —— leaving only words in the array. A for loop is used to remove any item remaining with a list tag; defects.

}

hangman.py -- {

  

}




