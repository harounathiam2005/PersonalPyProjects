# A program that generates a strong, secure password from an assortment of letters, numbers and symbols.

import random
from random import shuffle

# string of numbers, letters, and characters from which certain characters will be pulled.
caps = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
lowr = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
nums = "1 2 3 4 5 6 7 8 9 0"
symb = "! @ # $ % &"

# Characters in string are split into individual items; string converted to list.
capsstr = caps.split()
lowrstr = lowr.split()
numsstr = nums.split()
symbstr = symb.split()

#print(capsstr)
#print(lowrstr)
#print(numsstr)
#print(symbstr)

capslist = []
lowrlist = []
numslist = []
symblist = []

# Generate integers to be used as amount of each characters used in password.
capsrand = random.randrange(6, 8)
lowrrand = random.randrange(6, 8)
numsrand = random.randrange(6, 10)
symbrand = random.randrange(4, 6)

#print("caps:", capsrand)
#print("lowr:", lowrrand)
#print("nums:", numsrand)
#print("symb:", symbrand)

# A random number is generated, determining which character in each list is pulled. Process repeated 6 times. Characters
# pulled are placed in blank list called "capslist".
for i in range(capsrand):
    x = random.randrange(0, 26)
    capsx = capsstr[x]
    capslist.append(capsx)
#print(capslist)

for i in range(lowrrand):
    y = random.randrange(0, 26)
    lowry = lowrstr[y]
    lowrlist.append(lowry)
#print(lowrlist)

for i in range(numsrand):
    z = random.randrange(0, 10)
    numsz = numsstr[z]
    numslist.append(numsz)
#print(numslist)

for i in range(symbrand):
    w = random.randrange(0, 6)
    symbw = symbstr[w]
    symblist.append(symbw)
#print(symblist)

# Combine and shuffle lists. Take items from list and places into a complete string.
full = capslist + lowrlist + numslist + symblist
#print(full)
shuffle(full)
#print(full)

fullstr = ""
for item in full:
    fullstr += item
print("Password:", fullstr)
print("char length:", len(fullstr))
