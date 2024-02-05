"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
import os
cond = True

while cond == True:
    try:
        numero = int(input("Digite um número inteiro:  "))
        cond = False

    except(ValueError):
        os.system("cls")
        print("Digite apenas números inteiros.")
        continue

if (numero % 2) == 1:
    print("O número digitado é impar")
else:
    print("O número digitado é par")