# Importando as bibliotecas necessárias
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_excel('Filtred_Data.txt')
print(df.head())

# Dataset com regiões e atributos demográficos
dataset_demografico = [
    ['Sudeste', 'Alta Renda', 'Idade Jovem'],
    ['Sul', 'Baixa Renda', 'Idade Idosa'],
    ['Norte', 'Média Renda', 'Idade Adulto'],
    ['Sudeste', 'Alta Renda', 'Idade Adulto'],
    ['Sul', 'Baixa Renda', 'Idade Jovem']
]

# Converter para DataFrame
df_demografico = pd.DataFrame(dataset_demografico, columns=['Região', 'Renda', 'Idade', 'Zona'])

# Lista de regiões presentes no seu dataset
regioes = df_demografico['Região'].unique()

# Dicionário para armazenar regras por região
regras_por_regiao = {}

for regiao in regioes:
    # Filtra os dados pela região atual
    df_filtrado = df_demografico[df_demografico['Região'] == regiao]
    
    # Prepara os dados para o Apriori
    dataset = df_filtrado.drop('Região', axis=1).values.tolist()
    
    # Transforma em matriz binária
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    
    # Calcula os itemsets frequentes
    frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
    
    # Gera as regras de associação
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    
    # Armazena as regras no dicionário
    regras_por_regiao[regiao] = rules

# Agora, você pode acessar as regras de cada região pelo dicionário
for regiao, regras in regras_por_regiao.items():
    print(f"Regras para a região {regiao}:\n", regras)

# Preparar os dados para o Apriori
dataset = df_filtrado.drop('Região', axis=1).values.tolist()

# Transformando os dados em uma matriz binária
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Calculando itemsets frequentes com suporte acima de 0.4
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# Gerando regras de associação com confiança mínima de 0.7
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Exibindo as regras
print(rules)
