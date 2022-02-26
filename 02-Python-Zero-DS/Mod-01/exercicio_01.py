# importe o conjunto de dados chamado kc_house_data.csv do HD para memória
import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')

# 1. Quantas casas estão disponíveis para compra?
print(f'1. Quantas casas estão disponíveis para compra? \n'
      f' R: {data["id"].nunique()} casas.')

# 2. Quantos atributos as casas possuem?
print(f'2. Quantos atributos as casas possuem? \n'
      f'R: {len(data.columns)} atributos.')

# 3. Quais são os atributos das casas?
print(f'3. Quais são os atributos das casas? \n'
      f'R: Os atributos são: {list(data.columns)}.')

# 4. Qual a casa mais cara (casa com o maior valor de venda)?
print(f'4. Qual a casa mais cara (casa com o maior valor de venda)? \n'
      f'R: A casa {data.sort_values("price", ascending=False).iloc[0,0]} é a mais cara, '
      f'com o valor de {data.sort_values("price", ascending=False).iloc[0,2]}.')

# 5. Qual a casa com o maior número de quartos?
print(f'5. Qual a casa com o maior número de quartos? \n'
      f'R: A casa {data.sort_values("bedrooms", ascending=False).iloc[0,0]} '
      f'possui {data.sort_values("bedrooms", ascending=False).iloc[0,3]} quartos.')

# 6. Qual a soma total de quartos do conjunto de dados?
print(f'6. Qual a soma total de quartos do conjunto de dados? \n'
      f'R: A soma total é de {data["bedrooms"].sum()} quartos.')

# 7.Quantas casas possuem 2 banheiros?
print(f'7. Quantas casas possuem 2 banheiros? \n'
      f'R: Total com 2 banheiros são {len(data.loc[data["bathrooms"] == 2])} casas.')

# 8. Qual o preço médio de todas as casas no conjunto de dados?
print(f'8. Qual o preço médio de todas as casas no conjunto de dados? \n'
      f'R: Preço médio é de {data["price"].mean()}.')

# 9. Qual o preço médio de casas com 2 banheiros?
preco_medio = data.loc[data["bathrooms"] == 2]
print(f'9. Qual o preço médio de casas com 2 banheiros? \n'
      f'R: O preço médio é de {preco_medio["price"].mean()}.')

# 10. Qual o preço mínimo entre as casas com 3 quartos?
preco_min = data.loc[data["bedrooms"] == 3]
print(f'10. Qual o preço mínimo entre as casas com 3 quartos? \n'
      f'R: O preço mínimo é de {preco_min["price"].min()}.')

# 11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
sala_estar = data.loc[data["sqft_living"] > 300]
print(f'11. Quantas casas possuem mais de 300 metros quadrados na sala de estar? \n'
      f'R: O total é de {sala_estar["id"].count()} casas.')

# 12. Quantas casas tem mais de 2 andares?
acima_dois_andares = data.loc[data["floors"] > 2]
print(f'12. Quantas casas tem mais de 2 andares? \n'
      f'R: Total que tem mais de 2 andares é de {acima_dois_andares["id"].count()} casas.')

# 13. Quantas casas tem vista para o mar?
vista_mar = data.loc[data["waterfront"] == 1]
print(f'13. Quantas casas tem vista para o mar? \n'
      f'R: Total que tem vista para o mar é de {vista_mar["id"].count()} casas.')

# 14. Das casas com vista para o mar, quantas tem 3 quartos?
tres_quartos = data.loc[(data["waterfront"] == 1) & (data["bedrooms"] == 3)]
print(f'14. Das casas com vista para o mar, quantas tem 3 quartos? \n'
      f'R: Total que tem vista para o mar e 3 quartos '
      f'é de {tres_quartos["id"].count()} casas.')

# 15. Das casas com mais de 300 metros quadrados de sala de estar,
# quantas tem mais de 2 banheiros?
dois_banheiros = data.loc[(data["sqft_living"]) > 300 & (data["bathrooms"] > 2)]
print(f'15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros? \n'
      f'R: Total de sala de estar acima de 300 metros quadrados e mais que 2 banheiros '
      f'é de {dois_banheiros["id"].count()} casas.')
