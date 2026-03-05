import json
import pickle

def montarPickleDeJSON(arquivoJSONEntrada, pickleSaida):
    with open(arquivoJSONEntrada, encoding='utf-8-sig') as json_file:
        #text = json_file.read()
        json_data = json.load(json_file)
    with open(pickleSaida, 'wb') as arquivo:
        pickle.dump(json_data, arquivo)
    return True

def lerPickle(pickleEntrada):
    with open(pickleEntrada,'rb') as arquivo:
        valores = pickle.load(arquivo)
    return valores

#print(montarPickleDeJSON('data.txt','circuitos.pkl'))

#circuitos = lerPickle('circuitos.pkl')

#for i in circuitos:
#    print(type(i))

#with open('data.txt', 'r', encoding='utf-8-sig') as json_file:
#    #text = json_file.read()
#    json_data = json.load(json_file)