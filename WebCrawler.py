import urllib.request
from urllib.parse import urlparse
import re

textfile = open('links.txt','w') # File containing the links

url = input('Enter URL: ')

try:
    response = urllib.request.urlopen(url)

    m = re.findall(r'https*://(?:www\.)?[\w-]+(?:[./][\w-]+)*\.\w{2,6}', response.read().decode('utf-8'), re.I)
    if m:
        for match in m:
            textfile.write(match + '\n')

except Exception as e:
    print(e.__class__.__name__,e)

textfile.close()
