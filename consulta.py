from utils import carregar_usuarios
import json

def exibir_informacoes_pulseira(codigo_pulseira, usuarios):
   pulseira_encontrada = None

   for usuario_id, usuario_data in usuarios.items():
       for pulseira_id, pulseira_data in usuario_data.items():
           if 'pulseira' in pulseira_id and 'codigo' in pulseira_data and pulseira_data['codigo'] == codigo_pulseira:
               pulseira_encontrada = pulseira_data
               break
        
        
   if pulseira_encontrada:
        print("\nInformações da Pulseira")
        print(f"Código da Pulseira: {pulseira_encontrada['codigo']}")

        # Exibe informações do usuário da pulseira
        if 'dados' in pulseira_encontrada:
            dados_usuario = pulseira_encontrada['dados']
            print("\nInformações sobre o usuário da pulseira")
            print(f"Nome: {dados_usuario['nome']}")
            print(f"Nascimento: {dados_usuario['nascimento']}")
            print(f"Tipo Sanguíneo: {dados_usuario['tipo_sanguineo']}")

            # Exibe todas as informações do tutor
            info_tutor = usuario_data.get('dados_tutor', {})
            if info_tutor:
                print("\nInformações do Tutor:")
                print(f"Nome: {info_tutor.get('nome_tutor', 'N/A')}")
                print(f"Telefone: {info_tutor.get('telefone_tutor', 'N/A')}")
                print("> Endereço:")
                endereco_tutor = info_tutor.get('endereco_tutor', {})
                print(f" Bairro: {endereco_tutor.get('bairro_tutor', 'N/A')}")
                print(f" Cidade: {endereco_tutor.get('cidade_tutor', 'N/A')}")
                print(f" Estado: {endereco_tutor.get('estado_tutor', 'N/A')}")
                print("> Informações Adicionais:")
                info_adicionais_tutor = info_tutor.get('informacoes_adicionais_tutor', {})
                print(f" Título: {info_adicionais_tutor.get('Titulo', 'N/A')}")
                print(f" Descrição: {info_adicionais_tutor.get('Descricao', 'N/A')}")
            else:
                print("Nenhuma informação do tutor encontrada.")


        # Exibe todas as condições médicas
        print("\nCondições Médicas:")
        print(pulseira_encontrada['condicoes_medicas'])

        # Exibe todas as ocorrências médicas
        print("\nOcorrências Médicas:")
        if pulseira_encontrada['dados']['medicamentos'] is not None:
            for ocorrencia in pulseira_encontrada['ocorrencias_medicas']:

                ocorrencia = json.loads(ocorrencia)
                print(f"Data: {ocorrencia['Data']}")
                print(f"Local: {ocorrencia['Local']}")
                print(f"Relato: {ocorrencia['Relato']}")
                print(f"Sintomas: {ocorrencia['Sintomas']}")
                print("Medicamentos Prescritos:")
                for medicamento in ocorrencia['Medicamentos']:
                    print("Medicamentos perc")
                    print(f" Nome: {medicamento['Nome']}")
                    print(f" Tipo: {medicamento['Tipo']}")
                    print(f" Quantidade: {medicamento['Quantidade']}")
                    print(f" Tempo de Consumo: {medicamento['Tempo']}")

        else:
            print("Nenhuma ocorrência registrada.")


        # Exibe todas as alergias
        print("\nAlergias:")
        for alergia in pulseira_encontrada['dados']['alergias']:
            if isinstance(alergia, dict):
                print(f"- {alergia['Alergia']}")
                if 'Especificacao' in alergia and alergia['Especificacao']:
                    print(f"  Especificação: {alergia['Especificacao']}")
            else:
                print(f"- {alergia}")

        # Exibe todas as vacinas
        print("\nVacinas:")
        for vacina in pulseira_encontrada['dados']['vacinas']:
            print(f"Nome: {vacina['nome']}")
            print(f"Data: {vacina['data']}")
            print(f"Descrição: {vacina['descricao']}")
            print(f"Local: {vacina['local']}")
            print()

        # Exibe todos os medicamentos
        print("\nMedicamentos:")
        if pulseira_encontrada['dados']['medicamentos'] is not None:
            for medicamento in pulseira_encontrada['dados']['medicamentos']:
                print(f"Nome: {medicamento['Nome']}")
                print(f"Tipo: {medicamento['Tipo']}")
                print(f"Quantidade: {medicamento['Quantidade']}")
                print(f"Tempo de Consumo: {medicamento['Tempo']}")
                print()
        else:
            print("Nenhum medicamento cadastrado.")

        # Exibe todas as informações do tutor
        print("\nInformações do Tutor:")
        if 'dados_tutor' in pulseira_encontrada:
            for chave, valor in pulseira_encontrada['dados_tutor'].items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("Nenhuma informação do tutor encontrada.")


def consulta():
    # Carrega os usuários do arquivo
    usuarios = carregar_usuarios()

    # Solicita o código da pulseira ao usuário
    codigo_digitado = input("Digite o código da pulseira: ")

    # Chama a função para exibir as informações da pulseira
    exibir_informacoes_pulseira(codigo_digitado, usuarios)
