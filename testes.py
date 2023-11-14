import random
import re

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

def cadastrar_vacinas():
    vacinas_obrigatorias = ["Hepatite B", "BCG", "Tríplice Viral"]

    vacinas_recentes = []
    for vacina_obrigatoria in vacinas_obrigatorias:
        print(f"Você recebeu a vacina {vacina_obrigatoria} recentemente? (s/n): ")
        resposta = input().lower()

        if resposta == "s":
            vacinas_recentes.append(vacina_obrigatoria)

    return vacinas_recentes

def cadastro():
    numero_id = ''.join(str(random.randint(0, 9)) for _ in range(5))

    print()
    print("Seu ID é: " + numero_id)
    print()

    print("Dados do usuário")
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
    vacinas_recentes = cadastrar_vacinas()

    # Exibindo as informações do usuário
    print("\nInformações do Usuário:")
    print(f"Nome: {nome_user}")
    print(f"Data de Nascimento: {nasc_user}")
    print(f"Tipo Sanguíneo: {tp_user}")
    print("\nCondições Médicas:")
    for i, condicao in enumerate(condicoes_medicas, start=1):
        print(f"{i}. {condicao}")
    print("\nOcorrências Médicas:")
    for i, ocorrencia in enumerate(ocorrencias_medicas, start=1):
        print(f"\nOcorrência {i}:")
        print(f"  Data: {ocorrencia['Data']}")
        print(f"  Local: {ocorrencia['Local']}")
        print(f"  Relato: {ocorrencia['Relato']}")
        if ocorrencia["Medicamentos"]:
            print("  Medicamentos Prescritos:")
            for medicamento in ocorrencia["Medicamentos"]:
                print(f"    - {medicamento['Nome']} ({medicamento['Tipo']}), {medicamento['Quantidade']} por {medicamento['Tempo']}")
        print(f"  Sintomas: {ocorrencia['Sintomas']}")

    # Exibindo alergias, se houver
    if alergias:
        print("\nAlergias:")
        for alergia_info in alergias:
            print(f"  Alergia: {alergia_info['Alergia']}, Especificação: {alergia_info['Especificacao']}")

    # Exibindo as últimas vacinas
    if vacinas_recentes:
        print("\nÚltimas Vacinas:")
        for vacina_recente in vacinas_recentes:
            print(f"  {vacina_recente}")

# Exemplo de uso
cadastro()
