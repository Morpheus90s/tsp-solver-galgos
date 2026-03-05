from src.loader import TSPLoader
from src.strategies import NearestNeighborStrategy, TwoOptStrategy, SimulatedAnnealingStrategy
from src.visualizer import plot_tsp_comparison
import numpy as np

def run_experiment(instance_path, num_runs):
    # 0. Carregamento dos Dados
    matrix, problem = TSPLoader.load_matrix(instance_path)
    
    # 1. Construção (Nearest Neighbor)
    nn_solver = NearestNeighborStrategy()
    tour_nn = nn_solver.solve(matrix)
    dist_nn = int(problem.trace_tours([tour_nn])[0])

    # 2. Refinamento (2-Opt)
    two_opt_solver = TwoOptStrategy()
    tour_2opt = two_opt_solver.solve(matrix, initial_tour=tour_nn)
    dist_2opt = int(problem.trace_tours([tour_2opt])[0])

    # 3. Meta-heurística (Simulated Annealing) com Múltiplas Rodadas
    sa_solver = SimulatedAnnealingStrategy()
    sa_results = []
    best_tour_sa = None
    best_dist_sa = float('inf')

    print(f"\n--- Iniciando Experimentos (Instância: {problem.name}) ---")
    print(f"Baseline NN: {dist_nn}")
    print(f"Refinamento 2-Opt: {dist_2opt}")
    print(f"Executando Simulated Annealing ({num_runs}x)...")

    for i in range(num_runs):
        tour_sa = sa_solver.solve(matrix, initial_tour=tour_2opt, T_start=500.0, alpha=0.9999)
        dist_sa = int(problem.trace_tours([tour_sa])[0])
        sa_results.append(dist_sa)
        
        if dist_sa < best_dist_sa:
            best_dist_sa = dist_sa
            best_tour_sa = tour_sa
        print(f"  > Rodada {i+1}: {dist_sa}")

    avg_sa = np.mean(sa_results)

       # 4. Resultados Finais e Geração do Log
    log_content = (
        f"--- RELATÓRIO DE EXPERIMENTOS (Instância: {problem.name}) ---\n"
        f"Nearest Neighbor : {dist_nn}\n"
        f"Refinamento 2-Opt: {dist_2opt}\n"
        f"Execuções SA ({num_runs}x): {sa_results}\n"
        f"SA (Melhor)      : {best_dist_sa}\n"
        f"SA (Média)       : {avg_sa:.2f}\n"
        f"========================================\n"
    )

    print("\n" + log_content)

    # SALVANDO NO ARQUIVO (Isso garante que não saia vazio)
    with open("results/experiment_log.txt", "w") as f:
        f.write(log_content)
    print(f"Log salvo em: results/experiment_log.txt")

    # 5. Visualização
    plot_tsp_comparison(problem, tour_nn, best_tour_sa, dist_nn, best_dist_sa)


if __name__ == "__main__":
    run_experiment("data/eil51.tsp", 10)
