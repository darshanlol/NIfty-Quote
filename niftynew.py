#this script might not work anymore


import requests
import html5lib
page = requests.get("http://www.moneycontrol.com/indian-indices/nifty-50-9.html")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'b_20'})
name = name_box.get_text()
print name
price = soup.find(attrs={'class' : 'FL r_35'})
pricequote = price.text
print pricequote
points = soup.find(attrs={'class': 'FL r_20 PT10 MT3'})
point = points.text
print point
percentages = soup.find(attrs={'class': 'FL r_15 PT10 MT3 PL5'})
percentage = percentages.text
print percentage
import csv
from datetime import datetime
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, pricequote, point, percentage, datetime.now()])




