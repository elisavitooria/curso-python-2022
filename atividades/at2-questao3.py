#Faça um programa pra calcular o IMC e informar qual categoria pertence o IMC da pessoa
#entrada
peso = float(input('informe o seu peso(kg):'))
altura =float(input('informe a sua altura(m):'))
 
 #processamento
imc = peso / (altura **2)

#saída
if imc < 18.5:
    print(f'{imc} você está abaixo do peso normal.')
elif 18.5 <= imc < 24.99:
    print(f'{imc} normal')
elif 25 <= imc < 29.99:
    print(f'{imc} pré obeso')
elif 30 <= imc < 34.99:
    print(f'{imc} obesidade tipo I')
elif 35 <= imc < 39.99:
    print(f'{imc} obesidade tipo II')
elif 40 <= imc:
    print(f'{imc} obesidade tipo III')