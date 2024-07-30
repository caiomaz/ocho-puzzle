import numpy as np
from collections import deque
import copy
import time

# Função para verificar se o estado atual é o estado objetivo
def e_objetivo(matriz, objetivo):
    return matriz == objetivo

# Função para encontrar a posição do espaço em branco (representado por 0)
def encontrar_branco(matriz):
    for i in range(3):  # Percorre as linhas da matriz
        for j in range(3):  # Percorre as colunas da matriz
            if matriz[i][j] == 0:  # Verifica se o elemento é o espaço em branco
                return i, j  # Retorna a posição do espaço em branco
    return None

# Função para gerar estados filhos a partir do estado atual
def gerar_filhos(matriz):
    filhos = []
    x, y = encontrar_branco(matriz)  # Encontra a posição do espaço em branco
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Definição dos movimentos possíveis (cima, baixo, esquerda, direita)

    for movimento in movimentos:  # Itera sobre os movimentos possíveis
        novo_x, novo_y = x + movimento[0], y + movimento[1]  # Calcula a nova posição do espaço em branco

        if 0 <= novo_x < 3 and 0 <= novo_y < 3:  # Verifica se a nova posição está dentro dos limites da matriz
            nova_matriz = copy.deepcopy(matriz)  # Cria uma cópia da matriz atual
            # Troca o espaço em branco com o elemento na nova posição
            nova_matriz[x][y], nova_matriz[novo_x][novo_y] = nova_matriz[novo_x][novo_y], nova_matriz[x][y]
            filhos.append(nova_matriz)  # Adiciona a nova matriz gerada à lista de filhos
    
    return filhos

# Função de Busca em Largura (BFS)
def busca_em_largura(inicial, objetivo):
    fila = deque([inicial])  # Inicializa a fila com o estado inicial
    visitados = set()  # Conjunto para armazenar os estados já visitados
    caminho = []  # Lista para armazenar o caminho percorrido

    start_time = time.time()  # Inicia a contagem do tempo

    while fila:  # Enquanto houver estados na fila
        estado = fila.popleft()  # Remove o primeiro estado da fila
        estado_tupla = tuple(map(tuple, estado))  # Converte a matriz para uma tupla para permitir a comparação

        if estado_tupla in visitados:  # Verifica se o estado já foi visitado
            continue

        visitados.add(estado_tupla)  # Marca o estado como visitado
        caminho.append(estado)  # Adiciona o estado ao caminho percorrido

        if e_objetivo(estado, objetivo):  # Verifica se o estado atual é o objetivo
            end_time = time.time()  # Para a contagem do tempo
            return estado, caminho, end_time - start_time  # Retorna o estado final, o caminho e o tempo de execução

        filhos = gerar_filhos(estado)  # Gera os estados filhos a partir do estado atual
        for filho in filhos:  # Adiciona os estados filhos à fila
            fila.append(filho)
    
    end_time = time.time()  # Para a contagem do tempo caso não encontre a solução
    return None, caminho, end_time - start_time

# Função de Busca em Profundidade (DFS)
def busca_em_profundidade(inicial, objetivo):
    pilha = [inicial]  # Inicializa a pilha com o estado inicial
    visitados = set()  # Conjunto para armazenar os estados já visitados
    caminho = []  # Lista para armazenar o caminho percorrido

    start_time = time.time()  # Inicia a contagem do tempo

    while pilha:  # Enquanto houver estados na pilha
        estado = pilha.pop()  # Remove o último estado da pilha
        estado_tupla = tuple(map(tuple, estado))  # Converte a matriz para uma tupla para permitir a comparação

        if estado_tupla in visitados:  # Verifica se o estado já foi visitado
            continue

        visitados.add(estado_tupla)  # Marca o estado como visitado
        caminho.append(estado)  # Adiciona o estado ao caminho percorrido

        if e_objetivo(estado, objetivo):  # Verifica se o estado atual é o objetivo
            end_time = time.time()  # Para a contagem do tempo
            return estado, caminho, end_time - start_time  # Retorna o estado final, o caminho e o tempo de execução

        filhos = gerar_filhos(estado)  # Gera os estados filhos a partir do estado atual
        for filho in filhos:  # Adiciona os estados filhos à pilha
            pilha.append(filho)
    
    end_time = time.time()  # Para a contagem do tempo caso não encontre a solução
    return None, caminho, end_time - start_time

# Função para imprimir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:  # Itera sobre as linhas da matriz
        print(linha)  # Imprime a linha

# Função para tratar erros de entrada do usuário
def ler_matriz(nome):
    matriz = []
    for i in range(3):  # Itera sobre as 3 linhas da matriz
        while True:  # Loop para garantir a entrada válida
            try:
                linha = list(map(int, input(f"Linha {i+1} ({nome}): ").split()))  # Lê a linha e converte para inteiros
                if len(linha) != 3 or not all(0 <= x <= 8 for x in linha):  # Verifica se a linha tem 3 números entre 0 e 8
                    raise ValueError  # Levanta um erro se a condição não for satisfeita
                matriz.append(linha)  # Adiciona a linha à matriz
                break  # Sai do loop
            except ValueError:  # Trata o erro levantado
                print("Entrada inválida! Insira 3 números de 0 a 8, separados por espaços.")
    return matriz

# Função principal
def main():
    print("Bem-vindo ao 8-puzzle solver!")
    
    print("Insira a matriz inicial (use 0 para o espaço em branco):")
    inicial = ler_matriz("inicial")  # Lê a matriz inicial do usuário

    print("Insira a matriz objetivo (use 0 para o espaço em branco):")
    objetivo = ler_matriz("objetivo")  # Lê a matriz objetivo do usuário

    print("Escolha o algoritmo de busca:")
    print("1. Busca em Largura (BFS)")
    print("2. Busca em Profundidade (DFS)")
    while True:  # Loop para garantir a escolha válida do algoritmo
        try:
            escolha = int(input("Digite o número da sua escolha: "))  # Lê a escolha do usuário
            if escolha not in [1, 2]:  # Verifica se a escolha é válida
                raise ValueError  # Levanta um erro se a escolha não for válida
            break  # Sai do loop
        except ValueError:  # Trata o erro levantado
            print("Escolha inválida! Digite 1 para BFS ou 2 para DFS.")

    if escolha == 1:
        resultado, caminho, tempo = busca_em_largura(inicial, objetivo)  # Executa a busca em largura
    elif escolha == 2:
        resultado, caminho, tempo = busca_em_profundidade(inicial, objetivo)  # Executa a busca em profundidade

    if resultado:
        print("Solução encontrada:")
        imprimir_matriz(resultado)  # Imprime a matriz solução
        print(f"Tempo de execução: {tempo:.4f} segundos")  # Imprime o tempo de execução
        print("Caminho percorrido:")
        for passo in caminho:  # Itera sobre os passos do caminho
            imprimir_matriz(passo)  # Imprime cada passo do caminho
            print("---------")
    else:
        print("Nenhuma solução encontrada.")  # Imprime se não encontrou solução
        print(f"Tempo de execução: {tempo:.4f} segundos")  # Imprime o tempo de execução

if __name__ == "__main__":
    main()
