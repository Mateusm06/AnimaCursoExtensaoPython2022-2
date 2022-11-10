#criação de funções
preco = 2000

#Calcular 5% de imposto
imposto = preco * 0.05
print(imposto)

#Criar uma função calcular_imposto()
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto
preco = float(input('Digite aqui um valor: '))
imposto = calcular_imposto(preco)
print(imposto)
valores = [2.59, 20.03, 33.42, 92.05]
for valor in valores:
  print(f'O imposto de {valor} é {calcular_imposto(valor)}')

# Declarar um função calcula_imposto_aliquota que recebe dois parâmetros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.
  
def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto
for valor in valores:
  print(f'O imposto de {valor} é {calcular_imposto_aliquota(valor)}')