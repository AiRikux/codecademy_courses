import seaborn as sns# codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1 Explore the webpage displayed in the browser. What elements could be useful to scrape here? Which elements do we not want to scrape?

# 2 GET request to the website
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

# 3 create bs4 object

# get the content using .content
webpage = webpage_response.content
# use the library to get the content
soup = BeautifulSoup(webpage, "html.parser")

# 4 How are ratings distributed?
# get all ratings to a list
ratings = []
# skip first value as it is a heading
for rate in soup.select(".Rating")[1:]:
	ratings.append(float(rate.get_text()))

plt.hist(ratings).show()

