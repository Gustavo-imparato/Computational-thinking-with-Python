#lista com os nome de saltos 
texto_saltos = ['1o', '2o', '3o', '4o', '5o']

while True:
    #lista com os valores dos saltos
    saltos = [0 , 0, 0, 0, 0]

    #variaveis
    media_saltos = 0
    soma = 0
    melhor_salto = 0
    pior_salto = 0

    nome_atleta = input('nome: ')
    if nome_atleta != '':
        for i in range(5):
            saltos[i] = float(input(f'{texto_saltos[i]} salto: '))
            soma+=saltos[i]

        media_saltos = soma/len(saltos)
        melhor_salto = saltos[0]
        pior_salto = saltos[0]

        for salto in saltos:
            if salto > melhor_salto:
                melhor_salto = salto
            if salto < pior_salto:
                pior_salto = salto
            
            #exibindo os resultados 
            print(f'melhor salto: {melhor_salto}')
            print(f'pior salto: `{pior_salto}')
            print(f'{nome_atleta} \n media dos saltos{media_saltos}')
    else:
        print('informe o nome do atleta')

    print('continuar? \n 1-sim \n 2-não')
    opcao = int(input('opção: '))
    if opcao == 2:
        break
print('fim do programa')

