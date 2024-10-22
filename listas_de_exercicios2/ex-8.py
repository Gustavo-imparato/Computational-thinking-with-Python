#Calcular e mostrar a média aritmética dos números pares compreendidos entre 13 e 73. Utilize o laço que lhe for mais conveniente.

soma = 0
cont = 0

for i in range(14, 74, 2):
    soma += i
    cont += 1

media = soma / cont

print("A média aritmética dos números pares entre 13 e 73 é:", media)    