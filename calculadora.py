"""
Calculadora com lógica RPN
Alguns adendos podem ser feitos e testes de tipo de entrada
a viriável repete recebe False quando vai haver interrupção
pois não tenho experiência no Python e temia em algum caso
entrasse em loop. Quando gera resultado n"ao há alteração
da variável repete para garantir loop até tocar em espaço
"""

repete = True

while repete==True:

    print('Entre com espaço para interromper a calculadora')

    valor1 = input ('Entre o 1º número: ')

    if valor1.isspace():
        print ('Você pressionou espaço e interrompeu a calculadora')
        repete = False
        exit()
    else :
        valor1 = int(valor1)

    valor2 = input ('Entre o 2º número: ')

    if valor2.isspace():
        print ('Você pressionou espaço e interrompeu a calculadora')
        repete = False
        exit()
    else :
        valor2 = int(valor2)

    operacao = input ('Entre a operação ( + - * / ): ')

    if operacao == '+':
        resultado: int = valor1 + valor2
    elif operacao == '-':
        resultado: int = valor1 - valor2
    elif operacao == '*':
        resultado: int = valor1 * valor2
    elif operacao == '/':
        if valor2 == 0:
            print ('Divisor não pode ser 0')
            repete = False
            exit()
        else : 
            resultado: float = valor1 / valor2
    else :
        print('Você pressionou espaço e interrompeu a calculadora')
        repete = False
        exit()

    print ('{} {} {} = {}'.format(valor1, operacao, valor2, resultado))
else :
    print ('A calculadora foi interrompida')
