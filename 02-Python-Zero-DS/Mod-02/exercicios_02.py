# carregando Bibliotecas necessárias para o programa
import pandas as pd
import numpy as np

# importando conjunto de DADOS
# disponível em: https://www.kaggle.com/harlfoxem/housesalesprediction
data = pd.read_csv('datasets/kc_house_data.csv')


# 1. Crie uma nova coluna chamada: "house_age"
# - Se o valor da coluna "date" for maior que 2014-01-01 => 'new_house'
# - Se o valor da coluna "date" for menor que 2014-01-01 => 'old_house'
#
data['date'] = pd.to_datetime(data['date'])
data['house_age'] = 'house'
# print(data)

data.loc[data['date'] > '2014-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age'] = 'old_house'
# print(data.sort_values('date', ascending=True))
# print(data['house_age'].unique())


# 2. Crie uma nova coluna chamada: "dormitory_type"
# - Se o valor da coluna "bedrooms" for igual à 1 => 'studio'
# - Se o valor da coluna "bedrooms" for igual à 2 => 'apartment'
# - Se o valor da coluna "bedrooms" for maior que 2 => 'house'
#
data['dormitory_type'] = 'dormitory'
# print(data.dtypes)

data.loc[(data['bedrooms'] != 1) & ( data['bedrooms'] != 2) & ( data['bedrooms'] < 2), 'dormitory_type'] = ''
data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartment'
data.loc[data['bedrooms'] > 2, 'dormitory_type'] = 'house'
# print(data)
# print(data['dormitory_type'].unique())
# print(data.loc[data['dormitory_type'] == 'house', ['bedrooms', 'dormitory_type']].sort_values('bedrooms', ascending=True))


# 3. Crie uma nova coluna chamada: "condition_type"
# - Se o valor da coluna "condition" for menor ou igual à 2 => 'bad'
# - Se o valor da coluna "condition" for igual à 3 ou 4 => 'regular'
# - Se o valor da coluna "condition" for igual â 5 => 'good'
#
data['condition_type'] = 'condition'
# print(data.dtypes)

data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
data.loc[(data['condition'] == 3) | (data['condition'] == 4), 'condition_type'] = 'regular'
data.loc[data['condition'] == 5, 'condition_type'] = 'good'
# print(data.loc[:, ['condition', 'condition_type']].sort_values('condition', ascending=True))
# print(data['condition_type'].unique())


# 4. Modifique o TIPO da coluna "condition" para STRING
#
# print(data['condition'].dtypes)
data['condition'] = data['condition'].astype(str)
# print(data['condition'].dtypes)


# 5. Delete as colunas: "sqft_living15" e "sqft_lot15"
#
# print(data.columns)
cols = ['sqft_living15', 'sqft_lot15']
data = data.drop(cols, axis=1)
# print(data.columns)


# 6. Modifique o TIPO da coluna "yr_built" para DATE
#
# print(data['yr_built'].dtypes)

data['yr_built_date'] = data['yr_built'].astype(str) + "-01-01"
data['yr_built_date'] = pd.to_datetime(data['yr_built_date'])
# print(data['yr_built_date'].sort_values('yr_built_date', ascending=False))
# print(data['yr_built_date'].unique())

# print(data['yr_built_date'].dtypes)


# 7. Modifique o TIPO da coluna "yr_renovated" para DATE
#
# print(data['yr_renovated'].dtypes)

data.loc[data['yr_renovated'] == 0, 'yr_renovated'] = 2999
data['yr_renovated_date'] = data['yr_renovated'].astype(str) + "-01-01"
data['yr_renovated_date'] = pd.to_datetime(data['yr_renovated_date'], errors='coerce')
# print(data['yr_renovated_date'])
# print(data['yr_renovated_date'].unique())

# print(data['yr_renovated_date'].dtypes)


# 8. Qual a data mais antiga de construção de um imóvel?
#
antiga = data.sort_values('yr_built', ascending=True).head(1)
# print(antiga['yr_built'].to_string(index=False))


