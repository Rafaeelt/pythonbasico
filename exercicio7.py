while True:
    try:
        ano = int(input("Digite o ano de nascimento: "))
        if 1900 < ano <= 2026:
            print(f"Ano válido: {ano}")
            break
        else:
            print("Erro: O ano deve estar entre 1901 e 2026.")
    except ValueError:
        print("Erro: Digite apenas números.")