# importe o conjunto de dados chamado kc_house_data.csv do HD para memória
import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# mostre na tela as 5 primeiras linhas do conjunto de dados
print(data.head())

# mostre na tela o numero de colunas e numero de linhas do dataset
print(data.shape)

# mostre na tela o nome das colunas do conjunto de dados
print(data.columns)

# mostre na tela o conjunto de dados ordenados pela coluna price
print(data.sort_values('price'))
print(data[['id', 'price']].sort_values('price'))

# mostre na tela o conjunto de dados ordenados pela coluna price do
# maior para o menor
print(data[['id', 'price']].sort_values('price', ascending=False))