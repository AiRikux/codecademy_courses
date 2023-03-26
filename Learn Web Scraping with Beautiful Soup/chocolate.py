import seaborn as sns # codecademylib3_seaborn
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

plt.hist(ratings)
# plt.show()

# 5 Which chocolatier makes the best chocolate?
# get Company values
companies = []
# skip first value as it is a heading
for comp in soup.select(".Company")[1:]:
	companies.append(comp.get_text())
# create dataframe with companies and ratings only
df = pd.DataFrame(list(zip(companies, ratings)), columns=["Company", "Rating"])
# groupby company to see average
df.groupby("Company").mean().nlargest(10, 'Rating')

# 6 Is more cacao better?
# get CocoaPercent values
cocoa_percent = []
# skip first value as it is a heading
for cocoa in soup.select(".CocoaPercent")[1:]:
	cocoa_percent.append(float(cocoa.get_text()[:-1]))
# add column to dataframe
df["CocoaPercentage"] = cocoa_percent

plt.clf()
plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
# plt.show()

# More Questions
# Where are the best cocoa beans grown? Which countries produce the highest-rated bars?
