#get qoute from internet
#print the first qoute
#get user to press ENTER
#print another qoute

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

data = urlopen("https://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/#6463faa46c7a")
soup = BeautifulSoup(data, 'html.parser')

quotes = []
quotes2 = []
for p in soup.findAll('p'):
	quotes.append(p.text)


for q in quotes:
	if any(char.isdigit() for char in q) == True and q[0].isdigit() == True:
		quotes2.append(q)
	else:
		pass

print("Your 5 quotes of the day: \n")
for x in range(5):
	print(quotes2[random.randint(1, len(quotes2)-1)])

print("\n")
print("For more famous qoutes refresh the page.")
