from urllib import request, parse, error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive all of the achor tags
tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href', None))
