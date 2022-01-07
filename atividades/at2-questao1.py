#Faça um Programa que peça dois números e imprima o maior deles.

#entrada
num1 = float(input('digite o primeiro número:'))
num2 = float(input('digite o segundo número:'))

#saída
if num1 > num2:
  print("o", num1, "é maior que o", num2)
if num1 < num2:
  print("o", num2, "é maior que o", num1)