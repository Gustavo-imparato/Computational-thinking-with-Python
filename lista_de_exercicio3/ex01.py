#Escreva uma função que receba uma lista de números inteiros como parâmetro e retorna a soma de todos os elementos


def somar_lista(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

# Solicitar o tamanho da lista ao usuário
tamanho_lista = int(input("Digite o tamanho da lista: "))

# Solicitar os números inteiros ao usuário
lista_numeros = []
for i in range(tamanho_lista):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

# Calcular a soma da lista
resultado = somar_lista(lista_numeros)

# Exibir o resultado
print("A soma dos elementos da lista é:", resultado)