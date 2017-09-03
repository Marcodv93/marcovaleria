### google search for images function
from urllib import request
import requests
from bs4 import BeautifulSoup

url="https://www.google.be/search?tbm=isch&q=papa%20francisco"
r=requests.get(url)
sauce=r.content
soup=BeautifulSoup(sauce, "html.parser")
myimages=soup.findAll('img')

i=0
for image in myimages:
    i+=1
    name='image'+str(i)+'.jpg'
    request.urlretrieve(str(image['src']),name)
    if i>2:
    break