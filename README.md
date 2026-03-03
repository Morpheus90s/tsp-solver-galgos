# 🦅 Desafio de Estágio - Laboratório Galgos (PUC-Rio)
## Solução para o Problema do Caixeiro-Viajante (TSP)

Este repositório contém a solução para o desafio técnico do Laboratório Galgos. O foco aqui não foi apenas "resolver o problema", mas construir um código organizado, fácil de ler e que respeite os padrões clássicos da TSPLib 95.


## Como o projeto foi estruturado (Metodologia)

Para auxiliar na estruturação e garantir que nenhum detalhe técnico fosse esquecido, foi configurado um Agente Personalizado (Gemini) como um "copiloto" de Otimização.

O agente foi alimentado com o manual da TSPLIB 95 e princípios de SOLID para auxiliar na manutenção do código modular. O Strategy Pattern foi utilizado porque, se no futuro for desejado testar um Algoritmo Genético ou um 2-Opt, não é necessário modificar o carregamento dos dados basta "conectar" a nova estratégia.

### Transparência: A conversa e como a IA foi usada para estruturar o projeto podem ser conferidas aqui: [https://gemini.google.com/gem/17yXkcExhtJ8oUPRXuFLd1SbL0A4Kjoro?usp=sharing]

## Desafios Encontrados

Nem tudo foi "cópia e cola". Um ponto interessante que surgiu foi o erro de indexação (Offset Mismatch):
- O Problema:A TSPLib conta as cidades a partir do 1 (1-based), mas o Python e o NumPy começam do 0.
- A Solução: Foi percebido que o código inicial gerava um `KeyError: 0`. Foi necessário intervir manualmente para mapear os IDs corretamente, garantindo que o cálculo da distância correspondesse ao oficial.


## Primeiros Resultados

Para o primeiro teste, foi utilizada a instância eil51 (51 cidades):


| Algoritmo | Distância | Ótimo (TSPLib) | Gap (%) |
| :--- | :--- | :--- | :--- |
| Nearest Neighbor | 511 | 426 | ~19,9% |

O que isso significa?
O resultado de 511 demonstra que o algoritmo "guloso" funciona, mas é "parcialmente cego": ele escolhe a cidade mais próxima no momento e acaba deixando arestas gigantescas para o final. Ter um Gap de quase 20% é o que motiva a implementar um refinamento (como o 2-Opt) no próximo passo.

## Uso de IA (O que foi feito e o que a IA fez)

Seguindo o edital, os papéis são:
- IA: Auxiliou com o "esqueleto" do código (boilerplate), sugestões de padrões de projeto e formatação deste README.
- Candidato: Fez a lógica de correção de bugs de indexação, validou os cálculos de distância (EUC_2D), analisou os resultados e tomou as decisões de arquitetura.

## Como executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Execute o script: `python3 main.py`
