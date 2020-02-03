import csv

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
            if nome == list(medicamentos.keys())[:-1]:         
                medicamentos[nome] += apresentacao
            else:        
                novo_medicamento = {nome: apresentacao}
                medicamentos.update(novo_medicamento)

with open('lista_medicamentos.txt', 'w') as arquivo_med:
    arquivo_med.write(medicamentos)