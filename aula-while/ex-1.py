n = int(input('Digium um número: '))
maior = n
while n != 0:
    if n > maior:
        maior = n
    n = int(input('digite outro número: '))
print(f'maior: {maior}')
    