# 9. Qual a data mais antiga de renovação de um imóvel?
#
renovada = data.sort_values('yr_renovated', ascending=True).head(1)
# print(renovada['yr_renovated'].to_string(index=False))


# 10. Quantos imóveis tem 2 andares?
#
dois_andares = data.loc[data['floors'] == 2]
# print(dois_andares.shape)
# print(dois_andares['id'].count())

# data['two_floors'] = dois_andares['id'].count()
# print(data)


# 11. Quantos imóveis estão com a condição igual a "regular" ?
#
regular = data.loc[data['condition_type'] == 'regular']
# print(regular['id'].shape)
# print(regular['id'].count())

data['condition_regular'] = regular['id'].count()
# print(data)


# 12. Quantos imóveis estão com a condição igual a "bad" e possuem "visita para água" ?
#
bad_waterfront = data.loc[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)]
# print(bad_waterfront.shape)
# print(bad_waterfront['id'].count())

data['bad_waterfront'] = bad_waterfront['id'].count()
# print(data)


# 13. Quantos imóveis estão com a condição igual a "good" e são "new_house" ?
#
good_new_house = data.loc[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')]
# print(good_new_house.shape)
# print(good_new_house['id'].count())

data['good_new_house'] = good_new_house['id'].count()
# print(data)


# 14. Qual o valor do imóvel mais caro do tipo "studio" ?
#
studio = data.loc[data['dormitory_type'] == 'studio'].sort_values('price', ascending=False).head(1)


data['studio'] = studio['price'].to_string(index=False)

# print(data)


# 15. Quantos imóveis do tipo "apartment" foram reformados em 2015?
#
# print(data[['dormitory_type', 'yr_renovated']])

apartment_2015 = data.loc[(data['dormitory_type'] == 'apartment') & (data['yr_renovated'] == 2015)]
# print(apartment_2015.shape)
# print(apartment_2015['id'].count())

data['apartment_2015'] = apartment_2015['id'].count()
# print(data)


# 16. Qual o maior número de quartos que imóveis do tipo "house" possuem ?
#
house_bedrooms = data.loc[data['dormitory_type'] == 'house'].sort_values('bedrooms', ascending=False).head(1)
data['house_bedrooms'] = house_bedrooms['bedrooms'].to_string(index=False)

# print(data)


# 17. Quantos imóveis "new_house" foram reformados no ano de 2014?
#
new_house_2014 = data.loc[(data['house_age'] == 'new_house') & (data['yr_renovated'] == 2014)]

# print(new_house_2014[['house_age', 'yr_renovated']])
# print(new_house_2014.shape)

data['new_house_2014'] = new_house_2014['id'].count()
# print(data)


# 18. Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelos métodos:
#
# 18.1. Direto pelo nome das colunas
cols = ["id", "date", "price", "floors", "zipcode"]
# print(data[cols])

# 18.2. Pelos índices
# print(data.columns)

# print(data.iloc[:, [0, 1, 2, 7, 16]])

# 18.3. Pelos índices das linhas e o nome das colunas
cols = ["id", "date", "price", "floors", "zipcode"]
# print(data.loc[:, cols])

# 18.4. Índices booleanos
bools = [ True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False,  False, False, False, False, False, False, False, False, False, False, False, False, False, False ]

# print(data.loc[:, bools])


# 19. Salve um arquivo .csv somente as colunas dos itens 10 ao 17.
#
# print(data.iloc[:1, -1:-9:-1])
data.iloc[:1, -1:-9:-1].to_csv('datasets/exercise_02.csv', index=False)


# 20. Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"

# Plotly - Biblioteca que armazena uma função que desenha mapa
# Scatter MapBox - Função que desenha um mapa
import plotly.express as px

data_mapa = data[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['#1C8356'], zoom=3, height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
# mapa.show()

# salvando em html
mapa.write_html('datasets/map_house_green.html')
