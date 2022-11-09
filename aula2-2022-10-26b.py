nome = input('Qual o seu nome? ').title()
nota = float(input('Qual a sua nota? '))
if nota == 10:
  print(f'Parabéns, {nome}, você é o bichão mesmo')
elif nota >= 6 or nota < 10:
  print('Pelo menos passou')
else:
  print('Você precisa estudar mais')