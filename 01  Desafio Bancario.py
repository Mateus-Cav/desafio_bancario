def exibir_menu():
    print("\nBem-vindo ao Banco Python!")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Extrato")
    print("5. Sair")

def depositar(valor, saldo):
    if valor > 0:
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        saldo += valor
    else:
        print("Valor inválido para depósito.")
    
    return saldo

def sacar(valor, saldo):
    if saldo == 0:
        print("Não é possível realizar saques com saldo zerado.")
        return saldo

    if valor <= 0:
        print("Valor inválido para saque.")

    elif valor > 500:
        print("O valor máximo para saque é R$ 500.00.")

    elif valor > saldo:
        print("Saldo insuficiente para saque.")

    else:
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        saldo -= valor

    return saldo

def extrato(saldo):
    if saldo == 0:
        print("Não foram realizadas movimentações.")
    else:
        print(f"Seu saldo atual é R$ {saldo:.2f}.")

saldo_atual = 0
qtd_de_saques = 0
novo_saldo = 0

while True:
    print("\n")
    exibir_menu()
    escolha = int(input("Escolha o menu desejado: ").strip())

    if escolha == 5:
        print("Obrigado por usar o Banco Python!")
        break

    elif escolha == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: ").strip())
        novo_saldo = depositar(valor_deposito, saldo_atual)
        saldo_atual = novo_saldo

    elif escolha == 3:

        if qtd_de_saques > 3:
            print("Número máximo de saques atingido.")

        else:
            if saldo_atual == 0:
                print("Não é possível realizar saques com saldo zerado.")
                continue
            else:
                valor_saque = float(input("Digite o valor a ser sacado: ").strip())
                if valor_saque == 0:
                    print("Valor inválido para saque.")
                else:
                    novo_saldo = sacar(valor_saque, saldo_atual)
                    qtd_de_saques += 1
                    saldo_atual = novo_saldo

    elif escolha == 4:
        extrato(saldo_atual)

    else:
        print("Opção inválida. Tente novamente.")