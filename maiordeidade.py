#entrada
ano = int(input('informe o ano de nascimento:'))

#processamento
idade = 2022 - ano

if idade >= 18:
  print("idade suficiente.", idade)
  print("você foi aceito!")
  
if idade <	18:
  print("idade insuficiente.", idade)
  print("você não poderá participar")


