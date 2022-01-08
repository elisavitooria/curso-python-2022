# Faça um Programa que leia três números e mostre o maior deles
num1 = float(input('digite o 1º número:'))
num2 = float(input('digite o 2º número:'))
num3 = float(input('digite o 3º número:'))

if num1 > num2 and num3:
    print('o primeiro numero é maior que os demais')
if num2 > num1 and num3:
    print('o segundo numero é maior que os demais')
if num3 > num1 and num2:
    print('o terceiro numero é maior que os demais')
