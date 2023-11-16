from utils import (
    validar_data_nascimento,
    validar_tipo_sanguineo,
    validar_email,
    validar_cep,
    validar_data_ocorrencia,
    senha
)
from termo import aceitar_termos_privacidade
import json

contador_pulseiras = 1
contador_usuarios = 1

def gerar_id_pulseira():
    global contador_pulseiras
    id_pulseira = contador_pulseiras
    contador_pulseiras += 1
    return id_pulseira

def salvar_dados_json(dados):
    with open('usuarios.json', 'w', encoding='utf8') as file:
        json.dump(dados, file, indent=4)

def cadastrar_medicamento():
    resposta_medicamento = input("\nO usuário consome algum(ns) medicamento(s) regularmente? (s/n)\n").lower()

    if resposta_medicamento == 's':
        medicamentos = []
        while True:
            nome_medicamento = input("Nome do(s) medicamento(s): ")
            tipo_medicamento = input("Tipo do(s) medicamento(s): ")
            quantidade_medicamento = input("Quantidade do(s) medicamento(s): ")
            tempo_medicamento = input("Tempo de uso do medicamento(s): ")

            medicamentos.append({
                "Nome": nome_medicamento,
                "Tipo": tipo_medicamento,
                "Quantidade": quantidade_medicamento,
                "Tempo": tempo_medicamento
            })

            resposta_mais_medicamentos = input("\nDeseja adicionar mais medicamentos? (s/n)\n").lower()
            if resposta_mais_medicamentos != 's':
                break
    else:
        medicamentos = None

    return medicamentos

def cadastrar_vacinas():
    vacinas = []
    while True:
        print("\nCadastro de Vacinas\n")

        nome_vacina = input("Nome da vacina: ")
        data_vacina = input("Dia da aplicação: ")
        descricao_vacina = input("Descrição da vacina aplicada: ")
        local_vacinacao = input("Local de aplicação: ")

        vacinas.append({
            "nome": nome_vacina,
            "data": data_vacina,
            "descricao": descricao_vacina,
            "local": local_vacinacao
        })

        resposta_mais_vacinas = input("\nDeseja cadastrar mais vacinas? (s/n)\n").lower()
        if resposta_mais_vacinas != 's':
            break

    return vacinas

def cadastrar_usuario():
    global contador_usuarios

    if not aceitar_termos_privacidade():
        return None

    id_pulseira = gerar_id_pulseira()

    print("\nCadastro\n")
    print(f"\nSeu número de usuário é {contador_usuarios}, guarde ele com carinho.\n")
    print("\nAdicione as informações do Tutor responsável\n")

    email_tutor = input("Email: ")
    while not validar_email(email_tutor):
        print("Email inválido. Adicione email válido.")
        email_tutor = input("Email:")

    senha_tutor = senha()

    nome_tutor = input("Nome completo: ")
    
    telefone_tutor = input("Telefone: ")
    
    print("\nInformações de endereço\n")
    
    rua_tutor = input("Rua: ")
    
    numero_tutor = input("Número: ")
    
    cep_tutor = input("CEP: (formato xxxxxxxx) ")
    
    while not validar_cep(cep_tutor):
        print("Formato de CEP inválido. Digite novamente.")
        cep_tutor = input("CEP: (formato xxxxxxxx) ")

    bairro_tutor = input("Bairro: ")
    
    cidade_tutor = input("Cidade: ")
    
    estado_tutor = input("Estado: ")

    resposta_infoad = input("\nDeseja adicionar alguma informação adicional no cadastro? (s/n)\n").lower()

    if resposta_infoad == 's':
        titulo_info_adicional_tutor = input("Título da informação adicional: ")
        descricao_info_adicional_tutor = input("Descrição: ")
    else:
        titulo_info_adicional_tutor = descricao_info_adicional_tutor = None
    
    print("\nCadastro da pulseira\n")

    codigo_pulseira = input("Código presente na pulseira: ")
    
    print("\nInformações sobre o usuário da pulseira\n")

    nome_user = input("Nome completo: ")

    nasc_user = input("Data de nascimento (ddmmaaaa): ")
    while not validar_data_nascimento(nasc_user):
        print("Formato inválido. Digite novamente.")
        nasc_user = input("Data de nascimento (ddmmaaaa): ")

    tp_user = input("Tipo sanguíneo: ")
    while not validar_tipo_sanguineo(tp_user):
        print("Resposta inválida. Digite novamente.")
        tp_user = input("Tipo sanguíneo: ")

    medicamentos = cadastrar_medicamento()

    resposta_alergia = input("\nDeseja adicionar alguma informação adicional no cadastro de alergia? (s/n)\n").lower()

    if resposta_alergia == 's':
        alergia = input("Alergia: ")
        especificacao = input("Adicione especificações: ")
    else:
        alergia = especificacao = None
    
    vacinas = cadastrar_vacinas()

    condicoes_medicas = input("Informe a condição médica/de vulnerabilidade que o usuário se encontra: ")

    resposta_ocorrencia = input("\nDeseja adicionar alguma ocorrência média posterior relevante? (s/n)\n").lower()

    if resposta_ocorrencia == 's':
        data_ocorrencia = input("Data da ocorrência (ddmmaaaa): ")
        while not validar_data_ocorrencia(data_ocorrencia):
            print("Formato inválido, tente novamente.")
            data_ocorrencia = input("Data da ocorrência (ddmmaaaa): ")
            
        local_ocorrencia = input("Local da ocorrência (hospital, clínica, etc.): ")
        relato_ocorrencia = input("Relato da ocorrência: ")
        sintomas_ocorrencia = input("Sintomas que levaram à ocorrência: ")

        medicamentos_ocorrencia = cadastrar_medicamento()
    else:
        data_ocorrencia = local_ocorrencia = relato_ocorrencia = sintomas_ocorrencia = medicamentos_ocorrencia = None

    # Criar um dicionário com os dados do usuário
    user_data = {
        f"user{contador_usuarios}": {
            "login": {
                "email_tutor": email_tutor,
                "senha": senha_tutor
            },
            "dados_tutor": {
                "nome_tutor": nome_tutor,
                "telefone_tutor": telefone_tutor,
                "endereco_tutor": {
                    "rua_tutor": rua_tutor,
                    "numero_tutor": numero_tutor,
                    "cep_tutor": cep_tutor,
                    "bairro_tutor": bairro_tutor,
                    "cidade_tutor": cidade_tutor,
                    "estado_tutor": estado_tutor
                },
                "informacoes_adicionais_tutor": {
                    "Titulo": titulo_info_adicional_tutor,
                    "Descricao": descricao_info_adicional_tutor
                }
            },
            f"pulseira{id_pulseira}": {
                "codigo": codigo_pulseira,
                "dados": {
                    "nome": nome_user,
                    "nascimento": nasc_user,
                    "tipo_sanguineo": tp_user,
                    "medicamentos": medicamentos,
                    "alergias": {
                        "Alergia:": alergia,
                        "Especificacao": especificacao
                    },
                    "vacinas": vacinas
                },
                "condicoes_medicas": condicoes_medicas,
                "ocorrencias_medicas": {
                    "Data": data_ocorrencia,
                    "Local": local_ocorrencia,
                    "Relato": relato_ocorrencia,
                    "Sintomas": sintomas_ocorrencia,
                    "Medicamentos": medicamentos_ocorrencia
                }
            }
        }
    }

    contador_usuarios += 1
    
    salvar_dados_json(user_data)
    print("Cadastro concluído.")

    return user_data