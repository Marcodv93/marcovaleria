from urllib import request
import requests
from bs4 import BeautifulSoup

def image_search(query):
	query = query.replace(' ', '+')
	name = str(query)+'.jpg'
	url = 'http://www.freedigitalphotos.net/images/search.php?search='+str(query)
	r = requests.get(url)
	sauce = r.content
	soup = BeautifulSoup(sauce, 'html.parser')
	div = soup.find('div', {'class':'similar-premium'})
	request.urlretrieve(div.img['src'], name)

image_search('cutie pie')