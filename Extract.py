import requests
from bs4 import BeautifulSoup
import urllib.request
import os

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

		try:
			os.mkdir(category)
		except:
			print('file creation failed')

		category_file = category
		file_name = os.path.join(category_file, category + '.csv')
		f = open(file_name, 'w')
		ligneEntete = ";".join(entetes) + '\n'
		f.write(ligneEntete)					   
		f.close()	
		h3s = soup.findAll('h3')
		for h3 in h3s:
			a = h3.find('a')
			link = a['href']
			get_infos_product(url_category + link, file_name)

		next_page = soup.find('li',{'class':'next'})
		
		while next_page is not None:
			a = next_page.find('a')
			url_category_next_page = url_category + '/' + a['href']
			response = requests.get(url_category_next_page)
			if response.ok:
				soup = BeautifulSoup(response.text,'lxml')
				h3s = soup.findAll('h3')
				for h3 in h3s:
					a = h3.find('a')
					link = a['href']
					get_infos_product(url_category + link, file_name)
				next_page = soup.find('li',{'class':'next'})

			
	

def get_infos_product(url_product, file_name):

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
			image_url = image_url['src']
			image_url = image_url.replace('../../','')
			image_url = 'http://books.toscrape.com/' + image_url
		   

		f = open(file_name, 'a')
		valeurs = [url_product,
			       universal_product_code,
			       title.text,
			       price_including_tax,
			       price_excluding_tax,
			       number_available,
			       category.text,
			       star[1],
			       image_url,
			       product_description.text]
		
		ligne = ";".join(valeurs) + '\n'
		f.write(ligne)
		f.close()

		


if __name__ == "__main__":

    get_category('http://books.toscrape.com/')



	






	