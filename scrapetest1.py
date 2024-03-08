# demo of getting simple page via python
getpage = input("input page: ")
from urllib.request import urlopen
url = getpage
url = "https://" + url
page = urlopen(url)
print(page)
html_bytes = page.read()
print(html_bytes)
print("made nice with .decode():")
html = html_bytes.decode("utf-8")
print(html)
input("enter to quit")

#Note below import requests requires install first:  pip install requests
import requests 

# Making a GET request 
r = requests.get(url)
# check status code for response received 
# success code - 200 
print(r) 

# print content of request 
print(r.content)

#requests requires code:  pip install requests
#https://example.com/
input("enter to quit")
print(dir(r))
input("enter to really quit")