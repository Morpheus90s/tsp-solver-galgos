# Registro de Interação e Tomada de Decisão com IA

Este documento registra os marcos da colaboração entre o candidato e o assistente de IA para o desafio do Laboratório Galgos.

## 1. Configuração de Ambiente e Rigor Matemático (nint)

**Usuário:** "Como devo tratar o cálculo de distância para o tipo EUC_2D para garantir que meu resultado bata com o ótimo oficial?"

**IA:** Explicou a importância da norma **nint** (Nearest Integer) da TSPLIB 95. O `nint` é vital para que o custo total da rota seja idêntico ao benchmark oficial. Sugeriu a biblioteca `tsplib95`.

## 2. Arquitetura de Software (Strategy Pattern)

**Usuário:** "Quero começar com uma Heurística do Vizinho Mais Próximo (Nearest Neighbor). Você pode sugerir uma implementação modular seguindo o Strategy Pattern?"

**IA:** Propôs uma estrutura baseada em classes abstratas (`TSPSolverStrategy`). 

- **Insight Técnico:** A IA destacou a natureza "míope" do algoritmo guloso e a complexidade $O(n^2)$. 

- **Decisão do Candidato:** A arquitetura adotada permite a evolução do projeto sem refatorar o carregamento de dados.

## 3. Identificação e Correção de Erro (Intervenção Humana)

**Usuário:** "Identifiquei um Bug de Indexação (Index Mismatch): as instâncias da TSPLIB utilizam IDs baseados em 1, enquanto a nossa matriz NumPy utiliza índices baseados em 0. Isso gerou um KeyError: 0."

**IA:** Reconheceu a discrepância de cardinalidade.

- **Resolução:** O erro foi corrigido manualmente no código do solver para mapear os IDs oficiais (1 a 51) para os índices da matriz (0 a 50). Esse momento foi crucial para garantir a integridade referencial do sistema.

## 4. Refinamento de Performance (SA Tuning)

**Usuário:** "O SA está parando em 441, igual ao 2-Opt. Fiz testes aumentando a temperatura e reduzindo o alpha."

**IA:** Sugeriu parâmetros de resfriamento mais lentos ($\alpha=0.9999$).

- **Resultado:** Após o tuning manual dos hiperparâmetros, foi possível "saltar" do ótimo local de 441 para o recorde de **432** (Gap de 1,4%).

## 5. Implementação da Estratégia de Refinamento (2-Opt)

**Usuário:** "Quero implementar a segunda fase: Melhoria Local com 2-Opt para 'descruzar' as arestas e diminuir a distância total."

**IA:** Propôs a classe `TwoOptStrategy` e explicou o conceito de **Inversão de Subsequência**.

- **Decisão Técnica:** Adotei a abordagem de **Algoritmo Híbrido**. Utilizei o resultado do Nearest Neighbor como entrada para o 2-Opt. Isso demonstra uma visão de pipeline de otimização (Construção -> Refinamento).

- **Insight de Defesa:** O 2-Opt foca em atingir um **Ótimo Local** (Local Optima), garantindo que não existam cruzamentos simples de arestas, o que reduziu o custo de 511 para 441.

## 6. Evolução para o Estado da Arte (Meta-heurística)

**Usuário:** "Vamos implementar o Simulated Annealing para tentar escapar de ótimos locais e chegar perto dos 426."

**IA:** Introduziu o conceito de **Recozimento Simulado** e a agitação térmica para exploração global.

- **Destaque de Engenharia:** A implementação foi integrada ao *Strategy Pattern* existente, permitindo uma comparação direta de performance entre as três abordagens no script `main.py`.

## 7. Justificativa das Escolhas Arquiteturais

**Usuário:** "Como posso resumir a 'Justificativa das Escolhas' para o Lab Galgos?"

**IA:** Destacou quatro pilares fundamentais:
1. **Conformidade Normativa:** Uso do padrão TSPLIB 95 para reprodutibilidade.
2. **SOLID (OCP):** Uso do Strategy Pattern para permitir que o sistema evolua sem alteração do núcleo.
3. **Pipeline de Otimização:** Estratégia de duas fases (Construção e Refinamento) como padrão ouro em P.O.
4. **Validação Empírica:** Uso de análise visual (Matplotlib) para comprovar a eficácia dos algoritmos.

## 8. Preparação para Defesa Técnica (Perguntas "Casca de Banana")

**Usuário:** "Quais perguntas técnicas podem surgir na entrevista?"

**IA:** Simulou cenários sobre a diferença entre **Ótimo Local** e **Ótimo Global**, e as nuances entre as políticas de aceitação de melhoria (**First Improvement** vs **Best Improvement**).

- **Aplicação Prática:** Esses conceitos foram utilizados para justificar por que o 2-Opt (determinístico) estacionou em 441 e como a natureza estocástica do Simulated Annealing permitiu buscar o recorde de 432.

## 9. Intuição por trás da Meta-heurística (SA)

**Usuário:** "Explique a intuição física (metalurgia) por trás do Simulated Annealing."

**IA:** Explicou a analogia do recozimento de metais e o **Critério de Metropolis/Boltzmann**.

- **Decisão do Candidato:** Implementar o resfriamento geométrico lento ($\alpha = 0.9999$) para dar ao algoritmo tempo de "congelar" na melhor configuração possível, atingindo um gap de apenas 1,4% em relação ao ótimo global.

## 10. Ciência de Dados Experimental e Hyperparameter Tuning

**Usuário:** "Rodei 3 vezes com o ajuste de T=500 e alpha=0.9999 e os resultados variaram (432, 441, 437). Como explicar que o 432 é um sucesso de engenharia?"

**IA:** Validou que essa oscilação é a prova real do funcionamento do **Critério de Metropolis**. 

- **Conclusão Técnica:** O sucesso de atingir um **Gap de 1,4%** foi atribuído ao equilíbrio entre *Exploration* e *Exploitation*. O ajuste fino dos hiperparâmetros permitiu que o algoritmo tivesse "energia" probabilística para saltar de ótimos locais onde buscas locais determinísticas (como o 2-Opt) ficariam retidas.
- **Rigor Científico:** A variação dos resultados foi documentada não como erro, mas como evidência da natureza estocástica da meta-heurística implementada.
