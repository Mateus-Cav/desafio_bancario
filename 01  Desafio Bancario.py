from datetime import date, datetime

def exibir_menu():
    print("\nBem-vindo ao Banco Python!")
    print("0. Cadastrar usuário")
    print("1. Cadastrar Conta Corrente")
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
        return saldo, "invalido"

    if valor <= 0:
        print("Valor inválido para saque.")
        return "invalido"

    elif valor > 500:
        print("O valor máximo para saque é R$ 500.00.")
        return "invalido"

    elif valor > saldo:
        print("Saldo insuficiente para saque.")
        return "invalido"

    else:
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        saldo -= valor

    return saldo

def extrato(saldo, lista_transacoes=[]):
    if saldo == 0:
        print("Não foram realizadas movimentações.")
    else:
        print(f"Seu saldo atual é R$ {saldo:.2f}.\n")
        print("Movimentações realizadas: \n ********************************")
        print(lista_transacoes)

def cadastrar_usuario(dicionario_usuarios):
    nome = input("Digite o nome do usuário: ").strip()
    cpf = input("Digite o CPF do usuário: ").strip()
    #Remove caracteres especiais e espaços do CPF
    cpf = cpf.replace(".", "").replace("-", "").strip()
    #Verifica se o CPF tem 11 dígitos e se é numérico
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
        return None
    
    #Verifica se o CPF já está cadastrado
    if cpf in dicionario_usuarios.keys():
        print("Usuário já cadastrado.")
        return None
    
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Digite o endereço do usuário: ").strip()
    

    dicionario_usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }
    #lista_usuarios.append(dicionario_usuarios[cpf])
    print(f"Usuário {dicionario_usuarios[cpf]['nome']} cadastrado com sucesso!")
    return dicionario_usuarios[cpf]
    
def criar_conta_corrente(ordenador_contas, dic_contas_corrente, dicionario_usuarios):
    #Prefixo da conta corrente
    prefixo_conta_corrente = "0001"

    if dicionario_usuarios == {}:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
        return None

    cpf_usuario = input("Digite o CPF do usuário: ").replace(".", "").replace("-", "").strip()
    if cpf_usuario not in dicionario_usuarios.keys():
        print("Usuário não encontrado.")
        return None

    conta_corrente = prefixo_conta_corrente + str(ordenador_contas)
    dic_contas_corrente[cpf_usuario] = {
        "conta_corrente": conta_corrente,
    }

    nome_usuario = dicionario_usuarios[cpf_usuario]['nome']
    print(f"Conta corrente {conta_corrente} criada com sucesso para o usuário {nome_usuario}!")


#INICIO DO PROGRAMA:
contador_contas_criadas = 0
#Variáveis para controle de saldo e transações
saldo_atual = 0
qtd_de_saques = 0
novo_saldo = 0
quantidade_transacoes = 0
lista_extrato = []
lista_usuarios_cadastrados =[]
lista_conta_corrente = []
#Dicionário para armazenar os dados dos usuários
dic_usuarios = {}
dic_contas_corrente = {}



while True:
    print("\n")
    exibir_menu()
    escolha = int(input("Escolha o menu desejado: ").strip())

    if escolha == 5:
        print("Obrigado por usar o Banco Python!")
        break

    #CADASTRO DE USUÁRIO
    elif escolha == 0:
        novo_usuario = cadastrar_usuario(dic_usuarios)
        # if novo_usuario:
        #      print(dic_usuarios)

    elif escolha == 1:
        criar_conta_corrente(contador_contas_criadas, dic_contas_corrente, dic_usuarios)
        contador_contas_criadas += 1
        continue

    #DEPOSITO
    elif escolha == 2:
        valor_deposito = float(input("Digite o valor a ser depositado: ").strip())
        
        if quantidade_transacoes >= 10:
            print("Número máximo de transações atingido.")
            continue

        if valor_deposito > 0:
            quantidade_transacoes += 1
            
        novo_saldo = depositar(valor_deposito, saldo_atual)
        saldo_atual = novo_saldo
        data_atual = datetime.now()
        data_atual = data_atual.strftime('%d/%m/%Y %H:%M:%S')
        texto_deposito = f"Depósito de R$ {valor_deposito:.2f} realizado em {data_atual}"
        lista_extrato.append(texto_deposito)

    #SAQUE
    elif escolha == 3:

        if qtd_de_saques > 3:
            print("Número máximo de saques atingido.")
            continue

        elif quantidade_transacoes >= 10:
            print("Número máximo de transações atingido.")
            continue

        else:
            if saldo_atual == 0:
                print("Não é possível realizar saques com saldo zerado.")
                continue
            else:
                valor_saque = float(input("Digite o valor a ser sacado: ").strip())
                if valor_saque <= 0:
                    print("Valor inválido para saque.")
                else:
                    novo_saldo = sacar(valor_saque, saldo_atual)
                    if novo_saldo == "invalido":
                        continue
                    else:
                        qtd_de_saques += 1
                        quantidade_transacoes += 1
                        saldo_atual = novo_saldo
                        data_atual = datetime.now()
                        data_atual = data_atual.strftime('%d/%m/%Y %H:%M:%S')
                        texto_saque = f"Saque de R$ {valor_saque:.2f} realizado em {data_atual}"
                        lista_extrato.append(texto_saque)
    #EXTRATO
    elif escolha == 4:
        extrato(saldo_atual, lista_extrato)

    else:
        print("Opção inválida. Tente novamente.")