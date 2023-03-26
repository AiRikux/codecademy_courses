# learning how to do requests

# import python library that help you request webpage html from url
import requests
from bs4 import BeautifulSoup  # import beautiful soup library
import re  # import re for regex find

# GET request to the website
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

# get the content using .content
webpage = webpage_response.content
# use the library to get the content
soup = BeautifulSoup(webpage, "html.parser")

# print the <p> tag
print(soup.p)
# print the <p> tag but only their string
print(soup.p.string)

# we can get the children of the tag by using .children
for child in soup.div.children:
	print(child)

# find
turtle_links = soup.find_all("a")

# use re
soup.find_all(re.compile("h[1-9]"))

# use lists
print(soup.find_all(['h1', 'a', 'p']))

# attributes
print(soup.find_all(attrs={'class': 'banner', 'id': 'jumbotron'}))

# select with CSS Selector
prefix = "https://content.codecademy.com/courses/beautifulsoup/"

# get all links on home page
links = {}
# go through all of the a tags and get the links associated with them:
for a in turtle_links:
	links.append(prefix + a["href"])  # getting them into subpages links

# Define turtle_data:
turtle_data = []

# follow each link:
for link in links:
	webpage = requests.get(link)
	turtle = BeautifulSoup(webpage.content, "html.parser")
	# Add your code here:
	# Name
	# return as a list so we need to access the inside and get the string
	turtle_name = turtle.select(".name")[0].string
	turtle_data[turtle_name] = []


