contador = 1 
# Exibir de 1 a 10
while (contador <= 10):
  print(contador)
  contador += 1
# Criando uma lista 
animais = ['tatu', 'gato', 'pato']
# Exibindo os elementos da lista
print(animais)
# Exibindo o terceiro elemento da lista
print(animais[2])
# Exibindo a quantidade de elementos da lista
print(len(animais))
# Adicionando um novo elemento a lista
animais.append('cachorro')
print(animais)
print(len(animais))
# Removendo um elemento da lista
animais.pop(2)
print(animais)
i = 0
while (i < len(animais)):
  print(animais[i])
  i = i + 1

for animal in animais:
  print(animais)