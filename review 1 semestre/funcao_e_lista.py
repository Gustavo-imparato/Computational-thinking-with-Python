def tamanho_lista():
    print('TAMANHO DA LISTA')
    print('-----------------------------')
    t = int(input('tamanho: '))
    return t

def criar_lista(t):
    print('CRIAR UMA LISTA')
    print('-----------------------------')
    lista = []
    i=0
    while i<t:
        n = int(input('Numero: ' ))
        lista.append(n)
        i+=1
    return lista

def imprimir_lista(lista):
    print('TAMANHO DA LISTA')
    print('-----------------------------')
    for i in lista:
        print(f'Elemento: {i}')

def imprimir_pares(lista):
    print('TAMANHO DA LISTA')
    print('-----------------------------')
    for i in lista:
        if i%2 ==0:
            print(f'{i} é par')

def separar_pares(lista):
    print('SEPARANDO OS ELEMENTOS PARES DA LISTA')
    print('-----------------------------')
    lista_pares = []
    for i in lista:
        if i%2 ==0:
            lista_pares.append(i)
    return lista_pares

def obter_numero(lista):
    print('OBTER NUMERO DA LISTA')
    print('-----------------------------')
    n = int(input('Número: '))
    return n

def verificar_qntde_ocorrencias(lista, n):
    print('Quantidade de ocorrencias de um numero')
    print('-----------------------------')
    cont = 0
    for i in lista:
        if i ==n:
            cont+=1
    return cont




def principal():
    print('TAMANHO DA LISTA')
    print('-----------------------------')
    tamanho = tamanho_lista()
    minha_lista = criar_lista(tamanho)
    imprimir_lista(minha_lista)
    print(f'Tamanho: {len(minha_lista)}')
    imprimir_pares(minha_lista)
    lista_pares = separar_pares(minha_lista)
    imprimir_lista(lista_pares)
    n = obter_numero()
    qtde = verificar_qntde_ocorrencias()
    print(f'qnde: {qtde}')



    
principal()