def caixa_eletronico():
    while True:
        try:
            saque = float(input("Digite o valor do saque (máximo R$ 1000): R$ "))
            if saque <= 0:
                print("O valor do saque deve ser positivo.")
            elif saque > 1000:
                print("O valor do saque não pode ser maior que R$ 1000.")
            else:
                print(f"Saque realizado com sucesso: R$ {saque}")
                break
        except ValueError:
            print("Por favor, insira um valor válido.")

caixa_eletronico()
