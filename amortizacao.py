def amortizador (saldo_devedor_inicial, taxa_juros, prazo):
    amortizacao = 0
    pagamento = 0
    juros = 0
    total_juros = 0
    saldo_devedor = saldo_devedor_inicial
    for i in range(0, prazo + 1):
        print(juros, pagamento, amortizacao, saldo_devedor)
        juros = saldo_devedor * taxa_juros
        total_juros += juros
        amortizacao = saldo_devedor_inicial/prazo
        saldo_devedor -= amortizacao
        pagamento = amortizacao + juros
    print(total_juros)



amortizador(400000, 0.075, 30)
