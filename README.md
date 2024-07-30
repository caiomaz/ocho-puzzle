# 8-Puzzle Solver

Este projeto implementa uma solução para o problema do 8-puzzle usando dois algoritmos de busca: Busca em Largura (BFS) e Busca em Profundidade (DFS). O objetivo é organizar a matriz 3x3 contendo os números de 1 a 8 e um espaço em branco (representado pelo número 0), para que ela fique em uma ordem específica.

## Funcionalidades

- **Busca em Largura (BFS)**: Explora todos os nós em um nível antes de ir para o próximo nível.
- **Busca em Profundidade (DFS)**: Explora o mais profundo possível antes de retroceder.
- **Verificação Passo a Passo**: Exibe a organização da matriz em cada passo do caminho percorrido.
- **Medição de Tempo de Execução**: Mede o tempo de execução de cada algoritmo.

## Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Este código foi testado com Python 3.8+.

## Como usar

1. Clone este repositório para sua máquina local ou baixe o arquivo `8_puzzle_solver.py`.

2. Execute o programa no seu ambiente de desenvolvimento Python:
    ```
    $ python 8_puzzle_solver.py
    ```

3. Insira a matriz inicial e a matriz objetivo conforme solicitado pelo programa. Use 0 para representar o espaço em branco.

4. Escolha o algoritmo de busca:
    - Digite 1 para Busca em Largura (BFS)
    - Digite 2 para Busca em Profundidade (DFS)

5. O programa exibirá a solução encontrada, o tempo de execução e o caminho percorrido.

## Exemplo de uso
```
Bem-vindo ao 8-puzzle solver!
Insira a matriz inicial (use 0 para o espaço em branco):
Linha 1 (inicial): 1 2 3
Linha 2 (inicial): 4 0 5
Linha 3 (inicial): 6 7 8
Insira a matriz objetivo (use 0 para o espaço em branco):
Linha 1 (objetivo): 1 2 3
Linha 2 (objetivo): 4 5 6
Linha 3 (objetivo): 7 8 0
Escolha o algoritmo de busca:
    Busca em Largura (BFS)
    Busca em Profundidade (DFS)
    Digite o número da sua escolha: 1
    Solução encontrada:
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 0]
    Tempo de execução: 0.0023 segundos
    Caminho percorrido:
    ...
```