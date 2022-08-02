import requests
from bs4 import BeautifulSoup

# Website that is examined and entered in order to extract data
url = "https://greenopolis.com/list-of-nouns/"

# Access requested to the website
res = requests.get(url)
content = res.text
soup = BeautifulSoup(content, 'html.parser')

# Bare HTML pulled from website and converted into a string
text = soup.find_all('ul')
strtext = str(text)

# String of HTML code sliced and separated based on <li> tags found within code
spltext = strtext.split('</li><li>')

# Unimportant code is stripped from the list
del spltext[0]
last = len(spltext) - 1
print("Items:", last)
del spltext[last]

# Cycle through every item and extract items with HTML tags still attached; dubbed "defects"
for i in spltext:
    if "<" in i:
        print(spltext.index(i))
        spltext.remove(i)
print(spltext)

# Check for any possible missed defective items
for i in spltext:
    if "<" in i:
        print(spltext.index(i))
        spltext.remove(i)
