#  Desafio de Estágio - Laboratório Galgos (PUC-Rio)
## Solução para o Problema do Caixeiro-Viajante (TSP)

Este repositório contém a solução para o desafio técnico do **Laboratório Galgos**. O foco foi construir um código modular, organizado e que respeite os padrões clássicos da **TSPLib 95**.

---

## Metodologia e Estrutura

Para garantir o rigor técnico, configurei um **Agente Personalizado (Gemini)** como copiloto, alimentado com o manual da TSPLib e princípios de **SOLID**.

Utilizei o **Strategy Pattern** para permitir a troca fácil entre algoritmos. Isso significa que o carregamento dos dados é independente da lógica de resolução, permitindo escalabilidade para novos métodos.

> **Transparência:** A conversa e o uso da IA para estruturar o projeto podem ser conferidos aqui: [https://gemini.google.com/gem/17yXkcExhtJ8oUPRXuFLd1SbL0A4Kjoro?usp=sharing]

---

## Evolução dos Resultados (Instância eil51)


| Algoritmo | Distância | Ótimo (TSPLib) | Gap (%) |
| :--- | :--- | :--- | :--- |
| Nearest Neighbor (Baseline) | 511 | 426 | ~19,9% |
| **Nearest Neighbor + 2-Opt** | **441** | 426 | **~3,5%** |

### Análise Crítica
A transição do **Nearest Neighbor** (Algoritmo Construtivo) para o **2-Opt** (Busca Local) reduziu o custo em **13,7%**.
- O **NN** é "míope": escolhe o vizinho mais próximo e deixa arestas longas para o final.
- O **2-Opt** refinou a rota, mas estacionou em **441** por ter atingido um **Ótimo Local**: uma solução onde nenhuma troca simples de duas arestas melhora o caminho. Escapar desse vale exigiria técnicas como *Simulated Annealing*.

---

## Desafios Técnicos: O "Erro de Ouro"

Durante a implementação, identifiquei um **Indexing Offset Mismatch**:
- **O Problema:** `IndexError: index 51 out of bounds`. As instâncias da TSPLib são *1-based*, enquanto o NumPy é *0-based*.
- **A Solução:** Intervi manualmente no código sugerido pela IA para implementar uma normalização de índices. Esse ajuste garantiu que a busca local acessasse os pesos corretos da matriz sem quebrar a execução.

---

## Divisão de Papéis (IA e Candidato)
- **IA:** Auxiliou com o "esqueleto" (boilerplate), sugestão de padrões de projeto e revisão de normas técnicas.
- **Candidato:** Lógica de correção de indexação, validação dos cálculos de distância (EUC_2D), análise de GAP e decisões de arquitetura.

---

## Como executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o script: `python3 main.py`
