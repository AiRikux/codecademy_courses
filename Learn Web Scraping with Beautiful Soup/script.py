# learning how to do requests

## import python library that help you request webpage html from url
import requests
from bs4 import BeautifulSoup # import beautiful soup library

## GET request to the website
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

## get the content using .content
webpage = webpage_response.content
# use the library to get the content
soup = BeautifulSoup(webpage, "html.parser")

# print the <p> tag
print(soup.p)
# print the <p> tag but only their string
print(soup.p.string)