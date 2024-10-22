#estrutura de repetição for 

salarios = []
soma = 0 

for i in range(4):
    salario = float(input('Salário: '))
    soma+=salario
    salarios.append(salario)

media =soma/4

for salario in salarios:
    if salario < media:
        print(f'abaixo da media{salario:.2f}')