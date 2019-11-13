### google search for images function

#test by valeria
=======


from urllib import request
import requests
from bs4 import BeautifulSoup
import numpy as np

def google_search(query):
	query = query.replace(' ', '%20')
	url="https://www.google.be/"+str(query)
	r=requests.get(url)
	sauce=r.content
	soup=BeautifulSoup(sauce, "html.parser")
	myimages=soup.findAll('img')
	print(url)
	i=0
	for image in myimages:
	    i+=1
	    name=query+str(i)+'.TIF'
	    request.urlretrieve(str(image['src']),name)
	    if i>2:
	    	break
google_search('ugly spy')

def print_function(inputstring):
	print(inputstring)



def valeria_function(my_string):
		
	if my_string == "valeria":
		print("i love you")
	else:
		print("i love you more")









	
=======
# this is Marco modificationssss

