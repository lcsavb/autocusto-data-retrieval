import json
import requests

cids = '''M05.0, M05.3, M05.8, M06.0, M06.8, M08.0, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, Q80.0, Q80.1, Q80.2, Q80.3, Q80.8, Q82.8, M08.0, M08.1, M08.2, M08.3, M08.4, M08.8, M08.9, M05.0, M05.3, M05.8, M06.0, M06.8, M08.0, K50.0, K50.1, K50.8, L73.2, L40.0, L40.1, L40.4, L40.8, H30.1, H30.2, H30.8, H20.1, H15.0, E84.0, E84.8, N18.0, N18.8, D18.0, B18.0, B18.1, B17.1, B18.2, G20, I27.0, I27.2, I27.8, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, D61.0, G35, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, I27.0, I27.2, I27.8, G20, J45.0, J45.1, J45.8, E22.0, L40.0, L40.1, L40.4, L40.8, M88.0, M88.8, E83.3, N18.0, N25.0, E20.0, E20.1, E20.8, E89.2, N18.8, M05.0, M05.3, M05.8, M06.0, M06.8, K50.0, K50.1, K50.8, M45, M46.8, D59.0, D59.1, D59.0, D59.1, E83.3, N18.0, N25.0, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, E25.0, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, L40.0, L40.1, L40.4, L40.8, I20.0, I20.1, I21.0, I21.1, I21.2, I21.3, I21.4, I21.9, I22.0, I22.1, I22.8, I22.9, I23.0, I23.1, I23.2, I23.3, I23.4, I23.5, I23.6, I23.8, I24.0, I24.8, I24.9, M05.0, M05.3, M05.8, M06.0, M06.8, M08.0, L93.0, L93.1, M32.1, M32.8, G20, F20.0, F20.1, F20.2, F20.3, F20.4, F20.5, F20.6, F20.8, R52.1, R52.2, E70.0, E70.1, D84.1, E83.1, T45.4, E83.1, T45.4, E83.3, N18.0, N25.0, E83.1, T45.4, E23.2, G30.0, G30.1, G30.8, F00.0, F00.1, F00.2, D69.3, G20, B18.0, B18.1, M07.0, M07.2, M07.3, L40.0, L40.1, L40.4, L40.8, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, T86.1, Z94.0, T86.4, Z94.4, T86.4, Z94.4, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, J45.0, J45.1, J45.8, J44.0, J44.1, J44.8, D46.0, D46.1, D46.7, D61.0, D61.1, D61.2, D61.3, D61.8, D70, Z94.8, B17.1, B18.2, G35, E25.0, J45.0, J45.1, J45.8, J45.0, J45.1, J45.8, G35, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, G30.0, G30.1, G30.8, F00.0, F00.1, F00.2, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, G35, B17.1, B18.2, M07.0, M07.2, M07.3, M05.0, M05.3, M05.8, M06.0, M06.8, M45, M46.8, N80.0, N80.1, N80.2, N80.3, N80.4, N80.5, N80.8, M05.0, M05.3, M05.8, M06.0, M06.8, M08.0, D56.1, D56.8, D57.0, D57.1, D57.2, E76.1, I27.0, I27.2, I27.8, E75.2, B16.0, B16.2, B18.0, B18.1, D59.0, D59.1, M05.0, M05.3, M05.8, M06.0, M06.8, M08.0, E10.0, E10.1, E10.2, E10.3, E10.4, E10.5, E10.6, E10.7, E10.8, E10.9, L70.0, L70.1, L70.8, B18.0, B18.1, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, E22.0, E76.0, B17.1, B18.2, M07.0, M07.2, M07.3, D25.0, D25.1, D25.2, K50.0, K50.1, K50.8, K51.0, K51.1, K51.2, K51.3, K51.4, K51.5, K51.8, R52.1, R52.2, M07.0, M07.2, M07.3, Z94.1, Z94.1, E75.2, R52.1, R52.2, M07.0, M07.2, M07.3, G35, E22.0, F20.0, F20.1, F20.2, F20.3, F20.4, F20.5, F20.6, F20.8, M80.0, M80.1, M80.2, M80.3, M80.4, M80.5, M80.8, M81.0, M81.1, M81.2, M81.3, M81.4, M81.5, M81.6, M81.8, M82.0, M82.1, M82.8, E84.1, E84.8, E83.3, N18.0, N25.0, E83.0, G70.0, G20, E78.0, E78.1, E78.2, E78.3, E78.4, E78.5, E78.6, E78.8, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, F20.0, F20.1, F20.2, F20.3, F20.4, F20.5, F20.6, F20.8, M80.0, M80.1, M80.2, M80.3, M80.4, M80.5, M80.8, M81.0, M81.1, M81.2, M81.3, M81.4, M81.5, M81.6, M81.8, M82.0, M82.1, M82.8, B17.1, B18.2, G12.2, M80.0, M80.1, M80.2, M80.3, M80.4, M80.5, M80.8, M81.0, M81.1, M81.2, M81.3, M81.4, M81.5, M81.6, M81.8, M82.0, M82.1, M82.8, F84.0, F84.1, F84.3, F84.5, F84.8, M05.0, M05.3, M05.8, M06.0, M06.8, N18.0, N18.8, M07.0, M07.2, M07.3, M45, M46.8, L40.0, L40.1, L40.4, L40.8, G20, E83.3, N18.0, N25.0, I27.0, I27.2, I27.8, T86.1, Z94.0, T86.4, Z94.4, B17.1, B18.2, E23.0, M07.0, M07.2, M07.3, E85.1, N04.0, N04.1, N04.2, N04.3, N04.4, N04.5, N04.6, N04.7, N04.8, E75.2, B18.0, B18.1, G35, M05.0, M05.3, M05.8, M06.0, M06.8, M08.0, M05.0, M05.3, M05.8, M06.0, M06.8, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, G24.3, G24.4, G24.5, G24.8, G51.3, G51.8, D25.0, D25.1, D25.2, E22.8, N80.0, N80.1, N80.2, N80.3, N80.4, N80.5, N80.8, G40.0, G40.1, G40.2, G40.3, G40.4, G40.5, G40.6, G40.7, G40.8, F20.0, F20.1, 20.2, F20.3, F20.4, F20.5, F20.6, F20.8'''

