# demo of getting simple page via python
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page
print(page)
html_bytes = page.read()
print(html_bytes)
print("made nice with .decode():")
html = html_bytes.decode("utf-8")
print(html)