while True:
    print("1- Cadastrar")
    print("2- Consultar")
    print("3- sair")

    opcao = input("Escolha uma opção: ")

    if opção in ["1", "2", "3"]:
        break
    else:
        print("Opção inválida! - escolha novamente")

print("Você escolheu: ",opcao)