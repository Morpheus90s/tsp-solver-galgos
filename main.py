from src.loader import TSPLoader
from src.strategies import NearestNeighborStrategy, TwoOptStrategy

# 1. Carregar dados (Instância da TSPLib)
matrix, problem = TSPLoader.load_matrix("data/eil51.tsp")

# 2. Fase de Construção: Gerar Tour Inicial (Gulo)
print("Iniciando fase de construção (Nearest Neighbor)...")
nn_solver = NearestNeighborStrategy()
initial_tour = nn_solver.solve(matrix)
dist_nn = problem.trace_tours([initial_tour])[0]

# 3. Fase de Refinamento: Otimizar Tour (Busca Local)
print("Iniciando fase de refinamento (2-Opt)...")
two_opt_solver = TwoOptStrategy()
# Aqui passamos a rota do NN para ser "descruzada" pelo 2-Opt
refined_tour = two_opt_solver.solve(matrix, initial_tour=initial_tour)
dist_refined = problem.trace_tours([refined_tour])[0]

# 4. Exibir Resultados Comparativos
print("-" * 30)
print(f"Resultado Inicial (NN): {dist_nn}")
print(f"Resultado Refinado (2-Opt): {dist_refined}")
print(f"Melhoria Obtida: {dist_nn - dist_refined} unidades de distância.")
print("-" * 30)
