# Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = float(input('digite o 1º número:'))
num2 = float(input('digite o 2º número:'))
num3 = float(input('digite o 3º número:'))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")

