def calcular_taxa_juros(valor_principal, valor_prestacao, num_meses):
    """
    Calcula a taxa de juros mensal aproximada de um empréstimo
    usando o método de Newton-Raphson
    """
    # Taxa inicial estimada (1% ao mês)
    taxa = 0.01
    precisao = 0.0000001  # Precisão do cálculo
    
    while True:
        # Fórmula do valor presente das prestações
        vp = valor_prestacao * (1 - (1 + taxa) ** -num_meses) / taxa
        derivada = valor_prestacao * (
            ((num_meses * (1 + taxa) ** (-num_meses - 1)) * taxa - 
             (1 - (1 + taxa) ** -num_meses)) / (taxa ** 2)
        )
        angulo = vp - valor_principal
        
        # Verifica se a diferença é pequena o suficiente
        if abs(vp - valor_principal) < precisao:
            break
            
        # Atualiza a taxa usando o método de Newton-Raphson
        taxa = taxa - angulo / derivada
    
    return taxa * 100  # Retorna a taxa em porcentagem

def main():
    print("Calculadora de Taxa de Juros de Empréstimo")
    print("-------------------------------------")
    
    try:
        # Entrada de dados pelo usuário
        valor_principal = float(input("Digite o valor principal do empréstimo (R$): "))
        valor_prestacao = float(input("Digite o valor da prestação mensal (R$): "))
        num_meses = int(input("Digite o número de meses do financiamento: "))
        
        # Verifica se os valores são válidos
        if valor_principal <= 0 or valor_prestacao <= 0 or num_meses <= 0:
            print("Erro: Os valores devem ser maiores que zero!")
            return
            
        # Calcula a taxa de juros
        taxa_mensal = calcular_taxa_juros(valor_principal, valor_prestacao, num_meses)
        taxa_anual = ((1 + taxa_mensal/100) ** 12 - 1) * 100
        
        # Exibe os resultados
        print("\nResultados:")
        print(f"Taxa de juros mensal: {taxa_mensal:.2f}%")
        print(f"Taxa de juros anual: {taxa_anual:.2f}%")
        
        # Calcula e mostra o custo total do empréstimo
        custo_total = valor_prestacao * num_meses
        juros_total = custo_total - valor_principal
        print(f"\nCusto total do empréstimo: R$ {custo_total:.2f}")
        print(f"Total pago em juros: R$ {juros_total:.2f}")
        
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos!")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()