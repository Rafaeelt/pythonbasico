def realizar_login():
    while True:
        usuario = input("Digite o nome de usuário: ")
        if not usuario:
            print("O campo usuário não pode ser vazio.")
            continue
        senha = input("Digite a senha (mínimo 6 caracteres): ")
        if len(senha) < 6:
            print("A senha deve ter no mínimo 6 caracteres.")
            continue
        print("Login cadastrado com sucesso!")
        break

realizar_login()