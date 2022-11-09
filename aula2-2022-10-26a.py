''' Permite que o usuário digite algo
Title deixa a primeira letra em maiúsculo'''
nome = input('Qual o seu nome? ').title()
# Int antes do input transforma a string em inteiro
idade = int(input('Qual a sua idade? '))
# Calcula o dobro da idade
dobro = idade * 2
print(f'Seu nome é {nome} e vc tem {idade} anos')
print(f'O dobro da sua idade é {dobro} anos')
# If, Else e Elif servem para condicionar uma variável
if idade >= 18:
  print('Você é maior de idade, já pode dirigir.')
else:
  print('Você é menor de idade, ainda não pode dirigir.')
gênero = input('Qual o seu gênero? [M/F] ').title()[0]
if gênero == 'M':
  print('Você é do gênero masculino')
elif gênero == 'F':
  print('Você é do gênero feminino')