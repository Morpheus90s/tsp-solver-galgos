from abc import ABC, abstractmethod
import numpy as np
import math
import random

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

class TwoOptStrategy(TSPSolverStrategy):
    def solve(self, matrix: np.ndarray, initial_tour: list = None) -> list:
        # Se não houver rota inicial, usa a ordem natural dos nós (canonical)
        tour = list(initial_tour) if initial_tour else list(range(len(matrix)))
        best_tour = tour
        improved = True
        
        while improved:
            improved = False
            for i in range(1, len(best_tour) - 2):
                for j in range(i + 1, len(best_tour)):
                    if j - i == 1: continue  # Arestas adjacentes
                    
                    # Lógica do ganho (delta)
                    # Comparamos o custo de (i-1, i) e (j, j+1) 
                    # com o custo de (i-1, j) e (i, j+1)
                    # Distância atual das duas arestas que vamos tentar trocar
                    old_dist = matrix[best_tour[i-1]-1][best_tour[i]-1] + \
                            matrix[best_tour[j]-1][best_tour[(j+1) % len(best_tour)]-1]

                    # Distância se trocarmos as conexões (o "descruzar")
                    new_dist = matrix[best_tour[i-1]-1][best_tour[j]-1] + \
                            matrix[best_tour[i]-1][best_tour[(j+1) % len(best_tour)]-1]

                    if new_dist < old_dist:
                        # Realiza o swap: inverte o segmento entre i e j
                        best_tour[i:j+1] = reversed(best_tour[i:j+1])
                        improved = True
            
        return best_tour

class SimulatedAnnealingStrategy(TSPSolverStrategy):
    def solve(self, matrix, initial_tour, T_start=100.0, alpha=0.995, T_min=0.001):
        current_tour = list(initial_tour)
        # O custo inicial pode ser calculado via problem.get_weight ou matriz
        def get_cost(t):
            return sum(matrix[t[i]-1][t[(i+1)%len(t)]-1] for i in range(len(t)))

        current_cost = get_cost(current_tour)
        best_tour = list(current_tour)
        best_cost = current_cost
        T = T_start

        while T > T_min:
            # Gera um vizinho usando um 2-opt swap aleatório
            i, j = sorted(random.sample(range(len(current_tour)), 2))
            neighbor_tour = current_tour[:i] + current_tour[i:j+1][::-1] + current_tour[j+1:]
            neighbor_cost = get_cost(neighbor_tour)
            
            # Cálculo do Delta
            delta = neighbor_cost - current_cost
            
            # Critério de Aceitação de Boltzmann
            if delta < 0 or random.random() < math.exp(-delta / T):
                current_tour = neighbor_tour
                current_cost = neighbor_cost
                
                if current_cost < best_cost:
                    best_tour = list(current_tour)
                    best_cost = current_cost
            
            T *= alpha  # Resfriamento geométrico
            
        return best_tour