from abc import ABC, abstractmethod
import numpy as np

# Interface Base (Strategy Pattern)
class TSPSolverStrategy(ABC):
    @abstractmethod
    def solve(self, matrix: np.ndarray, start_node: int = 0) -> list:
        """Deve retornar uma lista com a ordem dos nodes (tour)."""
        pass

class NearestNeighborStrategy(TSPSolverStrategy):
    def solve(self, matrix: np.ndarray, start_node: int = 1) -> list:
        # A matrix do numpy é 0-indexed, mas os nodes da TSPLIB são 1-indexed
        num_nodes = len(matrix)
        
        # Ajuste para lidar com IDs que começam em 1
        unvisited = set(range(1, num_nodes + 1))
        tour = [start_node]
        unvisited.remove(start_node)

        current_node = start_node
        while unvisited:
            # Encontra o próximo node. 
            # Nota: na matriz numpy, o node 'i' está na posição 'i-1'
            next_node = min(unvisited, key=lambda node: matrix[current_node-1][node-1])
            unvisited.remove(next_node)
            tour.append(next_node)
            current_node = next_node
        
        return tour
