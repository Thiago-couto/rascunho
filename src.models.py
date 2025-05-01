import pandas as pd
from google.colab import files
from mlxtend.preprocessing import TransactionEncoder
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

print("Por favor, faça o upload do arquivo 'Filtred_Filename':")
uploaded_Filtred = files.upload()
Filtred_filename = list(uploaded_Filtred.keys())[0]
print(f"\nArquivo '{Filtred_filename}' carregado.")

# Carregar os dados
df = pd.read_csv(Filtred_filename, encoding='latin-1')

print(df.head())
print(f"Número de respostas carregadas: {len(df)}")
# Dataset com regiões e atributos demográficos
dataset_demografico = [
   ['Região', 'Faixa Etária', 'Faixa Salarial'],
    ['Sul', '17-24', '0-2.000'],
    ['Sul', '25-29', '0-2.000'],
    ['Sul', '30-34', '0-2.000'],
    ['Sul', '35-39', '0-2.000'],
    ['Sul', '40-44', '0-2.000'],
    ['Sul', '45-49', '0-2.000'],
    ['Sul', '50+', '0-2.000'],
    ['Sul', '17-24', '2.001-6.000'],
    ['Sul', '25-29', '2.001-6.000'],
    ['Sul', '30-34', '2.001-6.000'],
    ['Sul', '35-39', '2.001-6.000'],
    ['Sul', '40-44', '2.001-6.000'],
    ['Sul', '45-49', '2.001-6.000'],
    ['Sul', '50+', '2.001-6.000'],
    ['Sul', '17-24', '6.001-12.000'],
    ['Sul', '25-29', '6.001-12.000'],
    ['Sul', '30-34', '6.001-12.000'],
    ['Sul', '35-39', '6.001-12.000'],
    ['Sul', '40-44', '6.001-12.000'],
    ['Sul', '45-49', '6.001-12.000'],
    ['Sul', '50+', '6.001-12.000'],
    ['Sul', '17-24', '12.001-20.000'],
    ['Sul', '25-29', '12.001-20.000'],
    ['Sul', '30-34', '12.001-20.000'],
    ['Sul', '35-39', '12.001-20.000'],
    ['Sul', '40-44', '12.001-20.000'],
    ['Sul', '45-49', '12.001-20.000'],
    ['Sul', '50+', '12.001-20.000'],
    ['Sul', '17-24', '20.001+'],
    ['Sul', '25-29', '20.001+'],
    ['Sul', '30-34', '20.001+'],
    ['Sul', '35-39', '20.001+'],
    ['Sul', '40-44', '20.001+'],
    ['Sul', '45-49', '20.001+'],
    ['Sul', '50+', '20.001+'],
    ['Sudeste', '17-21', '0-2.000'],
    ['Sudeste', '25-29', '0-2.000'],
    ['Sudeste', '30-34', '0-2.000'],
    ['Sudeste', '35-39', '0-2.000'],
    ['Sudeste', '40-44', '0-2.000'],
    ['Sudeste', '45-49', '0-2.000'],
    ['Sudeste', '50+', '0-2.000'],
    ['Sudeste', '17-21', '2.001-6.000'],
    ['Sudeste', '25-29', '2.001-6.000'],
    ['Sudeste', '30-34', '2.001-6.000'],
    ['Sudeste', '35-39', '2.001-6.000'],
    ['Sudeste', '40-44', '2.001-6.000'],
    ['Sudeste', '45-49', '2.001-6.000'],
    ['Sudeste', '50+', '2.001-6.000'],
    ['Sudeste', '17-21', '6.001-12.000'],
    ['Sudeste', '25-29', '6.001-12.000'],
    ['Sudeste', '30-34', '6.001-12.000'],
    ['Sudeste', '35-39', '6.001-12.000'],
    ['Sudeste', '40-44', '6.001-12.000'],
    ['Sudeste', '45-49', '6.001-12.000'],
    ['Sudeste', '50+', '6.001-12.000'],
    ['Sudeste', '17-21', '12.001-16.000'],
    ['Sudeste', '25-29', '12.001-16.000'],
    ['Sudeste', '30-34', '12.001-16.000'],
    ['Sudeste', '35-39', '12.001-16.000'],
    ['Sudeste', '40-44', '12.001-16.000'],
    ['Sudeste', '45-49', '12.001-16.000'],
    ['Sudeste', '50+', '12.001-16.000'],
    ['Sudeste', '17-21', '16.001-20.000'],
    ['Sudeste', '25-29', '16.001-20.000'],
    ['Sudeste', '30-34', '16.001-20.000'],
    ['Sudeste', '35-39', '16.001-20.000'],
    ['Sudeste', '40-44', '16.001-20.000'],
    ['Sudeste', '45-49', '16.001-20.000'],
    ['Sudeste', '50+', '16.001-20.000'],
    ['Norte', '17-21', '0-2000'],
    ['Norte', '25-29', '0-2000'],
    ['Norte', '30-34', '0-2000'],
    ['Norte', '35-39', '0-2000'],
    ['Norte', '40-44', '0-2000'],
    ['Norte', '45-49', '0-2000'],
    ['Norte', '50+', '0-2000'],
    ['Norte', '17-21', '2.001-6.000'],
    ['Norte', '25-29', '2.001-6.000'],
    ['Norte', '30-34', '2.001-6.000'],
    ['Norte', '35-39', '2.001-6.000'],
    ['Norte', '40-44', '2.001-6.000'],
    ['Norte', '45-49', '2.001-6.000'],
    ['Norte', '50+', '2.001-6.000'],
    ['Norte', '17-21', '6.001-12.000'],
    ['Norte', '25-29', '6.001-12.000'],
    ['Norte', '30-34', '6.001-12.000'],
    ['Norte', '35-39', '6.001-12.000'],
    ['Norte', '40-44', '6.001-12.000'],
    ['Norte', '45-49', '6.001-12.000'],
    ['Norte', '50+', '6.001-12.000'],
    ['Norte', '17-21', '12.001-20.000'],
    ['Norte', '25-29', '12.001-20.000'],
    ['Norte', '30-34', '12.001-20.000'],
    ['Norte', '35-39', '12.001-20.000'],
    ['Norte', '40-44', '12.001-20.000'],
    ['Norte', '45-49', '12.001-20.000'],
    ['Norte', '50+', '12.001-20.000'],
    ['Norte', '17-21', '20.001+'],
    ['Norte', '25-29', '20.001+'],
    ['Norte', '30-34', '20.001+'],
    ['Norte', '35-39', '20.001+'],
    ['Norte', '40-44', '20.001+'],
    ['Norte', '45-49', '20.001+'],
    ['Norte', '50+', '20.001+'],
    ['Centro-oeste', '17-21', '0-2.000'],
    ['Centro-oeste', '25-29', '0-2.000'],
    ['Centro-oeste', '30-34', '0-2.000'],
    ['Centro-oeste', '35-39', '0-2.000'],
    ['Centro-oeste', '40-44', '0-2.000'],
    ['Centro-oeste', '45-49', '0-2.000'],
    ['Centro-oeste', '50+', '0-2.000'],
    ['Centro-oeste', '17-21', '2.001-6.000'],
    ['Centro-oeste', '25-29', '2.001-6.000'],
    ['Centro-oeste', '30-34', '2.001-6.000'],
    ['Centro-oeste', '35-39', '2.001-6.000'],
    ['Centro-oeste', '40-44', '2.001-6.000'],
    ['Centro-oeste', '45-49', '2.001-6.000'],
    ['Centro-oeste', '50+', '2.001-6.000'],
    ['Centro-oeste', '17-21', '6.001-12.000'],
    ['Centro-oeste', '25-29', '6.001-12.000'],
    ['Centro-oeste', '30-34', '6.001-12.000'],
    ['Centro-oeste', '35-39', '6.001-12.000'],
    ['Centro-oeste', '40-44', '6.001-12.000'],
    ['Centro-oeste', '45-49', '6.001-12.000'],
    ['Centro-oeste', '50+', '6.001-12.000'],
    ['Centro-oeste', '17-21', '12.001-20.000'],
    ['Centro-oeste', '25-29', '12.001-20.000'],
    ['Centro-oeste', '30-34', '12.001-20.000'],
    ['Centro-oeste', '35-39', '12.001-20.000'],
    ['Centro-oeste', '40-44', '12.001-20.000'],
    ['Centro-oeste', '45-49', '12.001-20.000'],
    ['Centro-oeste', '50+', '12.001-20.000'],
    ['Centro-oeste', '17-21', '20.001+'],
    ['Centro-oeste', '25-29', '20.001+'],
    ['Centro-oeste', '30-34', '20.001+'],
    ['Centro-oeste', '35-39', '20.001+'],
    ['Centro-oeste', '40-44', '20.001+'],
    ['Centro-oeste', '45-49', '20.001+'],
    ['Centro-oeste', '50+', '20.001+'],
    ['Nordeste', '17-21', '0-2000'],
    ['Nordeste', '22-24', '0-2000'],
    ['Nordeste', '25-29', '0-2000'],
    ['Nordeste', '30-34', '0-2000'],
    ['Nordeste', '35-39', '0-2000'],
    ['Nordeste', '40-44', '0-2000'],
    ['Nordeste', '45-49', '0-2000'],
    ['Nordeste', '17-21', '2.001-6.000'],
    ['Nordeste', '22-24', '2.001-6.000'],
    ['Nordeste', '25-29', '2.001-6.000'],
    ['Nordeste', '30-34', '2.001-6.000'],
    ['Nordeste', '35-39', '2.001-6.000'],
    ['Nordeste', '40-44', '2.001-6.000'],
    ['Nordeste', '45-49', '2.001-6.000'],
    ['Nordeste', '17-21', '6.001-12.000'],
    ['Nordeste', '22-24', '6.001-12.000'],
    ['Nordeste', '25-29', '6.001-12.000'],
    ['Nordeste', '30-34', '6.001-12.000'],
    ['Nordeste', '35-39', '6.001-12.000'],
    ['Nordeste', '40-44', '6.001-12.000'],
    ['Nordeste', '45-49', '6.001-12.000'],
    ['Nordeste', '17-21', '12.001-20.000'],
    ['Nordeste', '22-24', '12.001-20.000'],
    ['Nordeste', '25-29', '12.001-20.000'],
    ['Nordeste', '30-34', '12.001-20.000'],
    ['Nordeste', '35-39', '12.001-20.000'],
    ['Nordeste', '40-44', '12.001-20.000'],
    ['Nordeste', '45-49', '12.001-20.000'],
    ['Nordeste', '17-21', '20.001+'],
    ['Nordeste', '22-24', '20.001+'],
    ['Nordeste', '25-29', '20.001+'],
    ['Nordeste', '30-34', '20.001+'],
    ['Nordeste', '35-39', '20.001+'],
    ['Nordeste', '40-44', '20.001+'],
    ['Nordeste', '45-49', '20.001+'], 
]
df_demografico = pd.DataFrame(dataset_demografico, columns=['Região', 'Faixa Etária', 'Faixa Salarial'])

