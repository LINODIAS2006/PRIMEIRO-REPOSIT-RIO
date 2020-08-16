while True:

    def calculadora():

        def soma(x, y):
            return x + y

        def subtracao(x, y):
            return x - y

        def multiplicacao(x, y):
            return x * y

        def divisao(x, y):
            return x / y

        opcao = int(input('ESCOLHA \n1 para SOMA \n2 para SUBTRAÇÃO \n3 para MULTIPLICAÇÃO \n4 para DIVISÃO \n\n'))
        if opcao == 1:
            num1 = int(input('\nQual numero deseja somar? : '))
            num2 = int(input('Qual o outro numero para somar: '))
            print(f'\nA soma é igual a: {soma(num1, num2)}')

        elif opcao == 2:
            num1 = int(input('\nQual numero deseja subtrair? : '))
            num2 = int(input('Qual o outro numero para subtrair: '))
            print(f'\nA subtraçãp é igual a: {subtracao(num1, num2)}')

        elif opcao == 3:
            num1 = int(input('\nQual numero deseja multiplicar? : '))
            num2 = int(input('Qual o outro numero para multiplicar: '))
            print(f'\nA multiplicação é igual a: {multiplicacao(num1, num2)}')

        elif opcao == 4:
            num1 = int(input('\nQual numero deseja dividir? : '))
            num2 = int(input('Qual o outro numero para dividir: '))
            print(f'\nA divisão é igual a: {divisao(num1, num2)}')

        else:
            print('Opção inválida.')

        return;


    calculadora()

    opcao2 = int(input('\nSe deseja continuar calculando ESCOLHA \n1 para CONTINUAR \n2 para PARAR \n\n '))

if opcao2 == 1:
    bool = False

else:
    bool = True
