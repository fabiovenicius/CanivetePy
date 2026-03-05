interable = [162,235,254,254,52,365,452,627]
def funcao(numero):
    return numero * 3 
#map executa uma funcao em todos os dados
lista = list(map(funcao, interable))
print(interable)
print(lista)