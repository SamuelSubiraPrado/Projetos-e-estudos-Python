#Iterando uma string com while

nome = input("Digite um nome: ")
tamanho_nome = len(nome)

nova_string = ''
i=0

while i != tamanho_nome:
    for letra in nome:
        nova_string += f'*{letra}'
        i += 1
    nova_string += '*'
    
print(nova_string)