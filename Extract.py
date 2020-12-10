import requests
from bs4 import BeautifulSoup
import time

infos = []
header = []
star = 0
links = []
#get_all_categories()

def get_product_from_category(url_category):
	response = requests.get(url_category)
	if response.ok:
		soup = BeautifulSoup(response.text,'lxml')
		h3s = soup.findAll('h3')
		for h3 in h3s:
			a = h3.find('a')
			link = a['href']
			#links.append('http://books.toscrape.com/catalogue/category/books/christian_43/' + link)
			get_infos_product(url_category + link)


def get_infos_product(url_product):
	response = requests.get(url_product)
	if response.ok:
		soup = BeautifulSoup(response.text,'lxml')
		trs = soup.findAll('tr')
		title = soup.find('div', {'class':'col-sm-6 product_main'}).find('h1')
		for tr in trs:
			td = tr.find('td')
			infos.append(td.text)
		universal_product_code = infos[0]
		price_excluding_tax = infos[2]
		price_including_tax = infos[3]
		number_available = infos[5]

		descripts = soup.find('article', {'class':'product_page'}).findAll('p')
		product_description = descripts[3]

		lis=soup.find('ul', {'class':'breadcrumb'}).findAll('li')
		for li in lis:
			a = li.find('a')
			header.append(a)
		category = header[2]

		#product_page_url = soup.find('tr',{'class':'product_page'})
		

		stars = soup.find('div',{'col-sm-6 product_main'}).findAll('p') #review_rating
		p = stars[2]
		star = p['class']

		image_url = soup.find('div', {'class':'item active'}).find('img')

		print('product_page_url: ' + url_product + '\n')
		print('universal_product_code: ' + universal_product_code + '\n')
		print('Title: ' + title.text + '\n')
		print('price_including_tax: ' + price_including_tax + '\n')
		print('price_excluding_tax: ' + price_excluding_tax + '\n')
		print('number_available: ' + number_available + '\n')
		print('product_description: ' + product_description.text + '\n')
		print('category: ' + category.text + '\n')
		print('review_rating: ' + star[1] + '\n')
		print('image_url: ' + 'http://books.toscrape.com/' + image_url['src'] + '\n')

if __name__ == "__main__":
    #get_infos_product("http://books.toscrape.com/catalogue/unqualified-how-god-uses-broken-people-to-do-big-things_873/index.html")
    get_product_from_category("http://books.toscrape.com/catalogue/category/books/christian_43/")



	






	