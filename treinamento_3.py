"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} e voce tem {idade} anos
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
import os
cond = True

while cond == True:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        
        if nome and idade:

            print("Seu nome é", nome, "e você tem ", idade, "anos.")
            print(f"Seu nome invertido é {nome[::-1]}")

            if ' ' in nome:
                print("Seu nome contém espaços.")
            else:
                print("Seu nome não contém espaços.")   

            i = 0 #Contador de letras
            for letra in nome:

                if letra != ' ':
                    i = i + 1
            
            print(f"Seu nome contém {i} letras")

            print(f'A primeira letra do seu nome é {nome[0]}')
            print(f'A última letra do seu nome é {nome[-1]}\n\n')

            cond = False
        else:
            print("Desculpe, você deixou campos vazios.")
    except(ValueError):

        os.system("cls")
        print("Digite apenas números\n")
        continue

