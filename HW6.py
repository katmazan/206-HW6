# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = int(input('Enter count - '))
position = int(input('Enter position - '))

# Retrieve all of the anchor tags
tags = soup('a')
tags_lst = list()
for tag in tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)

for i in range(0,count):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tags_lst = list()
    for tag in tags:
        needed_tag = tag.get('href', None)
        tags_lst.append(needed_tag)    
    print('retrieving: ', tags_lst[position - 1])
    url = tags_lst[position - 1]
        

    html = urllib.request.urlopen(url, context=ctx).read()

    
