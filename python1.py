Exemplo 1

#Exemplo 1: Contador - Contando até 10


# Inicializando o contador
contador = 1


# Estrutura de repetição com teste no início (while)
while contador <= 10:
    print(contador)
    contador += 1  # Incrementa o contador

#Exemplo 2: Acumulador - Soma de Números


# Inicializando o acumulador
soma = 0
contador = 1


# Estrutura de repetição
while contador <= 5:
    numero = int(input(f"Digite o {contador}º número: "))
    soma += numero  # Acumulador (soma)
    contador += 1  # Incrementa o contador


#Contar números pares até N


 #Solicita a entrada do usuário
n = int(input("Digite um número inteiro N: "))


print(f"Números pares de 0 até {n}:")


