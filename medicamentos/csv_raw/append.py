import os
import glob
import pandas as pd

os.chdir('/home/lucas/dev/chupador/medicamentos/csv_raw/nomes/')

extensao = 'csv'

nomes_arquivos = [i for i in glob.glob(f'*.{extensao}')]

csv_combinado = pd.concat([pd.read_csv(n) for n in nomes_arquivos])

csv_combinado.to_csv('medicamentos.csv', index=False, encoding='utf-8-sig')