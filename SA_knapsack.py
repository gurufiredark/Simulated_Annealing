import random
import math

def simulated_annealing_knapsack(values, weights, capacity, initial_temperature=1000, cooling_rate=0.003, stopping_temperature=1e-8, max_iterations=10000):
    # Inicializa a solução atual e o melhor resultado
    current_solution = [random.randint(0, 1) for _ in values]
    best_solution = current_solution.copy()
    
    # Inicializa a temperatura e o número de iterações
    temperature = initial_temperature
    iteration = 0
    
    # Enquanto a temperatura for maior que a temperatura de parada e o número de iterações não ultrapassar o máximo permitido
    while temperature > stopping_temperature and iteration < max_iterations:
        # Escolhe um índice aleatório para modificar a solução
        index = random.randint(0, len(values)-1)
        
        # Gera uma nova solução com o item escolhido modificado
        new_solution = current_solution.copy()
        new_solution[index] = 1 - new_solution[index]
        
        # Calcula o valor e o peso da nova solução
        new_value = sum([v*s for v, s in zip(values, new_solution)])
        new_weight = sum([w*s for w, s in zip(weights, new_solution)])
        
        # Se a nova solução não ultrapassar a capacidade máxima da mochila, aceita a solução com uma probabilidade calculada pelo algoritmo Simulated Annealing
        if new_weight <= capacity:
            delta = new_value - sum([v*s for v, s in zip(values, current_solution)])
            probability = math.exp(delta/temperature)
            if random.random() < probability:
                current_solution = new_solution
                
        # Se a nova solução for melhor do que a melhor solução encontrada até agora, atualiza a melhor solução
        if sum([v*s for v, s in zip(values, current_solution)]) > sum([v*s for v, s in zip(values, best_solution)]):
            best_solution = current_solution.copy()
            
        # Resfria a temperatura
        temperature *= 1 - cooling_rate
        
        # Incrementa o número de iterações
        iteration += 1
    
    return best_solution

# Exemplo de uso
values = [60, 100, 120, 50, 80, 70, 30, 10, 20, 40]
weights = [10, 20, 30, 10, 20, 10, 5, 2, 4, 8]
capacity = 50

best_solution = simulated_annealing_knapsack(values, weights, capacity)

# Imprime a solução encontrada
print("Itens incluídos na mochila:")
for i, item in enumerate(best_solution):
    if item == 1:
        print(f"Item {i}: valor={values[i]}, peso={weights[i]}")
print(f"Valor total: {sum([v*s for v, s in zip(values, best_solution)])}")
print(f"Peso total: {sum([w*s for w, s in zip(weights, best_solution)])}")