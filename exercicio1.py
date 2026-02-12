def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade <= 0:
                print("A idade deve ser maior que 0.")
            else:
                print(f"Idade válida: {idade}")
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

validar_idade()





        