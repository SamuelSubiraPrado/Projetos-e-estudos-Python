#Sitemas de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
posicao_for = 0
for pergunta in perguntas:
    print('\nPergunta: ',pergunta['Pergunta'])
    print('\nOpções: ')
    
    #Também poderia ser feito assim:
    # for i, opcao in enumerate(pergunta['Opções']):
    #     print(f'{i}) {opcao}')
    
    i=0
    for opcao in pergunta['Opções']:
        
        print(f'{i}) {opcao}')
        i += 1
    
    digito = None
    while digito == None:

        escolha = input("Escolha uma opção: ")
        
        if escolha.isdigit() and (int(escolha) >= 0 and int(escolha) < 4):

            digito = int(escolha)

            if perguntas[posicao_for]['Opções'][digito] == pergunta['Resposta']:
                    print('Acertou!!!')
                    acertos += 1
            else:
                    print('Errou X')
                    print('Resposta: ',pergunta['Resposta'])

            posicao_for += 1

           

        if digito is None:
            print('DIGITE APENAS O NÚMERO DA OPÇÃO DESEJADA (0,1,2,3)!')
            continue
        
print(f'\nVOCÊ ACERTOU {acertos} DE {posicao_for} PERGUNTAS.\n\n')
