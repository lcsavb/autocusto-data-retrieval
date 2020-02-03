import csv
import json

medicamentos = {}



with open('csv_raw/medicamentos.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')

    n = 0
    for linha in leitor:

        nome = linha[0]
        apresentacao = [f'{linha[1]} ' + f'({linha[2]})']


        if n == 0:
            novo_medicamento = {nome: apresentacao}
            medicamentos.update(novo_medicamento)
            n = n + 1
        else:
            if nome == list(medicamentos.keys())[-1]:         
                medicamentos[nome] += apresentacao
            else:        
                novo_medicamento = {nome: apresentacao}
                medicamentos.update(novo_medicamento)

with open('lista_med.json', 'w') as lista_med:
    lista_med.write(json.dumps(medicamentos, indent=4, 
                sort_keys=True, ensure_ascii=False))