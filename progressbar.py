from tqdm import tqdm
import time

# Simulação de alguma tarefa que demora
#def minha_tarefa():
#    for _ in tqdm(range(100), desc='Executando tarefa', position=0):
#        time.sleep(0.1)  # Simula o tempo de execução

# Chamada da função para executar a tarefa
#minha_tarefa()

# Criando a barra de progresso final
barra_final = tqdm(total=1, position=0)
barra_final.set_description("Concluído")  # Define a descrição da barra final
barra_final.update(1)  # Atualiza a barra para 100%
