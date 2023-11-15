# Função para fazer o login
def login(usuarios):
    print("\nLogin")
    print()

    tentativas = 0

    while tentativas < 3:
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        # Verifica se o email e a senha correspondem a algum usuário cadastrado
        usuario_encontrado = None
        for pulseira in usuarios:
            if pulseira['usuario']['email_tutor'] == email and pulseira['usuario']['senha'] == senha:
                usuario_encontrado = pulseira['usuario']
                break

        if usuario_encontrado:
            print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario_encontrado['nome_tutor']}!")
            # Aqui você pode adicionar as ações que deseja após o login, por exemplo, exibir um menu específico.
            break
        else:
            tentativas += 1
            print("\nE-mail ou senha incorretos. Tente novamente.")

            if tentativas == 3:
                print("\nNúmero máximo de tentativas excedido. Redirecionando para o menu inicial.")
                break

            print(f"Você tem mais {3 - tentativas} tentativas restantes. Assim que forem ultrapassadas os sistema irá retornar ao menu inicial.")
            
