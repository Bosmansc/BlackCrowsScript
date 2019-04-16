## track the sales price of a set of skis on an online website

# import libraries
import  urllib.request as url
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import csv
import os

# specify the url
ski_page = 'https://www.snowcountry.nl/black-crows-atris-47323.html'

# query the website and return the html to the variable ‘page’
html = url.urlopen(ski_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html, 'html.parser')

# Take out the <div> of name and get its value
price_box = soup.find('p', attrs={'class': 'special-price'})

# Find the prices in the html
prices = soup.find_all("span", class_="price")
sales_price = prices[1].text.replace('€','').strip()
original_price = prices[2].text.replace('€','').strip()

# Set the prices in a dataframe
ski_data = [sales_price, original_price]


ski_df = pd.DataFrame( columns = ['sales_price', 'original_price'] )
ski_df.loc[datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")] = ski_data


print(ski_df)


## write to csv
filename = r'ski_sales_price.csv'
# if file does not exist write header 
if not os.path.isfile(filename):
   ski_df.to_csv(filename, quoting = csv.QUOTE_NONE, sep='\t')
else: # else it exists so append without writing the header
   ski_df.to_csv(filename, mode='a', header=False, quoting = csv.QUOTE_NONE, sep='\t')






