menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(saldo):
    valor = float(input("Insira o valor para depositar: "))

    if valor > 0: 
        saldo += valor
        print(f"Seu novo saldo é {saldo}")
        return saldo
    
def saque(saldo, numero_saques):
    
    if numero_saques >= 3:
        print("Limite de saque diário atingido")
        return saldo, numero_saques
        
    valor = float(input("Insira o valor para sacar: "))
    if valor > 0 and valor <= saldo:
        numero_saques += 1
        saldo -= valor
        print(f"Seu novo saldo é {saldo}")
    return saldo, numero_saques

while True:
    opcao = input (menu)
    
    if opcao == "d":
        print("Depósito")
        saldo = deposito(saldo)
    
    elif opcao == "s":
        print("Saque")
        saldo, numero_saques = saque(saldo, numero_saques)
    elif opcao == "e":
        print(f"Extrato {saldo}")
        
    elif opcao == "q":
        break
    
    
    else:
        print("Operação inválida, por favor selecione  novamente a operação desejada.")
        

