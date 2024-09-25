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


def deposito(saldo, extrato):
    valor = float(input("Insira o valor para depositar: "))
    if valor <= 0:
        print("Valor inválido.")

    elif valor > 0:
        saldo += valor
        print(f"Seu novo saldo é R$ {saldo:.2f}")
        extrato += f"Depósito no valor de R$ {valor:.2f} \n"
    return saldo, extrato


def saque(saldo, numero_saques, extrato):

    if numero_saques >= 3:
        print("Limite de saque diário atingido")
        return saldo, numero_saques

    valor = float(input("Insira o valor para sacar: "))

    if valor > 500.01:
        print("Valor máximo para saque é de R$ 500.00")

    elif valor > saldo:
        print("Saldo insuficiente, Operação não concluida.")

    elif valor <= 0:
        print("Valor inválido.")

    elif valor > 0 and valor <= saldo and valor <= 500.00:
        numero_saques += 1
        saldo -= valor
        print(f"Seu novo saldo é R$ {saldo:.2f}")
        extrato += f"Saque no valor de R$ {valor:.2f} \n"
    return saldo, numero_saques, extrato


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        print("Saque")
        saldo, numero_saques, extrato = saque(saldo, numero_saques, extrato)
    elif opcao == "e":
        print("\n-------------Extrato-------------")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"Saldo atual R$: {saldo:.2f}")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione  novamente a operação desejada.")
