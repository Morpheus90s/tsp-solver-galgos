from abc import ABC, abstractmethod
import numpy as np

# Interface Base (Strategy Pattern)
class TSPSolverStrategy(ABC):
    @abstractmethod
    def solve(self, matrix: np.ndarray, start_node: int = 0) -> list:
        """Deve retornar uma lista com a ordem dos nodes (tour)."""
        pass

# Implementação Concreta: Vizinho Mais Próximo
class NearestNeighborStrategy(TSPSolverStrategy):
    def solve(self, matrix: np.ndarray, start_node: int = 0) -> list:
        num_nodes = len(matrix)
        unvisited = set(range(num_nodes))
        tour = [start_node]
        unvisited.remove(start_node)

        current_node = start_node
        while unvisited:
            # Encontra o node não visitado com a menor distância do atual
            next_node = min(unvisited, key=lambda node: matrix[current_node][node])
            unvisited.remove(next_node)
            tour.append(next_node)
            current_node = next_node
        
        # O TSP exige o retorno à origem, mas a tsplib95.trace_tours 
        # já lida com o fechamento do ciclo[cite: 819].
        return tour