import json
from utils import validar_data_nascimento, validar_tipo_sanguineo, gerar_codigo_pulseira, validar_email, validar_cep, validar_data_ocorrencia
from termo import aceitar_termos_privacidade
from login import login
from consulta import consultar_pulseira

usuarios = [] 
senha = None


# Função do menu inicial
def menu_inicial():
    global usuarios, senha

    while True:
        print("\nHealth Tag")
        print("\nDigite uma opção:")
        print("(1) Login")
        print("(2) Cadastrar-se como Tutor")
        print("(3) Consultar")
        print("(4) Sair")

        escolha = input("\nEscolha uma opção: ")

        usuarios = carregar_usuarios()

        if escolha == "1":
            login(usuarios)
        elif escolha == "2":
            usuarios = cadastrar_tutor(usuarios)
        elif escolha == "3":
            consultar_pulseira(usuarios)
        elif escolha == "4":
            print("Saindo do sistema. Até logo!")
            salvar_usuarios(usuarios)
            break
        else:
            print("Por favor, escolha uma opção válida...")


# Carregando os usuários no arquivo json, 
def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def salvar_usuarios_no_arquivo(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file)


def salvar_usuarios(usuarios):
    salvar_usuarios_no_arquivo(usuarios)


# Cadastrando as vacinas
def cadastrar_vacinas():
    vacinas_recentes = []

    print("\nCadastro de Vacinas: Informe ao menos as duas últimas aplicações.\n")

    while True:
        # Solicitação do nome da vacina
        nome_vacina = input("Digite o nome da vacina: ")

        # Solicitação da data da vacina
        while True:
            data_vacina = input("Digite a data da vacina (ddmmaaaa): ")
            if validar_data_nascimento(data_vacina):
                break
            else:
                print("Formato de data inválido. Digite novamente.")

        # Solicitação da descrição da vacina
        descricao_vacina = input("Digite uma descrição da vacina: ")

        # Solicitação do local da vacinação
        local_vacinacao = input("Digite o local da vacinação: ")

        vacina = {
            "nome": nome_vacina,
            "data": data_vacina,
            "descricao": descricao_vacina,
            "local": local_vacinacao
        }

        vacinas_recentes.append(vacina)

        print(f"Vacina '{nome_vacina}' cadastrada com sucesso!")

        resposta = input("Deseja cadastrar outra vacina? (s/n) ")

        if resposta.lower() == "n":
            break
        elif resposta.lower() != "s":
            print("Por favor, digite uma opção válida...\n")
            break  # Sai do loop se a resposta não for 's' nem 'n'

    # Verifica se foram cadastradas pelo menos duas vacinas
    if len(vacinas_recentes) < 2:
        print("Aviso: Foi cadastrada apenas uma vacina. Lembre-se de cadastrar ao menos duas para completar o registro.")

    print("Vacinas cadastradas com sucesso!")

        
# Cadastrando medicamentos 
def cadastrar_medicamentos():
    medicamentos = []

    while True:
        print("Digite o nome do medicamento (ou 'n' para encerrar): ")
        nome_medicamento = input()

        if nome_medicamento.lower() == 'n':
            break

        tipo_medicamento = input("Digite o tipo do medicamento: ")
        quantidade_medicamento = input("Digite a quantidade do medicamento: ")
        tempo_medicamento = input("Digite o tempo de consumo do medicamento: ")

        medicamento = {
            "Nome": nome_medicamento,
            "Tipo": tipo_medicamento,
            "Quantidade": quantidade_medicamento,
            "Tempo": tempo_medicamento
        }

        medicamentos.append(medicamento)

    return medicamentos


# Cadastrando tutores 
def cadastrar_tutor(usuarios):
    if not aceitar_termos_privacidade():
        return

    dados_tutor = obter_dados_tutor()
    senha = obter_senha_valida()

    pulseiras = cadastrar_pulseira(**dados_tutor, senha_tutor=senha)
    usuario = {**dados_tutor, "senha": senha, "pulseiras": pulseiras}

    # Adiciona as informações do tutor e da pulseira à lista de usuários
    usuarios.append(usuario)

    # Salva os usuários no arquivo JSON
    salvar_usuarios(usuarios)

    print("\nCadastro realizado com sucesso! Redirecionando para o menu inicial...\n")
    menu_inicial()


