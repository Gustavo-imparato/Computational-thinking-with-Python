#Faça um programa para ler e escrever dados de uma turma de 5 alunos. O programa deve pedir dados como nome, idade e sexo. O programa deve imprimir os dados do aluno mais velho. Use o laço DO-WHILE.

i = 0
maior_idade = 0


while True :
    print('digite os dados dos alunos que deseja cadastrar')
    nome = input(' Nome do aluno: ')
    idade = int(input('Idade do aluno: '))
    sexo = input("Sexo do aluno (M ou F): ")

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome
        sexoVelho = sexo

    i += 1

    if i==5:
        break

print("Dados do aluno mais velho:")
print("Nome:", nome_mais_velho)
print("Idade:", maior_idade)
print('Sexo: ',sexoVelho)