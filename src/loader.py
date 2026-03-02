import tsplib95
import numpy as np

class TSPLoader:
    @staticmethod
    def load_matrix(file_path):
        """Carrega o arquivo .tsp e retorna a matriz de adjacência (EUC_2D)."""
        problem = tsplib95.load(file_path)
        nodes = list(problem.get_nodes())
        dimension = len(nodes)
        matrix = np.zeros((dimension, dimension))

        for i in range(dimension):
            for j in range(dimension):
                # Aplica o arredondamento oficial nint da TSPLib
                matrix[i][j] = problem.get_weight(nodes[i], nodes[j])
        
        return matrix, problem
