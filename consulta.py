from utils import carregar_usuarios

def consultar_pulseira():
    usuarios = carregar_usuarios()

    while True:
        print("\nConsulta de Pulseira")
        print("\nDigite o código da pulseira ou 'b' para voltar ao Menu Inicial: ")

        codigo_pulseira = input().upper()

        if codigo_pulseira == 'B':
            break  # Sair da função e voltar ao menu inicial

        pulseira_encontrada = None
        for usuario in usuarios:
            for pulseira_id, pulseira_data in usuario.items():
                if 'pulseira' in pulseira_id and 'codigo' in pulseira_data and pulseira_data['codigo'] == codigo_pulseira:
                    pulseira_encontrada = pulseira_data
                    break

        if pulseira_encontrada:
            exibir_informacoes_pulseira(pulseira_encontrada)
        else:
            print("Pulseira não encontrada. Verifique o código e tente novamente.")

        print("\nDeseja consultar outra pulseira? (s/n): ")
        opcao_continuar = input().lower()

        if opcao_continuar != 's':
            break  # Sair da função e voltar ao menu inicial

def exibir_informacoes_pulseira(pulseira):
    print("\nInformações da Pulseira")
    print(f"Código da Pulseira: {pulseira['codigo']}")
    print(f"Nome do Usuário: {pulseira['dados']['nome']}")
    print(f"Data de Nascimento: {pulseira['dados']['nascimento']}")
    print(f"Tipo Sanguíneo: {pulseira['dados']['tipo_sanguineo']}")

    # Adicione aqui a exibição de outras informações conforme necessário

    # Exibição de condições médicas
    print("\nCondições Médicas:")
    for condicao in pulseira['condicoes_medicas']:
        print(f"- {condicao}")

    # Exibição de ocorrências médicas
    print("\nOcorrências Médicas:")
    for ocorrencia in pulseira['ocorrencias_medicas']:
        print(f"Data: {ocorrencia['Data']}")
        print(f"Local: {ocorrencia['Local']}")
        print(f"Relato: {ocorrencia['Relato']}")
        print(f"Sintomas: {ocorrencia['Sintomas']}")
        print("Medicamentos Prescritos:")
        for medicamento in ocorrencia['Medicamentos']:
            print(f"  - Nome: {medicamento['Nome']}")
            print(f"    Tipo: {medicamento['Tipo']}")
            print(f"    Quantidade: {medicamento['Quantidade']}")
            print(f"    Tempo de Consumo: {medicamento['Tempo']}")
        print()

    # Exibição de alergias
    print("\nAlergias:")
    for alergia in pulseira['alergias']:
        print(f"- {alergia['Alergia']}")
        if 'Especificacao' in alergia and alergia['Especificacao']:
            print(f"  Especificação: {alergia['Especificacao']}")

    # Exibição de vacinas
    print("\nVacinas:")
    for vacina in pulseira['vacinas']:
        print(f"Nome: {vacina['nome']}")
        print(f"Data: {vacina['data']}")
        print(f"Descrição: {vacina['descricao']}")
        print(f"Local: {vacina['local']}")
        print()

    # Exibição de medicamentos
    print("\nMedicamentos:")
    for medicamento in pulseira['dados']['medicamentos']:
        print(f"Nome: {medicamento['Nome']}")
        print(f"Tipo: {medicamento['Tipo']}")
        print(f"Quantidade: {medicamento['Quantidade']}")
        print(f"Tempo de Consumo: {medicamento['Tempo']}")
        print()

    # Exibição de informações do tutor
    print("\nInformações do Tutor:")
    print(f"Nome: {pulseira['dados_tutor']['nome_tutor']}")
    print(f"E-mail: {pulseira['dados_tutor']['email_tutor']}")
    print(f"Telefone: {pulseira['dados_tutor']['telefone_tutor']}")
    print(f"Endereço: {pulseira['dados_tutor']['endereco_tutor']['rua_tutor']}, {pulseira['dados_tutor']['endereco_tutor']['numero_tutor']}")
    print(f"CEP: {pulseira['dados_tutor']['endereco_tutor']['cep_tutor']}")
    print(f"Bairro: {pulseira['dados_tutor']['endereco_tutor']['bairro_tutor']}")
    print(f"Cidade: {pulseira['dados_tutor']['endereco_tutor']['cidade_tutor']}")
    print(f"Estado: {pulseira['dados_tutor']['endereco_tutor']['estado_tutor']}")
    print(f"Informações Adicionais: {pulseira['dados_tutor']['informacoes_adicionais_tutor']}")
