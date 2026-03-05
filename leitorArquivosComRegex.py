import re
def leitor(arquivo, padrao):
    linhas = []
    with open(arquivo, 'r') as arquivo:
        for i in arquivo.readlines():
            if re.match(padrao, i):
                linhas.append(i)
    return linhas
