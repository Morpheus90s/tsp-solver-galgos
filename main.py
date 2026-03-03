from src.loader import TSPLoader
from src.strategies import NearestNeighborStrategy

# 1. Carregar dados
matrix, problem = TSPLoader.load_matrix("data/eil51.tsp")

# 2. Escolher estratégia e resolver
solver = NearestNeighborStrategy()
tour = solver.solve(matrix)

# 3. Calcular distância total (usando a ferramenta oficial do tsplib95)
distance = problem.trace_tours([tour])[0]

print(f"Resultado Vizinho Mais Próximo: {distance}")
