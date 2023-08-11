# Criar um sistema bancário com as operações: sacar; depositar e visualizar extrato.
# Depositar: deve ser possível depositar apenas valores positivos; todos os depositos devem ser armazenados em uma váriavel e exibidos no extrato.
# Sacar: máximo de 3 saques diários; limite máximo de R$500,00 por saque; caso não tenha saldo em conta exibir mensagem informando que não é possível sacar; todos os saques devem ser armazenados em uma váriavel e exibidos no extrato.
# Extrato: listar todos depositos e saques; no fim da lista deve ser exibido o saldo atual no formato R$ xxx.xx

menu = """
    Escolha uma operação:

    [1] Depositar
    [2] Sacar
    [3] Exibir Extrato
    [0] Sair

    =>"""

saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Informe o valor a ser depositado: R$"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito realizado com sucesso no valor de: R$ {deposito:.2f}\n"

        else:
            print("Operação falhou, informe um valor válido!")

    elif opcao == "2":
        saque = float(input("Informe o valor a ser sacado: R$"))

        if saque > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif saque > 500:
            print("Operação falhou! O valor do saque excedeu o limite por saque.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número de saques excedeu o limite por dia.")
        
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque realizado com sucesso no valor de: R$ {saque:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n===== EXTRATO ======")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nO valor do seu extrato é: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por ser nosso cliente, volte sempre!")
        break

    else:
        print("Operação inválida, favor selecionar outra opção!")