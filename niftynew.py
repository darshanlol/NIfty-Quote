import requests
import html5lib
page = requests.get("http://www.moneycontrol.com/indian-indices/nifty-50-9.html")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'b_20'})
name = name_box.get_text()
price = soup.find(attrs={'class' : 'FL gr_35'})
pricequote = price.text.strip()
import csv
from datetime import datetime
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, pricequote, datetime.now()])




	