cids_separados = (cids.split(', '))
cids_alto_custo = []

for cid in cids_separados:
    if cid not in cids_alto_custo:
        cids_alto_custo.append(cid)

cids_finais = ['M05.0', 'M05.3', 'M05.8', 'M06.0', 'M06.8', 'M08.0', 'E78.0', 'E78.1',
'E78.2', 'E78.3', 'E78.4', 'E78.5', 'E78.6', 'E78.8', 'Q80.0', 'Q80.1', 'Q80.2', 'Q80.3',
'Q80.8', 'Q82.8', 'M08.1', 'M08.2', 'M08.3', 'M08.4', 'M08.8', 'M08.9', 'K50.0', 'K50.1',
'K50.8', 'L73.2', 'L40.0', 'L40.1', 'L40.4', 'L40.8', 'H30.1', 'H30.2', 'H30.8', 'H20.1',
'H15.0', 'E84.0', 'E84.8', 'N18.0', 'N18.8', 'D18.0', 'B18.0', 'B18.1', 'B17.1', 'B18.2',
'G20', 'I27.0', 'I27.2', 'I27.8', 'D61.0', 'G35', 'J45.0', 'J45.1', 'J45.8', 'E22.0',
'M88.0', 'M88.8', 'E83.3', 'N25.0', 'E20.0', 'E20.1', 'E20.8', 'E89.2', 'M45', 'M46.8',
'D59.0', 'D59.1', 'E25.0', 'G40.0', 'G40.1', 'G40.2', 'G40.3', 'G40.4', 'G40.5', 'G40.6',
'G40.7', 'G40.8', 'I20.0', 'I20.1', 'I21.0', 'I21.1', 'I21.2', 'I21.3', 'I21.4', 'I21.9',
'I22.0', 'I22.1', 'I22.8', 'I22.9', 'I23.0', 'I23.1', 'I23.2', 'I23.3', 'I23.4', 'I23.5',
'I23.6', 'I23.8', 'I24.0', 'I24.8', 'I24.9', 'L93.0', 'L93.1', 'M32.1', 'M32.8', 'F20.0',
'F20.1', 'F20.2', 'F20.3', 'F20.4', 'F20.5', 'F20.6', 'F20.8', 'R52.1', 'R52.2', 'E70.0',
'E70.1', 'D84.1', 'E83.1', 'T45.4', 'E23.2', 'G30.0', 'G30.1', 'G30.8', 'F00.0', 'F00.1',
'F00.2', 'D69.3', 'M07.0', 'M07.2', 'M07.3', 'T86.1', 'Z94.0', 'T86.4', 'Z94.4', 'J44.0',
'J44.1', 'J44.8', 'D46.0', 'D46.1', 'D46.7', 'D61.1', 'D61.2', 'D61.3', 'D61.8', 'D70',
'Z94.8', 'N80.0', 'N80.1', 'N80.2', 'N80.3', 'N80.4', 'N80.5', 'N80.8', 'D56.1', 'D56.8',
'D57.0', 'D57.1', 'D57.2', 'E76.1', 'E75.2', 'B16.0', 'B16.2', 'E10.0', 'E10.1', 'E10.2',
'E10.3', 'E10.4', 'E10.5', 'E10.6', 'E10.7', 'E10.8', 'E10.9', 'L70.0', 'L70.1', 'L70.8',
'E76.0', 'D25.0', 'D25.1', 'D25.2', 'K51.0', 'K51.1', 'K51.2', 'K51.3', 'K51.4', 'K51.5',
'K51.8', 'Z94.1', 'M80.0', 'M80.1', 'M80.2', 'M80.3', 'M80.4', 'M80.5', 'M80.8', 'M81.0',
'M81.1', 'M81.2', 'M81.3', 'M81.4', 'M81.5', 'M81.6', 'M81.8', 'M82.0', 'M82.1', 'M82.8',
'E84.1', 'E83.0', 'G70.0', 'G12.2', 'F84.0', 'F84.1', 'F84.3', 'F84.5', 'F84.8', 'E23.0',
'E85.1', 'N04.0', 'N04.1', 'N04.2', 'N04.3', 'N04.4', 'N04.5', 'N04.6', 'N04.7', 'N04.8',
'G24.3', 'G24.4', 'G24.5', 'G24.8', 'G51.3', 'G51.8', 'E22.8']

resposta = requests.get('https://cid10-api.herokuapp.com/cid10/F20.1')
print(resposta.json()['nome'])

dicionario_final = {}
for cid in cids_finais:
    busca = f'https://cid10-api.herokuapp.com/cid10/{cid}'
    diagnostico = requests.get(busca).json()['nome']
    dicionario_final[cid] = diagnostico
    
print(dicionario_final)