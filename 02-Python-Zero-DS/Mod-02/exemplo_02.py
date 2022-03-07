# carrega um arquivo do disco rígido para a
# memória
import pandas as pd
from numpy import int64

df = pd.read_csv('datasets/kc_house_data.csv')

# mostra na tela as primeiras 6 linhas
print(df.head(6))

# mostra na tela os tipos de variáveis em cada coluna
# primeira coisa e mais importante a se fazer
print(df.dtypes)

# ============================================
# COMO CONVERTER OS TIPOS DE VARIÁVEIS
# ============================================

# funcao que converte de object (string) -> date
df['date'] = pd.to_datetime(df['date'])
print(df['date'].dtypes)

# funcao que converte de inteiro -> float
df['bedrooms'] = df['bedrooms'].astype(float)
print(df['bedrooms'].dtypes)
print(df[['id', 'bedrooms']].head(3))

# funcao que converte de float -> int64
df['bedrooms'] = df['bedrooms'].astype(int64)
print(df['bedrooms'].dtypes)
print(df[['id', 'bedrooms']].head(3))

# funcao que converte de inteiro -> string
df['bedrooms'] = df['bedrooms'].astype(str)
print(df['bedrooms'].dtypes)
print(df[['id', 'bedrooms']].head(3))

# funcao que converte de string -> int64
df['bedrooms'] = df['bedrooms'].astype(int64)
print(df['bedrooms'].dtypes)
print(df[['id', 'bedrooms']].head(3))

# ------------------------------------------------- #

# ============================================
# CRIANDO NOVAS VARIÁVEIS
# ============================================

df = pd.read_csv('datasets/kc_house_data.csv')

# mostra as colunas existentes no dataset
print(df.columns)

# criando nova coluna a partir de um valor
df['nome_do_meigarom'] = 'meigarom'
df['comunidade_ds'] = 80
df['data_abertura_comunidade_ds'] = pd.to_datetime('2020-02-28')
print(df.columns)

print(df[['id', 'date', 'nome_do_meigarom', 'comunidade_ds',
         'data_abertura_comunidade_ds']].head())

print(df.dtypes)

# ============================================
# DELETANDO NOVAS VARIÁVEIS
# ============================================

# deletando uma coluna
print(df.columns)
df = df.drop('nome_do_meigarom', axis=1)
# axis=1   - deleta ao longo das colunas
print(df.columns)

# deletando mais de uma coluna
# 1° FORMA
df = df.drop(['comunidade_ds', 'data_abertura_comunidade_ds'],
             axis=1)
print(df.columns)

# 2° FORMA
cols = ['comunidade_ds', 'data_abertura_comunidade_ds']
df = df.drop(cols, axis=1)
print(df.columns)

# ============================================
# FORMAS DE SELECIONAR COLUNAS
# ============================================

# 01- Direto pelo nome das colunas

# apenas uma coluna
print(df['price'])

# mais de uma coluna
print(df[['price', 'id', 'date']])
cols = ['price', 'id', 'date']
print(df[cols])

# 02- Pelos indices das linhas e colunas
# DADOS[linhas, colunas]

# 10 primeiras linhas e 3 primeiras colunas'
print(df.iloc[0:10, 0:3])

# todas as linhas e as 3 primeiras colunas
print(df.iloc[:, 0:3])

# 5 primeiras linhas e todas as colunas
print(df.iloc[0:5, :])

# 03- Pelos indices das linhas e nome das colunas

# 10 primeiras linhas e somente uma coluna
print(df.loc[0:10, 'price'])

# mais de uma coluna
print(df.loc[0:10, ['price', 'id', 'date']])
cols = ['price', 'id', 'date']
print(df.loc[0:10, cols])

# 04- Indices booleanos
# 1 - True      0 - False

bools = [True, False, True, True, False, False, False, False,
         False, False, False, False, False, False, False,
         False, False, False, False, False, False, False,
         False, False]
print(df.loc[0:10, bools])

# ============================================
# RESPONDENDO AS PERGUNTAS DE NEGÓCIO
# ============================================

df = pd.read_csv('datasets/kc_house_data.csv')

# # 1. Qual a data do imóvel mais antigo no portfólio?
df['date'] = pd.to_datetime(df['date'])
print(df.sort_values('date', ascending=True))

# 2. Quantos imóveis possuem o número máximo de andares?
# print(df['floors'].unique())

print(df[df['floors'] == 3.5].shape)

# 3. Criar uma classificação para o imóveis, separando-os em baixo e alto padrão, de acordo com preço.
# acima de R$ 540.000 -> alto padrão (high_standard)
# abaixo de R$ 540.000 -> baixo padrão (low_standard)

df['level'] = 'standard'

df.loc[df['price'] > 540000, 'level'] = 'high_level'
df.loc[df['price'] < 540000, 'level'] = 'low_level'
# print(df.head())

# 4. Gostaria de um relatório ordenado pelo preço e contento as seguintes informações:
# ( id do imóvel, data que o imóvel ficou disponível para compra, o número de quartos, o tamanho total do terreno, o preço, a classificação do imóvel ( alto e baixo padrão ) )
report = df[['id', 'date', 'price', 'bedrooms', 'sqft_lot', 'level' ]].sort_values('price', ascending=False)

# print(report)

report.to_csv('datasets/report_aula02.csv', index=False)

# 5. Gostaria de um mapa indicando onde as casas estão localizadas geograficamente.

# Plotly - Biblioteca que armazena uma função que desenha mapa
# Scatter MapBox - Função que desenha um mapa
import plotly.express as px

data_mapa = df[['id', 'lat', 'long', 'price']]

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', hover_data=['price'], color_discrete_sequence=['fuchsia'], zoom=3, height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
mapa.show()

# salvando em html
mapa.write_html('datasets/map_house_rocket.html')
