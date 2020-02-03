with open('paragrafos.txt') as f:
    linhas = f.readlines()
    for linha in linhas:
        if linha[0:3] == '[<a':
            print(linha)
            with open('raw_cids.txt', 'a+') as f2:
                f2.write(linha + '\n')