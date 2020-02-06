import glob
from tika import parser
import substring
import json

def verificar_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def busca_cid(c):
    lista_cids = []
    for i in range(len(c)):
        if c[i].upper() and c[i].isalpha():
            if verificar_int(c[i + 1]) and verificar_int(c[i + 2]):
                possivel_cid = (c[i:i+5]).rstrip()
                lista_cids.append(possivel_cid)
            else:
                continue
    
    return lista_cids

arquivos = glob.iglob('/home/lucas/dev/chupador/medicamentos/vinculador/protocolos/*.*')

protocolos_cids = {}
for a in arquivos:
    texto = parser.from_file(a)['content']
    lista_cids = busca_cid(texto)
    try:
        nome_protocolo = substring.substringByChar(str(a), '_', '.')
        nome_protocolo = nome_protocolo[1:-1]
    except:
        nome_protocolo = 'nao identificado'

    protocolos_cids.update({nome_protocolo:lista_cids})

protocolos_json = json.dumps(protocolos_cids, indent=1)

with open('protocolos.json', 'w') as novo_arquivo:
    novo_arquivo.write(protocolos_json)
    
    



