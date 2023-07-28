menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu.lower())
    if opcao == 'd':
        print('Depósito')
        valor = int(input('Qual o valor a ser depositado? '))
        if valor < 0:
            print('Valor para depósito deve ser positivo. Insira um novo valor: ')
            valor = int(input('Qual o valor a ser depositado? '))
        saldo += valor
        extrato += f'Depósito de R$ {valor:.2f}\n'
        continue
    if opcao == 's':
        print('Saque')
        if numero_saques < LIMITE_SAQUES:
            valor = int(input('Qual o valor para saque? '))
            if valor < 0:
                print('Valor para saque deve ser positivo. Insira um novo valor: ')
                valor = int(input('Qual o valor para saque? '))
            elif valor > 500:
                print('Valor limite para saque de R$ 500,00. Insira um novo valor: ')
                valor = int(input('Qual o valor para saque? '))
            else:
                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f'Saque de R$ {valor:.2f}\n'
                else:
                    print('Saldo insuficiente!')
        else:
            print('Você excedeu o número de saques diários! Máximo 3 saques por dia')
        continue
    if opcao == 'e':
        print('\n==================== Extrato ====================')
        print('Não existem movimentações para exibir!' if not extrato else extrato)
        print(f'\nSeu saldo atual é de R$ {saldo:.2f}')
        print('\n=================================================')
        continue
    if opcao == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada')
