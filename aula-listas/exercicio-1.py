salarios = [0, 0, 0, 0]
soma = 0

salarios[0] = float(input('Salario: '))
soma+=salarios[0]
salarios[1] = float(input('Salario: '))
soma+=salarios[1]
salarios[2] = float(input('Salario: '))
soma+=salarios[2]
salarios[3] = float(input('Salario: '))
soma+=salarios[3]
media = soma/4

print(media)
if salarios[0] < media:
    print(f'abaixo da media {salarios[0]:.2f}')
if salarios[1] < media:
    print(f'abaixo da media {salarios[1]:.2f}')
if salarios[2] < media:
    print(f'abaixo da media {salarios[2]:.2f}')
if salarios[3] < media:
    print(f'abaixo da media {salarios[3]:.2f}')


