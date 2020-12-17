import requests
from bs4 import BeautifulSoup
import time

def get_category(url_website):
	links = []

	response = requests.get(url_website)
	if response.ok:
		soup = BeautifulSoup(response.text,'lxml')
		lis=soup.find('ul', {'class':'nav nav-list'}).findAll('li')

		for li in lis:
			a = li.find('a')
			a = a['href']
			a = a.replace('index.html','')
			links.append(a)

		for i in range(1, len(links)):
			link = links[i]
			get_product_from_category(url_website + link)

def get_product_from_category(url_category):

	response = requests.get(url_category)
	if response.ok:
		soup = BeautifulSoup(response.text,'lxml')
		category = soup.find('div', {'class':'page-header action'}).find('h1')
		category = category.text

		entetes = [u'product_page_url',
				   u'universal_product_code',
				   u'title',
				   u'price_including_tax',
				   u'price_excluding_tax',
				   u'number_available',
				   u'category',
				   u'review_rating',
				   u'image_url',
				   u'product_description',]

		file_name = category + '.csv'
		f = open(file_name, 'w')
		ligneEntete = ";".join(entetes) + '\n'
		f.write(ligneEntete)					   
		f.close()	
		h3s = soup.findAll('h3')
		for h3 in h3s:
			a = h3.find('a')
			link = a['href']
			#links.append('http://books.toscrape.com/catalogue/category/books/christian_43/' + link)
			get_infos_product(url_category + link, file_name)
			
	


def get_infos_product(url_product, file_name):
	#with open('Christian.csv', 'w') as outf:
		#outf.write('product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating,image_url \n')

		response = requests.get(url_product)
		if response.ok:
			soup = BeautifulSoup(response.text,'lxml')
			infos = []
			header = []
			star = 0
			links = []
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


			stars = soup.find('div',{'col-sm-6 product_main'}).findAll('p') #review_rating
			p = stars[2]
			star = p['class']

			image_url = soup.find('div', {'class':'item active'}).find('img')

			#print('product_page_url: ' + url_product + '\n')
			#print('universal_product_code: ' + universal_product_code + '\n')
			#print('title: ' + title.text + '\n')
			#print('price_including_tax: ' + price_including_tax + '\n')
			#print('price_excluding_tax: ' + price_excluding_tax + '\n')
			#print('number_available: ' + number_available + '\n')
			#print('product_description: ' + product_description.text + '\n')
			#print('category: ' + category.text + '\n')
			#print('review_rating: ' + star[1] + '\n')
			#print('image_url: ' + 'http://books.toscrape.com/' + image_url['src'] + '\n')
		   

		f = open(file_name, 'a')
		valeurs = [url_product,
			           universal_product_code,
			           title.text,
			           price_including_tax,
			           price_excluding_tax,
			           number_available,
			           category.text,
			           star[1],
			           'http://books.toscrape.com/' + image_url['src'],
			           product_description.text,]
		
		ligne = ";".join(valeurs) + '\n'
		f.write(ligne)
		f.close()


		



if __name__ == "__main__":

    get_category('http://books.toscrape.com/')



	






	