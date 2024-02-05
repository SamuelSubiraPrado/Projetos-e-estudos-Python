#calculadora 
# pedir primeiro e segundo número e logo em seguida o operador(+,-,*,/)

import os
cond = True

while cond == True:
    
    try:
        print("    CALCULADORA BÁSICA    \n")
        num_1 = float(input("Digite o primeiro número: "))
        
        operador = input("Digite a operação (+ , - , * , / ): ")
        if len(operador) > 1:
             
             ("\nDigite apenas um caractere (+ , - , * , / )\n")
             continue
        
        num_2 = float(input("Digite o segundo número: "))

        if operador == '+':
            print( f'Resultado: {num_1} + {num_2} = {num_1 + num_2}')
        
        elif operador == '-':
            print( f'Resultado: {num_1} - {num_2} = {num_1 - num_2}')

        elif operador == '*':
            print( f'Resultado: {num_1} * {num_2} = {num_1 * num_2}')

        elif operador == '+':
            print( f'Resultado: {num_1} / {num_2} = {num_1 / num_2}')

        else:
            os.system("cls")
            print("\nDigite um operador válido\n")
            continue

        continuar= input ('\nDESEJA CONTINUAR? (S/N): \n')

        if continuar == 's' or continuar == 'S':
            continue

        else:
            print ("\nFinalizado")
            cond = False


    except(ValueError):
        os.system("cls")
        print("\nDigite apenas números\n")
        continue

    except:
        os.system("cls")
        print("\nErro desconhecido, por favor tente novamente\n")
        continue