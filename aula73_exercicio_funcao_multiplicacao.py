'''
Exercícios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor
da variável.
'''

#Permite o comando os.system('cls'), para limpar os terminais 
import os
continuar = True

#While utilizado para tratamento de erro, caso o except seja atingido, o programa "recomeça"
while continuar == True:

    try:
        #Tratando os números para uma tupla e retirando a virgula, assim recebendo números separados
        numeros= input('Digite os números a serem multiplicados: ')
        numeros_tratados = tuple(numeros.split(','))


        def mult_arg(*args):
            #Inicia com 1, pois qualquer número mult por 0, é zero.
            multiplicacao = 1
            for numero in args:
                if numero == 0:
                    continue
                else:
                    multiplicacao = multiplicacao * float(numero)
            return multiplicacao
            
        multiplicacao_final = mult_arg(*numeros_tratados)

        #Desativa o While
        continuar = False

        #Verificando se o número é par ou impar
        if (multiplicacao_final % 2) == 0:
            print(f"\nO resultado é {multiplicacao_final:.2f} e é um número Par")
        else:
            print(f"\nO resultado é {multiplicacao_final:.2f} e é um número Impar")

    except:
        os.system('cls')
        print("Digite apenas números, separe cada número por uma virgula.\n")
        
