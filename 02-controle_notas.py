nome = input("Qual seu nome? ")

nota = int(input("Digite a nota: "))
adicionar = input("Deseja digitar outra nota? ")

soma = nota
quantidade = 1

while adicionar == "sim":
    nota = int(input("Digite a nota: "))
    
    soma = soma + nota
    quantidade = quantidade + 1
    
    adicionar = input("Deseja adicionar outra nota? ")

media = soma / quantidade

print(f"Nome: {nome}")
print(f"Sua média: {media}")



