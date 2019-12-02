import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print ("Retrieving: ", url)
for i in range(count):
    next_url = tags[pos-1].get('href', None)
    print("Retrieving: ", next_url)
    next_html = urllib.request.urlopen(next_url, context=ctx).read()
    next_soup = BeautifulSoup(next_html, 'html.parser')
    tags = next_soup('a')
