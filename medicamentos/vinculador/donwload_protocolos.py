import urllib.request
from bs4 import BeautifulSoup
from tika import parser
import requests
import substring
import os

url_indice = 'http://www.saude.sp.gov.br/ses/perfil/gestor/assistencia-farmaceutica/medicamentos-dos-componentes-da-assistencia-farmaceutica/links-do-componente-especializado-da-assistencia-farmaceutica/relacao-estadual-de-medicamentos-do-componente-especializado-da-assistencia-farmaceutica/consulta-por-protocolo-clinico-e-diretriz-terapeutica'
indice = urllib.request.urlopen(url_indice)

sopa = BeautifulSoup(indice, 'html.parser')

for link in sopa.find_all('a'):
    endereco = str(link.get('href'))
    if '/resources/' in endereco:
        if endereco[0] != 'h':
            endereco = 'http://saude.sp.gov.br' + endereco
        endereco = str(endereco)
        os.system('wget ' + endereco)
        