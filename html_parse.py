import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
num_list = list()
for tag in tags:
    tagx = str(tag)
    tmp_list = re.findall('[0-9]+', tagx)
    num_list.append(tmp_list[0])
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
total_sum = sum(num_list)
print(num_list)
print(total_sum)
