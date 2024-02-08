import pandas as pd

# read avocado.csv
df = pd.read_csv("avocado.csv")

# get average of daily price
# avg_price = sum(df['AveragePrice'])/len(df) not this one
avg_price = df['AveragePrice'].mean()

# get median average daily price
med_price = df['AveragePrice'].median()

print(med_price)

# answering questions
"""
What does avg_price mean? 
It is a shorten term of average price connected with an underscore

Why are the mean and the median different?
Mean is the total of all the numbers divided by the number of data while median is the number in the 50th percentile

When would you report the median instead of the mean?
When you would try to get the middle number
"""