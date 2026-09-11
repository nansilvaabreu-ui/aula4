def Somar():
    numero_1= int(input("Digite o primeiro numero: "))
    numero_2= int(input("Digite o segundo numero: "))
    soma = numero_1 + numero_2
    print(soma)
def Subitrair():
    numero_1= int(input("Digite o primeiro numero: "))
    numero_2= int(input("Digite o segundo numero: "))
    sub = numero_1 - numero_2
    print(sub)
def Multiplicar():
    numero_1= int(input("Digite o primeiro numero: "))
    numero_2= int(input("Digite o segundo numero: "))
    mult = numero_1 * numero_2
    print(mult)
def Dividir():
    numero_1= int(input("Digite o primeiro numero: "))
    numero_2= int(input("Digite o segundo numero: "))
    div = numero_1 / numero_2
    print(div)
def Pares():
    numero= int(input("Digite um número: "))
    contador = 0
    while contador <= numero:
        print(contador)
        contador = contador + 2
def Impares():
    numero= int(input("Digite um número: "))
    contador = 1
    while contador <= numero:
        print(contador)
        contador = contador + 2
    print(contador)
def Somatorio():
    numero= int(input("Digite um número: "))
    contador = 1
    soma = 0
    while contador <= numero:
        soma = soma + contador
        contador = contador + 1

    print(f"O somatório é:", {soma})
def Fatorial():
    numero = int(input("Digite um número: "))
    contador = 1
    resultado = 1
    while contador <= numero:
        resultado = resultado * contador
        contador = contador + 1

    print("O fatorial é:", resultado)

while True:
    print ("CALCULADORA")
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Pares")
    print ("6 - Impares")
    print ("7 - Somatorio")
    print ("8 - Fatorial")
    print ("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        Somar()
    elif opcao == "2":
        Subitrair()
    elif opcao == "3":
        Multiplicar()
    elif opcao == "4":
        Dividir()
    elif opcao == "5":
        Pares()
    elif opcao == "6":
        Impares()
    elif opcao == "7":
        Somatorio()
    elif opcao == "8":
        Fatorial()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente!!!")
    