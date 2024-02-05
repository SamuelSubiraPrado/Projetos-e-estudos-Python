"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
import os
cond = True

while cond == True:
    try:
        hora = input("Digite o horário atual (ex: 18:35): ")
        hora_list = hora.split(':')
        hora_separado = int(hora_list[0])

        if hora_separado >= 0 and hora_separado <= 11:
                    print("Bom dia!")

        if hora_separado >= 12 and hora_separado <= 17:
                    print("Boa tarde!")

        if hora_separado >= 18 and hora_separado <= 23:
                    print("Boa noite!")
                    
    except:
        os.system("cls")
        print("Digite apenas números neste formato 18:35")
        continue
    