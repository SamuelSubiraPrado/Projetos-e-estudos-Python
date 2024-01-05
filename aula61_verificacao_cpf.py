"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

#OBS: ESSE CÓDIGO AINDA NÃO TEM TRATAMENTO DE ERROS, ENTÃO É NECESSÁRIO DIGITAR CORRETAMENTE O CPF

#OBTENDO O CPF
import os

condicao = True
while condicao == True:
    try:
       
        cpf_enviado_usuario = input("Digite seu CPF (Neste formato 123.456.789-10): ")
        cpf_sem_pontos = cpf_enviado_usuario.split('.')
        cpf_sem_traco = cpf_sem_pontos[2].split('-')
        cpf_extraido = cpf_sem_pontos[0] + cpf_sem_pontos[1] + cpf_sem_traco[0] + cpf_sem_traco[1]
        condicao = False
    
    except:
        os.system('cls')
        print("\nVocê digitou incorretamente, digite seu CPF no formato correto (123.456.789-10)\n")
        

#OBTENDO O PRIMEIRO DÍGITO
multiplicador = 10
soma_multiplicador_cpf = 0

for numero_cpf in cpf_extraido:
    if multiplicador != 1:
        soma_multiplicador_cpf += (multiplicador * int(numero_cpf))
        multiplicador += -1

resto_div = (soma_multiplicador_cpf * 10) % 11

if resto_div > 9:
    primeiro_digito = 0
else :
    primeiro_digito = resto_div

#OBTENDO O SEGUNDO DÍGITO
cpf_final = cpf_extraido + str(primeiro_digito)
multiplicador = 11
soma_multiplicador_cpf = 0

for numero_cpf in cpf_extraido:
    if multiplicador != 1:
        soma_multiplicador_cpf += (multiplicador * int(numero_cpf))
        multiplicador += -1

resto_div = (soma_multiplicador_cpf * 10) % 11

if resto_div > 9:
    segundo_digito = 0 
else :
    segundo_digito = resto_div

cpf_gerado_pelo_calculo = cpf_sem_pontos[0] + cpf_sem_pontos[1] + cpf_sem_traco[0] + str(primeiro_digito) + str(segundo_digito)

if cpf_gerado_pelo_calculo == cpf_extraido:
    os.system('cls')
    print('O cpf é válido')
else:
    os.system('cls') 
    print('O cpf é inválido')


