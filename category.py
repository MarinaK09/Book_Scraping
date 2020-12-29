import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import shutil

try:
	os.mkdir('category')
except:
	print('file creation failed')



category_file = 'category'
images_file = 'category_images'


try:
	os.mkdir(os.path.join(category_file, images_file))
	#open(category_file + '_images')
	path = os.path.dirname(os.path.abspath(images_file))
	os.chdir(path)
	urllib.request.urlretrieve('http://books.toscrape.com/media/cache/26/f5/26f5d20239a45046e756c6d09611b3ea.jpg', 'image_name.jpg')
	
	#shutil.move('image_name.jpg','./category/category_images')
except OSError:
	pass
print(path)


	






	