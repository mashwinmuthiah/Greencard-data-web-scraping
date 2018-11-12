from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('th')
print("Years")
for tag in tags:
    print(tag.get('Contents:',tag.contents[0]))
    
print("Applicants")
tags = soup('td')
for tag in tags:
    print(tag.get('Contents:',tag.contents[0]))
