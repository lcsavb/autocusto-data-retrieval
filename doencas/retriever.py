from bs4 import BeautifulSoup
import urllib.request
import re

pagina = open('lista_medicamentos.html')
sopa = BeautifulSoup(pagina)
links = []
for link in sopa.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))
pagina.close()

f = open('paragrafos.txt', 'a+')

for link in links:
    pagina_med = urllib.request.urlopen(link)
    sopa = BeautifulSoup(pagina_med, 'html.parser')
    for pagina in sopa.find_all('p'):
        f.write(str(pagina.contents) + '\n')

f.close()