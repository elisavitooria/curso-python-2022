#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato
#entrada
produto1 = float(input('valor do produto 1'))
produto2 =float(input('valor do produto 2'))
produto3 =float(input('valor do produto 3'))

if produto1 < produto2:
    if produto1 < produto3:
        print("voce deve comprar o primeiro produto!")
    else:
        print("voce deve comprar o terceiro produto!")
else:
    if produto2 < produto3:
        print("voce deve comprar o segundo produto!")
    else:
        print("voce deve comprar o terceiro produto!")