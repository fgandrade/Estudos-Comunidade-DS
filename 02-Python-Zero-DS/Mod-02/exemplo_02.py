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












