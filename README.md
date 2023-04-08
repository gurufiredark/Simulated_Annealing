# Terceiro Trabalho Modelagem e Otimização de Algoritmos - Parte 2

## Descrição:

O trabalho a seguir tem como intuito utilizar o algoritmo de otimização "Simulated Annealing", que é um algoritmo inspirado no processo de aquecimento e resfriamento de um material. Ele é baseado em um processo físico chamado de "recozimento simulado".

Nesse cado utilizaremos deste algortimo para resolver o Problema da Mochila.

O Problema da Mochila é um problema clássico de otimização combinatória que consiste em escolher um subconjunto de itens de uma lista, de modo a maximizar o valor total dos itens selecionados, considerando-se que a soma dos pesos dos itens selecionados não ultrapasse uma capacidade pré-definida. Em outras palavras, o problema consiste em escolher os itens mais valiosos que possam caber em uma mochila de capacidade limitada.

No contexto do Simulated Annealing, o processo de recozimento é simulado por meio de um processo iterativo que consiste em escolher aleatoriamente uma solução inicial e aplicar perturbações nessa solução para gerar novas soluções candidatas. O algoritmo avalia a qualidade de cada solução candidata, por meio de uma função de custo ou função objetivo, e decide se deve aceitar ou rejeitar a solução, com base na diferença de custo em relação à solução atual e na temperatura corrente do sistema.

## Como executar:

Basicamente, basta executar o SA_knapsack.py, que irá executar o algoritmo com os parâmetros pré-definidos no código.

Caso queira executar com outros parâmetros, basta executar o arquivo SA_knapsack.py com os parâmetros desejados, mudando nas variáveis: values, weights, capacity.

## Alunos:

Gabriel Biscaia 118928  
Gabriel Rodrigues 118038  
Pedro Zafalon 120117
