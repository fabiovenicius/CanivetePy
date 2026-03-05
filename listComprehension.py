preco = [100, 150, 300, 5500]
#Performar 1 ação em cada item da lista, criando uma nova lista
preco_com_imposto10 = [round(precoComImposto * 1.1,2) for precoComImposto in preco]
print(preco_com_imposto10)
'''
Qual o item que mais vende?
Usar zip para conectar itens de duas listas
'''
vendas_produto = [1550,500,2100,440]
produtos = ['Café', 'Arroz', 'Frutas','Feijão']
lista_aux = list(zip(vendas_produto,produtos))
print(lista_aux)
lista_aux.sort(reverse=True)
produtos = [produto for vendas, produto in lista_aux]
print(produtos)
'''
Dados de 2019 e 2020
Qual o item que mais vendeu em 2019?
'''
vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]
resposta = [(dados2019, produto) for produto, dados2019, dados2020 in vendas_produtos]
print(max(resposta))
'''
LC com if
'''
meta = 1000
produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produto[i] > meta]
print(produtos_acima_meta)
'''
LC com if-else
'''
resposta = [dados2019 if dados2019 > 600000 else 0 for produto, dados2019, dados2020 in vendas_produtos]
print(resposta)

