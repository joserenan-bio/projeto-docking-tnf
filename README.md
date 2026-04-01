Projeto: Análise Genômica e Docking Molecular (TNF-Alpha)
Este repositório apresenta um fluxo completo de Bioinformática, integrando a análise de sequências genéticas (Genômica) com a simulação de interações moleculares (Docking).

🚀 Objetivo
Analisar a proteína TNF-Alpha (Fator de Necrose Tumoral Alfa) sob duas perspectivas:

Estrutural: Avaliar a afinidade de ligação com o ligante Curcumina.

Sequencial: Processar e alinhar sequências proteicas/genômicas para identificação de variantes.

🛠️ Tecnologias e Ferramentas
Linguagens: Python (BioPython, Pandas).

Docking: PyRx, AutoDock Vina, UCSF ChimeraX.

Sistema: WSL2 (Ubuntu), Anaconda.

Bioinformática: Alinhamento de sequências (Clustal/FASTA).

📂 Conteúdo do Repositório
alinhamento.fasta: Sequência primária da proteína em formato bruto.

alinhamento.aln: Resultado do alinhamento múltiplo de sequências.

analise_variantes.py: Script Python para automação da análise de dados genômicos.

1TNF.pdb & receptor_limpo.pdbqt: Estrutura da proteína preparada para o docking.

resultado_final.pdbqt: Resultado da simulação de acoplamento molecular.

🔬 Resultados Obtidos
O docking molecular demonstrou a interação da Curcumina com o sítio ativo da TNF-Alpha, com energias de afinidade que sugerem potencial inibitório. O fluxo de trabalho automatizado via Python permitiu a integração rápida entre os dados de sequenciamento e a modelagem estrutural.

👨‍🔬 Autor
José Renan Lima do Nascimento Biomédico e Pesquisador em Bioinformática.
