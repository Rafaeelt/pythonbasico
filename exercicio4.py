def validar_quantidade():
    while True:
        try:
            idade = int(input("Digite a quantidade: "))
            if idade <= 0:
                print("A quantidade não pode ser 0 ou negativo.")
            else:
                print(f"Quantidade válida: {validar_quantidade}")
                break
        except ValueError:
            print("Por favor, insira uma quantidade válida de produtos.")

validar_quantidade()