import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_excel('Filtred_Data.xlsx')
print(df.head())

# Dataset com regiões e atributos demográficos
dataset_demografico = [
    ['Sudeste', 'Alta Renda', 'Idade Jovem'],
    ['Sul', 'Baixa Renda', 'Idade Idosa'],
    ['Norte', 'Média Renda', 'Idade Adulto'],
    ['Sudeste', 'Alta Renda', 'Idade Adulto'],
    ['Sul', 'Baixa Renda', 'Idade Jovem']
]

df_demografico = pd.DataFrame(dataset_demografico, columns=['Região', 'Renda', 'Idade'])

# Dividir os dados em treino e teste (por exemplo, 70% treino, 30% teste)
train_df, test_df = train_test_split(df_demografico, test_size=0.3, random_state=42)

# Função para processar os dados e gerar regras
def processar_regras(df_dados):
    dataset = df_dados.drop('Região', axis=1).values.tolist()
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df_transformed = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df_transformed, min_support=0.4, use_colnames=True)
    regras = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    return regras

# Processar dados de treino
regras_treino = processar_regras(train_df)

# Processar dados de teste para validação
regras_teste = processar_regras(test_df)

# Visualizar as regras (exemplo)
print("Regras de treino:\n", regras_treino)
print("Regras de teste:\n", regras_teste)

# Resultado, Grafico simples
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Desenhar caixas e setas
ax.text(0.1, 0.8, 'Carregar Dados', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightblue"))
ax.text(0.1, 0.6, 'Dividir em Treino/Teste', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightgreen"))
ax.text(0.1, 0.4, 'Processar Regras\ncom Apriori', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow"))
ax.text(0.1, 0.2, 'Visualizar Resultados', fontsize=12, bbox
