n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
print('Escolha uma operação: '
    '1:soma, 2:subtração, 3:divisão, '
    '4:multiplicação')
operacao = input('Digite o numero da operação: ')

match operacao:
    case '1':
        operador = "soma"
        print('A {} de {} com {} '
        'é {}'.format(operador, n1, n2, n1+n2))
    case '2':
        operador = "subtração"
        print('A {} de {} com {} '
        'é {}'.format(operador, n1, n2, n1-n2))
    case '3':
        operador = "divisão"
        print('A {} de {} com {} '
        'é {}'.format(operador, n1, n2, n1/n2))
    case '4':
        operador = "multiplicação"
        print('A {} entre {} e {} '
        'é {}'.format(operador, n1, n2, n1*n2))
