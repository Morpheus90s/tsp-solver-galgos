import matplotlib.pyplot as plt

def plot_tsp_comparison(problem, tour_nn, tour_2opt, dist_nn, dist_2opt):
    coords = problem.node_coords
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    tours = [tour_nn, tour_2opt]
    # Garantindo que dist_nn e dist_2opt sejam apenas o número
    titles = [f"NN ({dist_nn})", f"2-Opt ({dist_2opt})"]
    colors = ["red", "green"]

    for ax, tour, title, color in zip([ax1, ax2], tours, titles, colors):
        # Fecha o ciclo voltando para a primeira cidade
        path = tour + [tour[0]]
        
        # Extrai as coordenadas X e Y
        x = [coords[node][0] for node in path]
        y = [coords[node][1] for node in path]
        
        ax.plot(x, y, marker='o', color=color, linestyle='-', markersize=5)
        ax.set_title(title)
        ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    # No Codespaces, salvamos a imagem para ver no explorer lateral
    plt.savefig('comparison_plot.png')
    print("✅ Gráfico gerado com sucesso: comparison_plot.png")
    plt.close()
