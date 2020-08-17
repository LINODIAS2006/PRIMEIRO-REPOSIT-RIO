

# CALCULADORA SIMPLES


#laço de repetição para que seja pssível mais de um cálculo sem sair do programa.
while True:

    def calculadora():
        """Função que cria mais quatro funçôes com as quatro operações e executa as respectivas operações
        atrevés das condicionais correspndentes"""
        def soma(x, y):
            """Função que executa a soma de dois números quaisquer"""
            return x + y

        def subtracao(x, y):
            """Função que executa a subtração de dois números quaisquer"""
            return x - y

        def multiplicacao(x, y):
            """Função que executa a multiplicação de dois números quaisquer"""
            return x * y

        def divisao(x, y):
            """Função que executa a divisão de dois números quaisquer"""
            return x / y

        #Variável que recebe as opções do usuário
        opcao = int(input('ESCOLHA \n1 para SOMA \n2 para SUBTRAÇÃO \n3 para MULTIPLICAÇÃO \n4 para DIVISÃO \n\n'))

        #Condicional que trata a opção 1 do usuário e chama a função soma pelo print
        if opcao == 1:
            num1 = int(input('\nQual numero deseja somar? : '))
            num2 = int(input('Qual o outro numero para somar: '))
            print(f'\nA soma é igual a: {soma(num1, num2)}')

        #Condicional que trata a opção 2 do usuário e chama a função subtração pelo print
        elif opcao == 2:
            num1 = int(input('\nQual numero deseja subtrair? : '))
            num2 = int(input('Qual o outro numero para subtrair: '))
            print(f'\nA subtraçãp é igual a: {subtracao(num1, num2)}')

        #Condicional que trata a opção 3 do usuário e chama a função multiplicação pelo print
        elif opcao == 3:
            num1 = int(input('\nQual numero deseja multiplicar? : '))
            num2 = int(input('Qual o outro numero para multiplicar: '))
            print(f'\nA multiplicação é igual a: {multiplicacao(num1, num2)}')

        #Condicional que trata a opção 4 do usuário e chama a função divisão pelo print
        elif opcao == 4:
            num1 = int(input('\nQual numero deseja dividir? : '))
            num2 = int(input('Qual o outro numero para dividir: '))
            print(f'\nA divisão é igual a: {divisao(num1, num2)}')

        #Trata uma possível opção inválida digitada pelo usuário
        else:
            print('Opção inválida.')

        #Retorno da função calculadora
        return;

    #Chama a função calculadora
    calculadora()

    #Variavel que recebe a as opções do usuário de PARAR ou CONTINUAR calculando
    opcao2 = int(input('\nSe deseja continuar calculando ESCOLHA \n1 para CONTINUAR \n2 para PARAR \n\n '))

#Utiliza a opção do usuário para converter o booleano em False e para o laço de repetição
if opcao2 == 1:
    bool = False

#Utiliza a opção do usuário para converter o booleano em True e continuar o laço de repetição
else:
    bool = True
