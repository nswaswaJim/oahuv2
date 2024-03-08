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

