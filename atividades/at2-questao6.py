#entrada
nota1 = float(input('primeira nota'))
nota2 = float(input('segunda nota'))

#processamento
media = (nota1 + nota2) / 2

#saída
if media >= 7:
    print(f'{media} APROVADO')
elif media<7:
    print('REPROVADO')
else:
    print('APROVADO SEM DISTINÇÃO')
