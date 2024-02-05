#Calculo IMC
import os

condicao = True
while condicao == True:

    try:
        nome = input("Digite Seu nome: ")
        altura = float(input("Digite a sua altura (ex: 1.70): "))
        peso = float(input("Digite seu peso:  "))
        condicao = False
    except(ValueError):
        os.system('cls')
        print("Digite apenas números no campo Altura e Peso")
        continue

imc = peso/ (altura*altura)


print(f"\n{nome} tem {altura} de altura,\npesa {peso} kg e seu IMC é\n{imc:.2f}")
