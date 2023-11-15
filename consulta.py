import json

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


def consultar_pulseira(usuarios):
    while True:

        print("\nConsulta de Pulseira")
        print("\nDigite o código da pulseira ou 'b' para voltar ao Menu Inicial: ")
        
        codigo_pulseira = input().upper()

        if codigo_pulseira == 'B':
            break  # Sair da função e voltar ao menu inicial

        pulseira_encontrada = None
        for pulseira in usuarios:
            if 'codigo' in pulseira and pulseira['codigo'] == codigo_pulseira:
                pulseira_encontrada = pulseira
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
    usuarios = carregar_usuarios()

    print("\nInformações da Pulseira")
    print(f"Código da Pulseira: {pulseira['codigo']}")
    print(f"Nome do Usuário: {pulseira['nome']}")
    print(f"Data de Nascimento: {pulseira['nascimento']}")
    print(f"Tipo Sanguíneo: {pulseira['tipo_sanguineo']}")
    
    # Display other information as needed
    
    # Display conditions médicas
    print("\nCondições Médicas:")
    for condicao in pulseira['condicoes_medicas']:
        print(f"- {condicao}")

    # Display ocorrências médicas
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

    # Display alergias
    print("\nAlergias:")
    for alergia in pulseira['alergias']:
        print(f"- {alergia['Alergia']}")
        if 'Especificacao' in alergia and alergia['Especificacao']:
            print(f"  Especificação: {alergia['Especificacao']}")

    # Display vacinas recentes
    print("\nVacinas Recentes:")
    print(f"{pulseira['vacinas_recentes']['titulo']}")
    print(f"{pulseira['vacinas_recentes']['descricao']}")
    for vacina in pulseira['vacinas_recentes']['vacinas']:
        print(f"  - Nome: {vacina['nome']}")
        print(f"    Data: {vacina['data']}")
        print(f"    Descrição: {vacina['descricao']}")
        print(f"    Local: {vacina['local']}")
    
    # Display medicamentos
    print("\nMedicamentos:")
    for medicamento in pulseira['medicamentos']:
        print(f"Nome: {medicamento['Nome']}")
        print(f"Tipo: {medicamento['Tipo']}")
        print(f"Quantidade: {medicamento['Quantidade']}")
        print(f"Tempo de Consumo: {medicamento['Tempo']}")
        print()

    # Display informações do tutor
    print("\nInformações do Tutor:")
    print(f"Nome: {pulseira['usuario']['nome_tutor']}")
    print(f"E-mail: {pulseira['usuario']['email_tutor']}")
    print(f"Telefone: {pulseira['usuario']['telefone_tutor']}")
    print(f"Endereço: {pulseira['usuario']['rua_tutor']}, {pulseira['usuario']['numero_tutor']}")
    print(f"CEP: {pulseira['usuario']['cep_tutor']}")
    print(f"Bairro: {pulseira['usuario']['bairro_tutor']}")
    print(f"Cidade: {pulseira['usuario']['cidade_tutor']}")
    print(f"Estado: {pulseira['usuario']['estado_tutor']}")
    print(f"Informações Adicionais: {pulseira['usuario']['informacoes_adicionais_tutor']}")
