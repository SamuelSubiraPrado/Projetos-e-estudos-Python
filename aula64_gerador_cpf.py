"""
ESTE CÓDIGO SERVE APENAS PARA FINS EDUCATIVOS, FAVOR NÃO USAR DE MANEIRA INADEQUADA.
"""

#Gerando um CPF aleatório
import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

#OBTENDO O PRIMEIRO DÍGITO
multiplicador = 10
soma_multiplicador_cpf = 0

for numero_cpf in nove_digitos:
    if multiplicador != 1:
        soma_multiplicador_cpf += (multiplicador * int(numero_cpf))
        multiplicador += -1

resto_div = (soma_multiplicador_cpf * 10) % 11

if resto_div > 9:
    primeiro_digito = 0
else :
    primeiro_digito = resto_div

#OBTENDO O SEGUNDO DÍGITO
cpf_final = nove_digitos + str(primeiro_digito)
multiplicador = 11
soma_multiplicador_cpf = 0

for numero_cpf in cpf_final:
    if multiplicador != 1:
        soma_multiplicador_cpf += (multiplicador * int(numero_cpf))
        multiplicador += -1

resto_div = (soma_multiplicador_cpf * 10) % 11

if resto_div > 9:
    segundo_digito = 0 
else :
    segundo_digito = resto_div

cpf_gerado_pelo_calculo = nove_digitos + str(primeiro_digito) + str(segundo_digito)

print(f'CPF gerado aleatoriamente: {cpf_gerado_pelo_calculo}')


