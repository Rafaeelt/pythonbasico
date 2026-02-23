while True:
    try:
        parcelas = int(input("Digite o número de parcelas (1 a 12): "))
        if 1 <= parcelas <= 12:
            print(f"Número de parcelas aceito: {parcelas}")
            break
        else:
            print("Erro: Escolha um valor entre 1 e 12.")
    except ValueError:
        print("Erro: Digite apenas números.")