# Obtendo dados dos tutores
def obter_dados_tutor():
    nome_tutor = input("Digite o seu nome completo: ")
    
    # Solicitação do e-mail do tutor com validação
    while True:
        email_tutor = input("Digite o seu e-mail: ")
        if validar_email(email_tutor):
            break
        else:
            print("Formato de e-mail inválido. Digite novamente.")

    telefone_tutor = input("Digite o seu telefone: ")
    rua_tutor = input("Digite o nome da sua rua: ")
    numero_tutor = input("Digite o número da sua residência: ")
    
    # Solicitação do CEP do tutor com validação
    while True:
        cep_tutor = input("Digite o seu CEP: (formato: 00000000): ")
        if validar_cep(cep_tutor):
            break
        else:
            print("Formato de CEP inválido. Digite novamente.")

    bairro_tutor = input("Digite o nome do seu bairro: ")
    cidade_tutor = input("Digite o nome da sua cidade: ")
    estado_tutor = input("Digite o nome do seu estado: ")
    informacoes_adicionais_tutor = input("Digite informações adicionais (opcional): ")

    return {
        "nome_tutor": nome_tutor,
        "email_tutor": email_tutor,
        "telefone_tutor": telefone_tutor,
        "rua_tutor": rua_tutor,
        "numero_tutor": numero_tutor,
        "cep_tutor": cep_tutor,
        "bairro_tutor": bairro_tutor,
        "cidade_tutor": cidade_tutor,
        "estado_tutor": estado_tutor,
        "informacoes_adicionais_tutor": informacoes_adicionais_tutor
    }

# Função para validar e obter uma senha do usuário
def obter_senha_valida():
    while True:
        senha = input("Digite uma senha (com pelo menos um número e um caractere especial): ")
        confirmacao_senha = input("Digite novamente a senha para confirmar: ")

        if senha == confirmacao_senha and any(c.isdigit() for c in senha) and any(c in "!@#$%^&*()-_+=<>,.?/:;|[]{}`~" for c in senha):
            return senha
        else:
            print("Senha inválida. Certifique-se de que ela contenha pelo menos um número e um caractere especial, e que as duas inserções sejam iguais.")


# Função para cadastrar a pulseira
def cadastrar_pulseira(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor, bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor, senha_tutor):
    pulseiras = []
    primeira_pulseira = True

    while True:
        # Solicitação do código da pulseira
        if primeira_pulseira:
            print("Informe o código da pulseira (8 caracteres alfanuméricos): ")
        else:
            print("Deseja cadastrar outra pulseira? Informe o código da nova pulseira (8 caracteres alfanuméricos) ou 'n' para encerrar: ")

        codigo_pulseira = input().upper()

        if codigo_pulseira == 'N':
            break

        # Verifica se o código da pulseira já existe no cadastro
        if any(p['codigo'] == codigo_pulseira for p in pulseiras):
            print("Código da pulseira já cadastrado. Por favor, informe um novo código (8 caracteres alfanuméricos) ou 'n' para encerrar.")
            continue

        pulseira = cadastrar_pessoa(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor, bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor, senha_tutor, codigo_pulseira)

        pulseiras.append(pulseira)
        print(f"Pulseira cadastrada com sucesso! Código: {pulseira['codigo']}")

        primeira_pulseira = False

    return pulseiras


