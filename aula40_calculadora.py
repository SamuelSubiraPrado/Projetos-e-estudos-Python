#Calculadora 
#solicitar n1, um operador e n2;

continuar = True
while continuar == True:

    try:
        n1= float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+ ,-,/,*): ")
        n2= float(input("Digite o segundo número: "))
        resultado = 0

        if operador == '+': 
            resultado = n1 + n2
            print (f"Seu resultado é {resultado:.2f}.")
        elif operador == '-': 
            resultado = n1 - n2
            print (f"Seu resultado é {resultado:.2f}.")
        elif operador == '*': 
            resultado = n1 * n2
            print (f"Seu resultado é {resultado:.2f}.")
        elif operador == '/': 
            resultado = n1 + n2
            print (f"Seu resultado é {resultado:.2f}.")
        else:
            print("Você não digitou um operador valido.")

        continuar=input ('Deseja continuar? (S/N): ')

        if continuar == 's' or continuar == 'S':
            continuar = True

        else:
            print ("Finalizado")
            continuar = False
        
    except:
        
        print("Você digitou algo incorretamente, tenha certeza de digitar apenas números e operadores.")

        continuar=input ('Deseja continuar? (S/N): ')

        if continuar == 's' or continuar == 'S':
            continuar = True

        else:
            print ("Finalizado")
            continuar = False
    
