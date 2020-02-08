import json
import urllib.request
from bs4 import BeautifulSoup
from vinculador import busca_cid, verificar_int

# url = urllib.request.urlopen('http://www.saude.sp.gov.br/ses/perfil/gestor/assistencia-farmaceutica/medicamentos-dos-componentes-da-assistencia-farmaceutica/links-do-componente-especializado-da-assistencia-farmaceutica/relacao-estadual-de-medicamentos-do-componente-especializado-da-assistencia-farmaceutica/consulta-por-medicamento')

# sopa = BeautifulSoup(url,'html.parser')

# dicionario = {}
# for link in sopa.find_all('a'):
#     end_link = str(link.get('href'))
#     if end_link[0] != 'h':
#         end_link = 'http://www.saude.sp.gov.br' + end_link
#     dicionario[link.string] = [end_link]
    

# with open('med_links.json', 'w') as arquivo:
#     arquivo.write(json.dumps(dicionario, indent=4, ensure_ascii=False))

with open('med_links.json', 'r') as arquivo:
    lista_meds = json.load(arquivo)

for link in lista_meds.values():
    url = urllib.request.urlopen(link[0])
    sopa = BeautifulSoup(url,'html.parser')
    cids = busca_cid(sopa.get_text())
    print(cids)
    link.append(cids)

with open('med_links_cids.json', 'w') as arquivo:
    arquivo.write(json.dumps(lista_meds, indent=4, ensure_ascii=False))