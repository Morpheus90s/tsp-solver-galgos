from src.loader import TSPLoader
from src.strategies import NearestNeighborStrategy, TwoOptStrategy, SimulatedAnnealingStrategy
from src.visualizer import plot_tsp_comparison

# 0. Carregamento dos Dados (O que estava faltando!)
# Substitua pelo caminho correto da sua instância
matrix, problem = TSPLoader.load_matrix("data/eil51.tsp")

# 1. Construção (Nearest Neighbor) -> Baseline
nn_solver = NearestNeighborStrategy()
tour_nn = nn_solver.solve(matrix)
dist_nn = int(problem.trace_tours([tour_nn])[0])

# 2. Refinamento (2-Opt) -> Melhoria Local
two_opt_solver = TwoOptStrategy()
tour_2opt = two_opt_solver.solve(matrix, initial_tour=tour_nn)
dist_2opt = int(problem.trace_tours([tour_2opt])[0])

# 3. Meta-heurística (Simulated Annealing) -> Estado da Arte
sa_solver = SimulatedAnnealingStrategy()
# Iniciamos com Warm Start a partir do 2-Opt
# Aumentamos a Temperatura Inicial e deixamos o Alpha mais lento (0.9995)
tour_sa = sa_solver.solve(matrix, initial_tour=tour_2opt, T_start=500.0, alpha=0.9999, T_min=0.01)
dist_sa = int(problem.trace_tours([tour_sa])[0])

# 4. Exibição de Resultados
print("-" * 40)
print(f"ESTRATÉGIA      | DISTÂNCIA")
print("-" * 40)
print(f"Nearest Neighbor | {dist_nn}")
print(f"2-Opt (Local)    | {dist_2opt}")
print(f"Simulated Ann.   | {dist_sa}")
print("-" * 40)

# 5. Visualização (Comparando o melhor resultado com a baseline)
plot_tsp_comparison(problem, tour_nn, tour_sa, dist_nn, dist_sa)
