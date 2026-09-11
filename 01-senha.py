nome = input("Digite o nome:")
senha_digitada = input("Digite sua senha:")
senha_cadastrada = '123'

while senha_digitada != senha_cadastrada or nome != nome:
    print ("Nome ou Senha incorreta! Tente novamente.")
    nome = input("Digite seu nome:")
    senha_digitada = input("Digite sua senha:")

    print (f"{nome} Bem-vindo ao Sistema...")