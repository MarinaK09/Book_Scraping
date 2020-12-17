import requests
from bs4 import BeautifulSoup
import time

url = 'http://books.toscrape.com/'

#def get_category(url_website)
links = []

response = requests.get(url)
if response.ok:
	soup = BeautifulSoup(response.text,'lxml')
	lis=soup.find('ul', {'class':'nav nav-list'}).findAll('ul')
	for li in lis:
		print(li)
		a = li.find('a')
		category = a.text
		a = a['href']
		a = a.replace('index.html','')
		links.append(a)
		print(category)
		#get_product_from_category(a, category)
	#print(len(links))

#for i in range(15):
	#url = 'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/'+