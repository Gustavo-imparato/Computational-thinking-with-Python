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

def principal():
    print('TAMANHO DA LISTA')
    print('-----------------------------')
    t = tamanho_lista()
    lista = criar_lista(t)
    imprimir_lista(lista)

    
principal()