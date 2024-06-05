Menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:

    opcao = input (Menu)

    if opcao == "d":
        print("Deposito\n")
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0: 
            saldo += valor 
            extrato += f"Deposito R$: {valor:.2f}\n"

        else:
            print("Operação falhou, valor invalido para deposito.")


    elif opcao == "s":
        print("Sacar")
        valor = float(input("Informe o valor de saque: "))


        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif numero_saque  > limite_saque:
            print("Operação falhou! Quantidade de saques excedido.")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou, valor invalido para deposito.")

    elif opcao == "e":
        print("\n========= EXTRATO =========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$: {saldo:.2f}")
        print("=================================")


    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação invalida, por favor selecione a operação desejada.")