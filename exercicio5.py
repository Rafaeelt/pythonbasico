while True:
    try:
        qtd = int(input("Digite a quantidade de produtos (inteiro positivo): "))
        if qtd > 0:
            print(f"Quantidade válida: {qtd}")
            break
        else:
            print("Erro: A quantidade deve ser maior que zero.")
    except ValueError:
        print("Erro: Digite apenas números inteiros.")