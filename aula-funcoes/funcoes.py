'''
Calculadora simples
 -adição 
 -subtração
 -divisão
 -multiplicação

 Funções
 -menu()
 -entrada_dados()
 -adicao()
 -subtracao()
 -divisao()
 -multiplicacao()
 -imprimir()
 -controlador()
'''

#Funções Menu()
def menu():
    print(' Menu ')
    print('1-adição')
    print('2-subtração')
    print('3-divisão')
    print('4-multiplicação')
    op = int(input('Operação: '))
    return op

#------------------------------------------------
#Função entrada de dados()
def entrada_dados():
    print(' Entrada de dados ')
    num = int(input('Número: '))
    return num

#-----------------------------------------------
#Função adição()
def adicao(n1, n2):
    print(' Adição ')
    result = n1 + n2
    return result

#-----------------------------------------------
#Função subtração()
def subtracao(n1, n2):
    print(' Subtração ')
    result = n1 - n2
    return result

#-----------------------------------------------
#Função multiplicação()
def multiplicacao(n1, n2):
    print(' Multiplicação ')
    result = n1 * n2
    return result

#-----------------------------------------------
#Função divisão()
def divisao(n1, n2):
    print(' Divisão ')
    result = n1 / n2
    return result

#--------------------------------------------------
#Função imprime()
def imprime(result):
    print(' Imprime ')
    print('resultado :',result)

#--------------------------------------------------
#Função controlador()
def controlador(n1, n2, op):
    print(' Controlador ')
    if op==1:
        result = adicao(n1, n2)
    elif op==2:
        result = subtracao(n1, n2)
    elif op==3:
        result = divisao(n1, n2)
    elif op==4:
        result = multiplicacao(n1, n2)
    else:
        result = 'Opção inválida'
    return result

#------------------------------------------------------
#Pincipal
print('**- Pincipal -**')
op = menu()
n1 = entrada_dados()
n2 = entrada_dados()
result = controlador(n1, n2, op)
imprime(result)
