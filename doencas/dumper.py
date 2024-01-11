import substring

arquivo_cids = open('cids.txt', 'w+')

with open('raw_cids.txt', 'r') as f:
    arquivo = f.readlines()
    for linha in arquivo:
        try:
            cids = substring.substringByChar(linha, startChar='(', endChar=')')
            arquivo_cids.write(cids[1:-1])
        except:
            pass

arquivo_cids.close()