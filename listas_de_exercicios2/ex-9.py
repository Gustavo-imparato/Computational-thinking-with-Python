#Escreva um programa para ler a quantidade de alunos existentes em uma turma. Depois disso, o programa deve ler as notas de cada um destes alunos, calcular e mostrar na tela a média aritmética destas notas. Utilize o laço WHILE.

x = int(input('Informe o numero de alunos da turma: '))
soma= 0
contagem = 0
i = 0

while i < x:
    nota = float(input('Informe a nota de um aluno: '))
    soma += nota
    i += 1
media = soma/x
print(f'A média de nota da turma é: {media:.2f} ',)
