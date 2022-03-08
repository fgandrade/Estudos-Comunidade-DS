# Carregando pacotes
import numpy as np
import pandas as pd

# Carregando base de DADOS
file_path = '/Users/felipe/Documents/repos/Estudos-Comunidade-DS/02-Python-Zero-DS/Mod-02/datasets/'
data = pd.read_csv(f'{file_path}kc_house_data.csv')

################################################################################################################################################################
#                               RESPONDENDO AS PERGUNTAS
################################################################################################################################################################

# # 1. Crie uma nova coluna chamada: "house_age"
# - Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house'
# - Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house'
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
data['house_age'] = data['date'].apply(lambda x : 'new_house' if x > pd.to_datetime('2014-01-01', format='%Y-%m-%d') else 'old_house')
data.head()

# # 2. Crie uma nova coluna chamada: "dormitory_type"
# - Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
# - Se o valor da coluna "bedrooms" for igual à 2 => 'apartment'
# - Se o valor da coluna "bedrooms" for maior que 2 => 'house'
data['bedrooms'].unique()

data['dormitory_type'] = data['bedrooms'].apply(lambda x: 'studio' if x == 1 else
                                                          'apartment' if x == 2 else
                                                          'house' if x > 2 else 'NA')
data.head()

# # 3. Crie uma nova coluna chamada: "condition_type"
# - Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
# - Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
# - Se o valor da coluna "condition" for igual â 5 => 'good'
data['condition'].unique()

data['condition_type'] = data['condition'].apply(lambda x: 'bad' if x <= 2 else
                                                           'regular' if (x == 3) | (x == 4) else 'good')
data.head()

# # 4. Modifique o TIPO da coluna "condition" para STRING
data['condition'].dtypes

data['condition'] = data['condition'].astype(str)
data['condition'].dtypes

# # 5. Delete as colunas: "sqft_living15" e "sqft_lot15"
data.columns

data = data.drop(columns=['sqft_living15', 'sqft_lot15'])
data.columns

# # 6. Modifique o TIPO da coluna "yr_built" para DATE
data['yr_built'] = pd.to_datetime(data['yr_built'], format='%Y')
data['yr_built']

# # 7. Modifique o TIPO da coluna "yr_renovated" para DATE
data['yr_renovated'].dtypes
data['yr_renovated'] = data['yr_renovated'].apply(lambda x: pd.to_datetime('1900-01-01', format='%Y-%m-%d') if x == 0
                                                       else pd.to_datetime(x, format='%Y'))

data['yr_renovated']

# # 8. Qual a data mais antiga de construção de um imóvel?
data['yr_built'].min()

# # 9. Qual a data mais antiga de renovação de um imóvel?
data.loc[data['yr_renovated'] > pd.to_datetime('1900-01-01', format='%Y-%m-%d'), 'yr_renovated'].min()

# # 10. Quantos imóveis tem 2 andares?
data.loc[data['floors'] == 2, 'id'].size

# # 11. Quantos imóveis estão com a condição igual a "regular" ?
data.loc[data['condition_type'] == 'regular', 'id'].size

# # 12. Quantos imóveis estão com a condição igual a "bad" e possuem "visita para água" ?
data.loc[(data['condition_type'] == 'bad') & (data['waterfront'] == 1), 'id'].size

# # 13. Quantos imóveis estão com a condição igual a "good" e são "new_house" ?
data.loc[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house'), 'id'].size

# # 14. Qual o valor do imóvel mais caro do tipo "studio" ?
data.loc[data['dormitory_type'] == 'studio', 'price'].max()

# # 15. Quantos imóveis do tipo "apartment" foram reformados em 2015?
data.loc[(data['yr_renovated'] == pd.to_datetime('2015-01-01')) & (data['dormitory_type'] == 'apartment'), 'id'].size

# # 16. Qual o maior número de quartos que imóveis do tipo "house" possuem ?
data.loc[data['dormitory_type'] == 'house', 'bedrooms'].max()

# # 17. Quantos imóveis "new_house" foram reformados no ano de 2014?
data.loc[(data['house_age'] == 'new_house') & (data['yr_renovated'] == pd.to_datetime('2014-01-01')), 'id'].size

# # 18. Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelos métodos:

# 18.1. Direto pelo nome das colunas
data[['id', 'date', 'price', 'floors', 'zipcode']]

# 18.2. Pelos índices
data.iloc[:, [0, 1, 2, 7, 16]]

# 18.3. Pelos índices das linhas e o nome das colunas
data.loc[:,['id', 'date', 'price', 'floors', 'zipcode']]

# 18.4. Índices booleanos
bools = [True, True, True, False, False, False, False, True, False, False, False,
        False, False, False, False, False, True, False,  False, False, False, False ]

data.loc[:, bools]

# # 19. Salve um arquivo .csv somente as colunas dos itens 10 ao 17.
data[['house_age', 'dormitory_type', 'condition_type']].to_csv(f'{file_path}resolucao_exercicio_02.csv')

# # 20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"
import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['#1C8356'], zoom=3, height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()

# salvando em html
# mapa.write_html('datasets/map_house_green.html')
