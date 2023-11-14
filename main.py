import random
import re
import json


# Função do menu inicial
def menu_inicial():
    usuarios = []  # Mantenha uma lista de usuários cadastrados

    while True:
        print("\nHealth Tag")
        print("\nDigite uma opção:")
        print("(1) Login")
        print("(2) Cadastrar-se como Tutor")
        print("(3) Consultar")
        print("(4) Sair")

        escolha = int(input("Escolha uma opção: "))

        usuarios = carregar_usuarios()               

        if escolha == 1:
            login(usuarios)
        elif escolha == 2:
            usuarios = cadastrar_tutor(usuarios)
        elif escolha == 3:
            print("Opção de consulta")
        elif escolha == 4:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Por favor, escolha uma opção válida...")

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


def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file)

def validar_data_nascimento(data):
    # Regex para o formato ddmmaaaa
    padrao = re.compile(r"^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{4}$")
    return bool(padrao.match(data))

def validar_data_ocorrencia(data):
    # Regex para o formato ddmmaaaa
    padrao = re.compile(r"^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{4}$")
    return bool(padrao.match(data))

def validar_tipo_sanguineo(tipo_sanguineo):
    # Regex para validar tipo sanguíneo
    padrao = re.compile(r"^(A|B|AB|O)[\+-]?$")
    return bool(padrao.match(tipo_sanguineo.upper()))

def validar_email(email):
    # Regex para validar o formato do email
    padrao = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(padrao.match(email))

def validar_telefone(telefone):
    # Regex para validar números de telefone no formato xx9xxxxxxxx
    padrao = re.compile(r'^[0-9]{2}9[0-9]{8}$')
    return bool(padrao.match(telefone))

def validar_cep(cep):
    # Regex para validar o formato do CEP xxxxx-xxx
    padrao = re.compile(r'^\d{5}-\d{3}$')
    return bool(padrao.match(cep))

def gerar_codigo_pulseira():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(6))

def cadastrar_vacinas():
    vacinas_obrigatorias = ["Hepatite B", "BCG", "Tríplice Viral"]

    vacinas_recentes = []
    for vacina_obrigatoria in vacinas_obrigatorias:
        print(f"Você recebeu a vacina {vacina_obrigatoria} recentemente? (s/n): ")
        resposta = input().lower()

        if resposta == "s":
            vacinas_recentes.append(vacina_obrigatoria)

    # Retorna um dicionário com título e descrição genérica
    return {"titulo": "Vacinas Recentes", "descricao": "Lista de vacinas recentes:", "vacinas": vacinas_recentes}

def cadastrar_tutor(usuarios):
    print("Cadastro de Tutor")
    print()

    print("Nome Completo: ")
    nome_tutor = input()

    print("E-mail: ")
    email_tutor = input()
    while not validar_email(email_tutor):
        print("E-mail inválido. Digite novamente: ")
        email_tutor = input()

    print("Telefone (formato: xx9xxxxxxxx): ")
    telefone_tutor = input()
    while not validar_telefone(telefone_tutor):
        print("Telefone inválido. Digite novamente: ")
        telefone_tutor = input()

    print("Rua: ")
    rua_tutor = input()

    print("Número: ")
    numero_tutor = input()

    print("CEP (formato: xxxxx-xxx): ")
    cep_tutor = input()
    while not validar_cep(cep_tutor):
        print("CEP inválido. Digite novamente: ")
        cep_tutor = input()

    print("Bairro: ")
    bairro_tutor = input()

    print("Cidade: ")
    cidade_tutor = input()

    print("Estado: ")
    estado_tutor = input()

    print("Informações Adicionais: ")
    informacoes_adicionais_tutor = input()

    # Solicitando e validando a senha do usuário
    senha = obter_senha_valida()

    # Chame a função para cadastrar as pulseiras
    pulseiras = cadastrar_pulseira(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor, bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor)

    # Adicione as pulseiras ao usuário
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
        "senha": senha,  # Adicione a senha do usuário
        "pulseiras": pulseiras  # Adicione as pulseiras ao usuário
    }

    usuarios.append(usuario)

    print("Cadastro realizado com sucesso! Redirecionando para o menu inicial...")

# Função para validar e obter uma senha do usuário
def obter_senha_valida():
    while True:
        senha = input("Digite uma senha (com pelo menos um número e um caractere especial): ")
        confirmacao_senha = input("Digite novamente a senha para confirmar: ")

        if senha == confirmacao_senha and any(c.isdigit() for c in senha) and any(c in "!@#$%^&*()-_+=<>,.?/:;|[]{}`~" for c in senha):
            return senha
        else:
            print("Senha inválida. Certifique-se de que ela contenha pelo menos um número e um caractere especial, e que as duas inserções sejam iguais.")


def cadastrar_pulseira(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor, bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor):
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

        pulseira = cadastrar_pulseira_individual(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor, bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor)
        pulseira['codigo'] = codigo_pulseira

        pulseiras.append(pulseira)
        print(f"Pulseira cadastrada com sucesso! Código: {pulseira['codigo']}")

        primeira_pulseira = False

    return pulseiras


# Função atualizada para incluir as informações do tutor no usuário associado à pulseira
def cadastrar_pulseira_individual(nome_tutor, email_tutor, telefone_tutor, rua_tutor, numero_tutor, cep_tutor, bairro_tutor, cidade_tutor, estado_tutor, informacoes_adicionais_tutor):
    codigo_pulseira = gerar_codigo_pulseira()

    print(f"\nCadastrando pulseira com o id: {codigo_pulseira}")

    print("Cadastro do Usuário")
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
        print("Digite a primeira condição médica do usuário: ")
        condicao = input()

        if condicao:
            condicoes_medicas.append(condicao)
            break
        else:
            print("É necessário inserir pelo menos uma condição médica.")

    while True:
        print("Deseja adicionar mais uma condição médica? (s/n): ")
        opcao = input().lower()

        if opcao == "s":
            print("Digite a próxima condição médica: ")
            condicao = input()
            condicoes_medicas.append(condicao)
        elif opcao == "n":
            break
        else:
            print("Opção inválida. Por favor, escolha 's' para sim ou 'n' para não.")

    # Armazenando as ocorrências médicas do usuário
    ocorrencias_medicas = []
    while True:
        print("Ocorências médicas\nDigite os detalhes da última ocorrência médica:")

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
    print(f"{resultado_vacinas['titulo']}\n{resultado_vacinas['descricao']}")
    for vacina in resultado_vacinas['vacinas']:
        print(vacina)

     # Solicitando e validando a senha do usuário
    while True:
        senha = input("Digite uma senha (com pelo menos um número e um caractere especial): ")
        confirmacao_senha = input("Digite novamente a senha para confirmar: ")

        if senha == confirmacao_senha and any(c.isdigit() for c in senha) and any(c in "!@#$%^&*()-_+=<>,.?/:;|[]{}`~" for c in senha):
            break
        else:
            print("Senha inválida. Certifique-se de que ela contenha pelo menos um número e um caractere especial, e que as duas inserções sejam iguais.")

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
        "senha": senha  # Adicione a senha do usuário
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
        "usuario": usuario
    }

    print("Cadastro realizado com sucesso! Redirecionando para o menu inicial...")
    
    # Agora, chame a função menu_inicial para voltar ao menu inicial
    menu_inicial()

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

            print(f"Você tem mais {3 - tentativas} tentativas restantes.")

if __name__ == "__main__":
    menu_inicial()
