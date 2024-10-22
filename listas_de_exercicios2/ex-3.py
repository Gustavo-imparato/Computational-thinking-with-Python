#Escreva um programa que leia um conjunto de 10 números inteiros positivos. Seu programa deve determinar e imprimir o maior deles. Use o laço FOR
x = 0
for i in range(10):
    y = int(input('digite um numero: '))
    if y > x:
        x = y 
print(x)