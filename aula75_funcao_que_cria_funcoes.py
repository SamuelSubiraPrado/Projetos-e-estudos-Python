'''
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
'''

#Minha versão
'''
num = float(input("Informe um número: "))

def multiplicar(num):
    
    def duplicar(num):
        return f'\n2 x {num * 2}'
        
    def triplicar(num):
        return f'\n3 x {num * 3}'

    def quadruplicar (num):
        return f'\n4 x {num * 4}\n'

    return duplicar(num), triplicar(num), quadruplicar(num)

print(*multiplicar(num))
'''

#Versão pós-aula

num_usuario = float(input("Informe um número: "))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return f'{multiplicador} x {numero} = {numero * multiplicador}'
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(num_usuario))
print(triplicar(num_usuario))
print(quadruplicar(num_usuario))

