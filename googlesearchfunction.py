### google search for images function
#test
from urllib import request
import requests
from bs4 import BeautifulSoup

def google_search(query):
	query = query.replace(' ', '%20')
	url="https://www.google.be/search?tbm=isch&q="+str(query)
	r=requests.get(url)
	sauce=r.content
	soup=BeautifulSoup(sauce, "html.parser")
	myimages=soup.findAll('img')

	i=0
	for image in myimages:
	    i+=1
	    name=query+str(i)+'.jpg'
	    request.urlretrieve(str(image['src']),name)
	    if i>2:
	    	break
google_search('cutie pie')
