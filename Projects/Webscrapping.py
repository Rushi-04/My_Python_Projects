import requests

from bs4 import BeautifulSoup

#url
url = "https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/"

#Request to the site
req = requests.get(url)

#Creating instance 
soup = BeautifulSoup(req.content,"html.parser")


res = soup.title

#printing 
print(soup.prettify())
print(res.prettify())
print(res.get_text())
# print(soup.get_text())
# print(res.get_text())

