skirt = {'size': 'M', 'price': 139.90, 'color': 'black'}
skirt

skirt = {'size': 'M', 'price': 139.90, 'color': 'black', 'date': '2020-01-01'}
skirt

skirt = {'size': 'M', 'price': 139.90, 'color': ['black', 'red', 'blue'], 'date': '2020-01-01'}
skirt

skirt['size']
skirt['price']
skirt['color'][0]
skirt['color'][1]
skirt['color'][2]

##############################################################################
#                               AGRUPAMENTO                                  #
##############################################################################
import pandas as pd

file_path = '/Users/felipe/Documents/repos/Estudos-Comunidade-DS/02-Python-Zero-DS/Mod-03/datasets'

df = pd.read_csv(f'{file_path}/kc_house_data.csv')
df.head()

# Quantos imóveis existem por número de quartos?
df[['id', 'bedrooms']].groupby('bedrooms').size()

df_grouped = df[['id', 'bedrooms']].groupby('bedrooms')

for bedrooms, frame in df_grouped:
    print('número de quartos: {}'.format(bedrooms))
    print(frame.shape, end='\n\n')


##############################################################################
#                       RESPONDENDO AS PERGUNTAS DO CEO                      #
##############################################################################
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x)

file_path = '/Users/felipe/Documents/repos/Estudos-Comunidade-DS/02-Python-Zero-DS/Mod-03/datasets'

df = pd.read_csv(f'{file_path}/kc_house_data.csv')
df.head()

# # 1. Qual o número de imóveis por ano de construção?
df[['id', 'yr_built']].groupby('yr_built').count()

# # 2. Qual o menor número de quartos por ano de construção de imóveis?
df[['bedrooms', 'yr_built']].groupby('yr_built').min()

# # 3. Qual o preço de compra mais alto por cada número de quarto?
df[['price', 'bedrooms']].groupby('bedrooms').max()

# # 4. Qual a soma de todos os preços de compra por número de quartos?
df[['price', 'bedrooms']].groupby('bedrooms').sum()

# # 5. Qual a soma de todos os preços de compra por número de quartos e banheiros?
df[['price', 'bedrooms', 'bathrooms']].groupby(['bedrooms', 'bathrooms']).sum()

# # 6. Qual o tamanho médio das salas dos imóveis por ano de construção?
df[['sqft_living', 'yr_built']].groupby('yr_built').mean()

# # 7. Qual o tamanho mediano das salas dos imóveis por ano de construção?
df[['sqft_living', 'yr_built']].groupby('yr_built').median()

# # 8. Qual o desvio-padrão do tamanho das salas dos imóveis por ano de construção?
df[['sqft_living', 'yr_built']].groupby('yr_built').std()

# # 9. Como é o crescimento médio de preços de compras dos imóveis por ano, por dia e pela semana do ano?

# Crescimento total de preços de compras de imóveis por ano
# Eixo X: Anos
# Eixo Y: Soma dos preços
# Gráfico: Barras

# First graph
from matplotlib import pyplot as plt

df['year'] = pd.to_datetime(df['date']).dt.year
df.head()

df[['price', 'year']].groupby('year').sum().reset_index()

by_year = df[['price', 'year']].groupby('year').sum().reset_index()
plt.figure(figsize=(20, 12))
plt.bar(by_year['year'], by_year['price'])

# Second graph
df['day'] = pd.to_datetime(df['date'])
by_day = df[['price', 'day']].groupby('day').mean().reset_index()

plt.figure(figsize=(20, 12))
plt.plot(by_day['day'], by_day['price'])

# Third graph
df['year_week'] = pd.to_datetime(df['date']).dt.strftime('%Y-%U')
by_week_year = df[['price', 'year_week']].groupby('year_week').mean().reset_index()

plt.figure(figsize=(20, 12))
plt.plot(by_week_year['year_week'], by_week_year['price'])
plt.xticks(rotation=60);


## Dashboard
from matplotlib import gridspec

fig = plt.figure(figsize=(20, 12))
specs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

ax1 = fig.add_subplot(specs[0,:]) # First Row - All Colums
ax2 = fig.add_subplot(specs[1,0]) # Second Row - First Colum
ax3 = fig.add_subplot(specs[1,1]) # Second Row - Second Colum

# First graph
df['year'] = pd.to_datetime(df['date']).dt.year
by_year = df[['price', 'year']].groupby('year').sum().reset_index()

ax1.bar(by_year['year'], by_year['price'])

# Second graph
df['day'] = pd.to_datetime(df['date'])
by_day = df[['price', 'day']].groupby('day').mean().reset_index()

ax2.plot(by_day['day'], by_day['price'])

# Third graph
df['year_week'] = pd.to_datetime(df['date']).dt.strftime('%Y-%U')
by_week_year = df[['price', 'year_week']].groupby('year_week').mean().reset_index()

ax3.plot(by_week_year['year_week'], by_week_year['price'])
plt.xticks(rotation=80);

# # 10. Eu gostaria de olhar no mapa e conseguir identificar as casas com maior preço
import plotly.express as px

houses = df[['id', 'lat', 'long', 'price']]

fig = px.scatter_mapbox(houses, lat='lat', lon='long', size='price', color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)

fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
fig.show()
