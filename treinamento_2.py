# Pedir 2 números e informar qual é maior ou caso 
# sejam iguais, informar que são iguais

import os
cond = True

while cond == True:
    try:
        valor_1 = float(input("Digite o primeiro valor: "))
        valor_2 = float(input("Digite o segundo valor: "))
        cond = False
    except:
        os.system("cls")
        print("Digite apenas números\n")
        continue

if valor_1 > valor_2:
    print(f"O primeiro valor ({valor_1}) é maior que o segundo valor ({valor_2})")

elif valor_1 < valor_2:
    print(f"O primeiro valor ({valor_1}) é menor que o segundo valor ({valor_2})")

elif valor_1 == valor_2:
    print(f"O primeiro valor ({valor_1}) é igual ao segundo valor ({valor_2})")
