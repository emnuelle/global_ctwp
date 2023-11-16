import json
from utils import salvar_dados_json
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
        for usuario_id, usuario_data in usuarios.items():
            if usuario_data['login']['email_tutor'] == email and usuario_data['login']['senha'] == senha:
                usuario_encontrado = usuario_data
                break

        if usuario_encontrado:
            print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario_encontrado['dados_tutor']['nome_tutor']}!")
            menu_secundario(usuario_encontrado['dados_tutor']['nome_tutor'])
        else:
            tentativas += 1
            print("\nE-mail ou senha incorretos. Tente novamente.")

            if tentativas == 3:
                print("\nNúmero máximo de tentativas excedido. Redirecionando para o menu inicial.")
                break

            print(f"Você tem mais {3 - tentativas} tentativas restantes. Assim que forem ultrapassadas o sistema irá retornar ao menu inicial.")


def menu_secundario(user_data):
    while True:
        print("\nMenu Secundário")
        print("1. Adicionar informações")
        print("2. Alterar informações")
        print("3. Voltar ao menu inicial")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
          # adicionar_informacoes(user_data)
            print(1)
        elif escolha == '2':
            exibir_menu_alteracao(user_data)
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_alteracao(user_data):
    while True:
        print("\nMenu de Alteração:")
        print("1. Alterar email do tutor")
        print("2. Alterar senha do tutor")
        print("3. Alterar telefone do tutor")
        print("4. Alterar endereço do tutor")
        print("5. Alterar informações adicionais do tutor")
        print("6. Alterar informações da pulseira")
        print("7. Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            alterar_email_tutor(user_data)
        elif escolha == "2":
            alterar_senha_tutor(user_data)
        elif escolha == "3":
            alterar_telefone_tutor(user_data)
        elif escolha == "4":
            alterar_endereco_tutor(user_data)
        elif escolha == "5":
            alterar_info_adicional_tutor(user_data)
        elif escolha == "6":
            alterar_info_pulseira(user_data)
        elif escolha == "7":
            print("Saindo do menu de alteração.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def alterar_email_tutor(user_data):
    novo_email = input("Digite o novo email do tutor: ")
    user_data["login"]["email_tutor"] = novo_email
    salvar_dados_json(user_data)
    print("Email do tutor alterado com sucesso.")


def alterar_senha_tutor(user_data):
    novo_senha = input("Digite a nova senha do tutor: ")
    user_data["login"]["senha"] = novo_senha
    salvar_dados_json(user_data)
    print("Senha do tutor alterada com sucesso.")


def alterar_telefone_tutor(user_data):
    novo_telefone = input("Digite o novo telefone do tutor: ")
    user_data["dados_tutor"]["telefone_tutor"] = novo_telefone
    salvar_dados_json(user_data)
    print("Telefone do tutor alterado com sucesso.")


def alterar_endereco_tutor(user_data):
    print("Digite as novas informações de endereço do tutor:")

    novo_rua = input("Rua: ")
    novo_numero = input("Número: ")
    novo_cep = input("CEP (formato xxxxxxxx): ")
    novo_bairro = input("Bairro: ")
    nova_cidade = input("Cidade: ")
    novo_estado = input("Estado: ")

    # Atualiza as informações de endereço do tutor
    endereco_tutor = user_data["dados_tutor"]["endereco_tutor"]
    endereco_tutor["rua_tutor"] = novo_rua
    endereco_tutor["numero_tutor"] = novo_numero
    endereco_tutor["cep_tutor"] = novo_cep
    endereco_tutor["bairro_tutor"] = novo_bairro
    endereco_tutor["cidade_tutor"] = nova_cidade
    endereco_tutor["estado_tutor"] = novo_estado

    salvar_dados_json(user_data)
    print("Endereço do tutor alterado com sucesso.")


def alterar_info_adicional_tutor(user_data):
    print("Digite as novas informações adicionais do tutor:")

    novo_titulo = input("Título da informação adicional: ")
    nova_descricao = input("Descrição: ")

    # Atualiza as informações adicionais do tutor
    info_adicional_tutor = user_data["dados_tutor"]["informacoes_adicionais_tutor"]
    info_adicional_tutor["Titulo"] = novo_titulo
    info_adicional_tutor["Descricao"] = nova_descricao

    salvar_dados_json(user_data)
    print("Informações adicionais do tutor alteradas com sucesso.")



def alterar_info_pulseira(user_data):
    print("\nAlterar Informações da Pulseira:")

    pulseira_data = user_data["user1"]["pulseira1"]

    while True:
        print("\nMenu de Alteração da Pulseira:")
        print("1. Alterar nome do usuário")
        print("2. Alterar data de nascimento")
        print("3. Alterar tipo sanguíneo")
        print("4. Alterar alergias")
        print("5. Alterar vacinas")
        print("6. Alterar condições médicas")
        print("7. Alterar ocorrências médicas")
        print("8. Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            novo_nome = input("Digite o novo nome do usuário: ")
            pulseira_data["dados"]["nome"] = novo_nome
        elif escolha == "2":
            nova_data_nascimento = input("Digite a nova data de nascimento (ddmmaaaa): ")
            pulseira_data["dados"]["nascimento"] = nova_data_nascimento
        elif escolha == "3":
            novo_tipo_sanguineo = input("Digite o novo tipo sanguíneo: ")
            pulseira_data["dados"]["tipo_sanguineo"] = novo_tipo_sanguineo
        elif escolha == "4":
            alterar_alergias(pulseira_data)
        elif escolha == "5":
            alterar_vacinas(pulseira_data)
        elif escolha == "6":
            nova_condicao_medica = input("Digite a nova condição médica: ")
            pulseira_data["condicoes_medicas"] = nova_condicao_medica
        elif escolha == "7":
            alterar_ocorrencias_medicas(pulseira_data)
        elif escolha == "8":
            print("Saindo do menu de alteração da pulseira.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    salvar_dados_json(user_data)
    print("Informações da pulseira alteradas com sucesso.")









    
    


