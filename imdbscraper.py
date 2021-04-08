from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.request


html = urlopen('https://www.imdb.com/list/ls050745379/')
bs = BeautifulSoup(html, 'html.parser')
l = []
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images:
    x = image['src']+'\n'
    l.append(x)

for i in range(10):
    url = l[i]
    urllib.request.urlretrieve(url, 'D:/Users/Heisenberg/Desktop/image_analysis_deepface/sample_data/%s.jpg '%i)

for i in range(10):
    url="%s.jpg" %i