# Dividir os dados em treino e teste (por exemplo, 70% treino, 30% teste)
train_df, test_df = train_test_split(df_demografico, test_size=0.3, random_state=42)

# Função para processar os dados e gerar regras
def processar_regras(df_dados):
    dataset = df_dados.drop('Região', axis=1).values.tolist()
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df_transformed = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df_transformed, min_support=0.07, use_colnames=True)
    regras = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    return regras

# Processar dados de treino
regras_treino = processar_regras(train_df)

# Processar dados de teste para validação
regras_teste = processar_regras(test_df)

# Visualizar as regras (exemplo)
print("Regras de treino:\n", regras_treino)
print("Regras de teste:\n", regras_teste)

# Resumo, Grafico simples de fluxo
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Desenhar caixas e setas
ax.text(0.1, 0.8, 'Carregar Dados', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightblue"))
ax.text(0.1, 0.6, 'Dividir em Treino/Teste', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightgreen"))
ax.text(0.1, 0.4, 'Processar Regras\ncom Apriori', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow"))
ax.text(0.1, 0.2, 'Visualizar Resultados', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightcoral"))

contagem = df_demografico.groupby(['Região', 'Faixa Etária', 'Faixa Salarial']).size().reset_index(name='Quantidade')

# Para facilitar a visualização, podemos criar uma tabela pivot
pivot_table = contagem.pivot_table(
    index='Região',
    columns=['Faixa Etária', 'Faixa Salarial'],
    values='Quantidade',
    fill_value=0
)
# Plotar o gráfico de barras empilhadas
pivot_table.plot(kind='bar', stacked=True, figsize=(12,8))

plt.title('Densidade Demográfica de Cientistas de Dados por Região, Faixa Etária e Faixa Salarial')
plt.xlabel('Região')
plt.ylabel('Número de Cientistas de Dados')
plt.legend(title='Faixa Etária / Faixa Salarial', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
