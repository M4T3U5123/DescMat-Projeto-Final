# Problema: Análise de sistemas lineares de transporte
# Objetivo: Resolver um problema de alocação de recursos em um sistema de transporte e visualizar os resultados.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Entrada de dados
# Gerar matriz de custos (aleatória)
np.random.seed(42)
custos = np.random.randint(10, 100, size=(5, 5))

# Capacidade de transporte por rota
capacidade = np.random.randint(50, 200, size=5)

# Demanda por local
demanda = np.random.randint(30, 150, size=5)

# Resolução do sistema linear
# Montar sistema Ax = b onde A é a matriz de coeficientes, x as alocações e b as demandas
A = np.eye(5)
b = demanda

# Resolver o sistema linear
try:
    alocacao = np.linalg.solve(A, b)
except np.linalg.LinAlgError as e:
    alocacao = None
    print("Erro ao resolver o sistema linear:", e)

# Visualização dos resultados
def plotar_resultados(custos, capacidade, demanda, alocacao):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Gráficos de barras para capacidade e demanda
    x = np.arange(len(capacidade))
    width = 0.35

    ax.bar(x - width / 2, capacidade, width, label='Capacidade')
    ax.bar(x + width / 2, demanda, width, label='Demanda')

    # Plotar alocação
    if alocacao is not None:
        ax.plot(x, alocacao, 'o-', color='red', label='Alocação')

    ax.set_xlabel('Rotas')
    ax.set_ylabel('Quantidade')
    ax.set_title('Análise de Alocação de Recursos')
    ax.legend()
    plt.show()

# Chamar a função de visualização
plotar_resultados(custos, capacidade, demanda, alocacao)

# Estruturas de dados adicionais
# Exemplo de fila para gerenciar alocações pendentes
from collections import deque

fila_alocacoes = deque()
for i, d in enumerate(demanda):
    fila_alocacoes.append((i, d))

# Processar a fila
while fila_alocacoes:
    rota, qtd = fila_alocacoes.popleft()
    print(f"Processando rota {rota} com demanda de {qtd}")
