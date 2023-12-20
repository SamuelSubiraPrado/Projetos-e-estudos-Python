'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e litar valores da sua lista
não permita que o programa quebre com
erros de indives inexistentes na lista
'''

#Selecione uma opção [i]nserir, [a]pagar, [l]istar
#[a]pagar - escolha um idice p/apagar / se não existir, continue e mostrar que não foi possível apagar
#[i]nserir - Valor: ____
#[l]istar - listar os valores atuais
import os

lista = []
condicao = True

print('\tFAÇA A SUA LISTA\n')
while condicao == True:
    selecao = ''
    selecao = input('\nSelecione uma opção [i]nserir, [a]pagar, [l]istar:  ')
    
    if selecao == 'i' or selecao == 'I' : 

        os.system('cls')
        inserir= input('Valor: ')
        lista.append(f'{inserir}')

    elif selecao == 'a' or selecao == 'A' : 
        
        os.system('cls')
        try:
            apagar=input('Qual indice você deseja apagar?  ')
            print(f'{lista[int(apagar)]} foi apagado da lista')
            lista.pop(int(apagar))
            
        except ValueError:
            print('Digite apenas um número')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif selecao == 'l' or selecao == 'L' :

        os.system('cls')

        if len(lista) == 0:
            print('Sua lista está vazia')
        else:

            for indice, nome in enumerate(lista):
                print(indice, nome)

    else:
        os.system('cls')
        print('Digite apenas a inicial da opção desejada [i],[a],[l]\n')
