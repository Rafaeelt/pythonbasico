while True:
    try:
        altura = float(input("Digite a altura em metros (ex: 1.75): "))
        if altura > 0:
            print(f"Altura válida: {altura}m")
            break
        else:
            print("Erro: A altura deve ser maior que zero.")
    except ValueError:
        print("Erro: Digite um número decimal válido (use ponto).")