# Função para cadastrar uma pessoa individualmente
def cadastrar_pessoa(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor,
                      bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor, senha_tutor, codigo_pulseira):

    print(f"\nCadastrando pulseira com o id: {codigo_pulseira}")

    print("Cadastro do Usuário\n")
    print("Lembre-se que o usuário é quem vai carregar a pulseira.")
    print()

    print("Nome Completo: ")
    nome_user = input()

    # Validação da Data de Nascimento
    while True:
        print("Data de Nascimento (ddmmaaaa): ")
        nasc_user = input()

        if validar_data_nascimento(nasc_user):
            break
        else:
            print("Formato de data inválido. Digite novamente.")

    # Validação do Tipo Sanguíneo
    while True:
        print("Insira o tipo sanguíneo (A, B, AB, O, com ou sem sinal): ")
        tp_user = input()

        if validar_tipo_sanguineo(tp_user):
            break
        else:
            print("Tipo sanguíneo inválido. Digite novamente.")

    # Armazenando as condições médicas do usuário
    condicoes_medicas = []
    while True:
        print("Digite a primeira condição médica/de vulnerabilidade do usuário: ")
        condicao = input()

        if condicao:
            condicoes_medicas.append(condicao)
            break
        else:
            print("É necessário inserir pelo menos uma condição médica.")

    while True:
        print("Deseja adicionar mais uma condição médica/de vulnerabilidade? (s/n): ")
        opcao = input().lower()

        if opcao == "s":
            print("Digite a próxima condição médica/de vulnerabilidade: ")
            condicao = input()
            condicoes_medicas.append(condicao)
        elif opcao == "n":
            break
        else:
            print("Opção inválida. Por favor, escolha 's' para sim ou 'n' para não.")

    # Verifica se a pessoa toma algum medicamento
    print("A pessoa toma algum medicamento? (s/n): ")
    resposta_medicamento = input().lower()

    medicamentos_pulseira = []
    if resposta_medicamento == "s":
        medicamentos_pulseira = cadastrar_medicamentos()

    # Armazenando as ocorrências médicas do usuário
    ocorrencias_medicas = []
    while True:
        print("Ocorrências médicas\nDigite os detalhes da última ocorrência médica:")

        while True:
            data_ocorrencia = input("Data da ocorrência (ddmmaaaa): ")
            if validar_data_ocorrencia(data_ocorrencia):
                break
            else:
                print("Formato de data inválido. Digite novamente.")

        local_ocorrencia = input("Local da ocorrência (hospital, clínica, etc.): ")

        relato_ocorrencia = input("Relato da ocorrência: ")

        medicamentos_ocorrencia = []
        while True:
            print("Deseja adicionar um medicamento prescrito? (s/n): ")
            opcao_medicamento = input().lower()

            if opcao_medicamento == "s":
                medicamento_nome = input("Nome do medicamento: ")
                medicamento_tipo = input("Tipo do medicamento: ")
                medicamento_quantidade = input("Quantidade prescrita: ")
                medicamento_tempo = input("Tempo de consumo: ")

                medicamento = {
                    "Nome": medicamento_nome,
                    "Tipo": medicamento_tipo,
                    "Quantidade": medicamento_quantidade,
                    "Tempo": medicamento_tempo
                }

                medicamentos_ocorrencia.append(medicamento)
            elif opcao_medicamento == "n":
                break
            else:
                print("Opção inválida. Por favor, escolha 's' para sim ou 'n' para não.")

        sintomas_ocorrencia = input("Sintomas que levaram à ocorrência: ")

        ocorrencia = {
            "Data": data_ocorrencia,
            "Local": local_ocorrencia,
            "Relato": relato_ocorrencia,
            "Medicamentos": medicamentos_ocorrencia,
            "Sintomas": sintomas_ocorrencia
        }

        ocorrencias_medicas.append(ocorrencia)

        print("\nOcorrência médica registrada com sucesso!")

        print("Deseja adicionar mais uma ocorrência médica? (s/n): ")
        opcao_ocorrencia = input().lower()

        if opcao_ocorrencia != "s":
            break

    # Coletando alergias do usuário
    alergias = []
    print("Você possui alguma alergia? (s/n): ")
    resposta_alergias = input().lower()

    if resposta_alergias == "s":
        while True:
            print("Digite a alergia do usuário: ")
            alergia = input()

            if alergia:
                especificacao = input("Especificações da alergia (se houver): ")
                alergia_info = {"Alergia": alergia, "Especificacao": especificacao}
                alergias.append(alergia_info)

                print("Deseja adicionar mais uma alergia? (s/n): ")
                opcao_alergia = input().lower()

                if opcao_alergia != "s":
                    break
            else:
                break

    # Cadastrando as últimas vacinas
    resultado_vacinas = cadastrar_vacinas()

    if resultado_vacinas:
        print(f"{resultado_vacinas['titulo']}\n{resultado_vacinas['descricao']}")
        for vacina in resultado_vacinas['vacinas']:
            print(vacina)
    else:
        print("Erro ao cadastrar vacinas.")

    # Copie as informações do tutor para o usuário
    usuario = {
        "nome_tutor": nome_tutor,
        "email_tutor": email_tutor,
        "telefone_tutor": telefone_tutor,
        "rua_tutor": rua_tutor,
        "numero_tutor": numero_tutor,
        "cep_tutor": cep_tutor,
        "bairro_tutor": bairro_tutor,
        "cidade_tutor": cidade_tutor,
        "estado_tutor": estado_tutor,
        "informacoes_adicionais_tutor": informacoes_adicionais_tutor,
        "senha": senha_tutor  # Adicione a senha do usuário
    }

    pulseira = {
        "codigo": codigo_pulseira,
        "nome": nome_user,
        "nascimento": nasc_user,
        "tipo_sanguineo": tp_user,
        "condicoes_medicas": condicoes_medicas,
        "ocorrencias_medicas": ocorrencias_medicas,
        "alergias": alergias,
        "vacinas_recentes": resultado_vacinas,
        "medicamentos": medicamentos_pulseira,  # Adiciona os medicamentos à pulseira
        "usuario": usuario
    }

    print("Cadastro realizado com sucesso! Redirecionando para o menu inicial...")

    # Agora, chame a função menu_inicial para voltar ao menu inicial
    menu_inicial()
    return pulseira
