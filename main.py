import json
from termo import aceitar_termos_privacidade
from fonte import validar_data_nascimento, validar_tipo_sanguineo, validar_email, validar_cep, cad_senha, gerar_pin_aleatorio, validar_cd_pulseira, gerar_coordenadas

def carregar_dados_json():
    try:
        with open("usuarios.json", "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def salvar_dados_json(usuarios):
    with open("usuarios.json", "w", encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4)

def cadastrar_usuario(usuarios):
    pin = gerar_pin_aleatorio()

    # Solicitar informações do usuário
    print("------------------------------------------------")
    print("  Adicione as informações do Tutor responsável  ")
    print("------------------------------------------------")
    senha = cad_senha()
    
    print("\nInformações de Contato\n")
    email_tutor = input("Digite o email do tutor: ")
    while not validar_email(email_tutor):
        print("Email inválido. Adicione email válido.")
        email_tutor = input("Email:")
        
    telefone_tutor = input("Digite o telefone do tutor: ")
    
    print("\nInformações de Endereço\n")
    rua_tutor = input("Digite a rua do tutor: ")
    numero_tutor = input("Digite o número do tutor: ")
    cep_tutor = input("Digite o CEP do tutor (formato xxxxxxxx): ")
    while not validar_cep(cep_tutor):
        print("Formato de CEP inválido. Digite novamente.")
        cep_tutor = input("CEP: (formato xxxxxxxx) ")
    bairro_tutor = input("Digite o bairro do tutor: ")
    cidade_tutor = input("Digite a cidade do tutor: ")
    estado_tutor = input("Digite o estado do tutor: ")
    
    resposta_infoad = input("\nDeseja adicionar alguma informação adicional no cadastro? (s/n)\n").lower()
    if resposta_infoad == 's':
        titulo_info_adicional = input("Título da informação adicional: ")
        descricao_info_adicional = input("Descrição: ")
    else:
        titulo_info_adicional = descricao_info_adicional = "Nenhuma informação adicionada."
    
    print("------------------------------------------------")
    print("  Informações sobre o usuário da pulseira  ")
    print("------------------------------------------------")
    cd_pulseira = input("Digite o código exibido na pulseira: (formato xxx.xxx.xxx-xx) ")
    while not validar_cd_pulseira(cd_pulseira):
        print("Código inválido. Por favor, tente novamente.")
        cd_pulseira = input("Digite o código exibido na pulseira: (formato xxx.xxx.xxx-xx) ")
    
    nome = input("Digite o nome completo do usuário: ")

    condicoes_medicas = input("Digite as condições médicas/de vulnerabilidade que o usuário se encontra: ")
    
    nascimento = input("Digite a data de nascimento (ddmmaaaa): ")
    while not validar_data_nascimento(nascimento):
        print("Formato inválido. Digite novamente.")
        nascimento = input("Data de nascimento (ddmmaaaa): ")
        
    tipo_sanguineo = input("Digite o tipo sanguíneo: ")
    while not validar_tipo_sanguineo(tipo_sanguineo):
        print("Resposta inválida. Digite novamente.")
        tipo_sanguineo = input("Tipo sanguíneo: ")
    
    resposta_medicamento = input("\nO usuário consome algum(ns) medicamento(s) regularmente? (s/n)\n").lower()
    if resposta_medicamento == 's':
        medicamentos = []
        while True:
            med_atual = input("Nome do(s) medicamento(s): ")
            tipo_med_atual = input("Tipo do(s) medicamento(s): ")
            qtd_med_atual = input("Quantidade do(s) medicamento(s): ")
            tp_med_atual = input("Tempo de uso do medicamento(s): ")

            medicamentos.append({
                "Nome": med_atual,
                "Tipo": tipo_med_atual,
                "Quantidade": qtd_med_atual,
                "Tempo": tp_med_atual
            })

            resposta_mais_medicamentos = input("\nDeseja adicionar mais medicamentos? (s/n)\n").lower()
            if resposta_mais_medicamentos != 's':
                break
    else:
        medicamentos = "Nenhuma informação registrada."
    
    resposta_alergia = input("\nDeseja adicionar alguma informação adicional no cadastro de alergia? (s/n)\n").lower()
    if resposta_alergia == 's':
        alergia = input("Alergia: ")
        alergia_esp = input("Adicione especificações: ")
    else:
        alergia = alergia_esp = "Nenhuma informação adicionada."
        
    while True:
        print("\nCadastro de Vacinas\n")

        nome_vacina = input("Digite o nome da última vacina tomada: ")
        data_vacina = input("Digite a data da última vacina tomada: ")
        descricao_vacina = input("Digite a descrição da última vacina tomada: ")
        local_vacina = input("Digite o local da última vacina tomada: ")

        resposta_mais_vacinas = input("\nDeseja cadastrar mais vacinas? (s/n)\n").lower()
        if resposta_mais_vacinas != 's':
            break
    
    # Informações específicas de ocorrências médicas
    resposta_ocorrencia = input("Deseja adicionar alguma ocorrência médica posterior relevante? (s/n)\n").lower()

    ocorrencias_medicas = {}
    if resposta_ocorrencia == 's':
        ocorrencias_medicas["Data"] = input("Data da ocorrência: ")
        ocorrencias_medicas["Local"] = input("Local da ocorrência (hospital, clínica, etc.): ")
        ocorrencias_medicas["Relato"] = input("Relato da ocorrência: ")
        ocorrencias_medicas["Sintomas"] = input("Sintomas que levaram à ocorrência: ")
        ocorrencias_medicas["Medicamentos"] = input("Medicamentos relacionados à ocorrência: ")
    else:
       ocorrencias_medicas = "Nenhuma informação registrada."

    
    # Adicionar informações do usuário ao dicionário
    usuarios[pin] = {
        "senha": senha,
        "data_tutor": {
            "email_tutor": email_tutor,
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
                "Titulo": titulo_info_adicional,
                "Descricao": descricao_info_adicional
            }
        },
        "pulseira": {
            "dados": {
                "codigo" : cd_pulseira,
                "nome": nome,
                "nascimento": nascimento,
                "tipo_sanguineo": tipo_sanguineo,
                "medicamentos": {
                    "Nome": med_atual,
                    "Tipo": tipo_med_atual,
                    "Quantidade": qtd_med_atual,
                    "Tempo": tp_med_atual
                },
                "alergias": {
                    "Alergia": alergia,
                    "Especificacao": alergia_esp
                },
                "vacinas": {
                    "nome": nome_vacina,
                    "data": data_vacina,
                    "descricao": descricao_vacina,
                    "local": local_vacina
                }
            },
            "condicoes_medicas": condicoes_medicas,
            "ocorrencias_medicas": ocorrencias_medicas
        }
    }

    salvar_dados_json(usuarios)
    print("-----------------------------------------------------------------------------")
    print(f"Usuário cadastrado com sucesso. Seu PIN é: {pin}, guarde ele com carinho. :)")
    print("-----------------------------------------------------------------------------")
    
    return pin


def login(usuarios):
    pin = input("Digite o seu PIN: ")
    senha = input("Digite a sua senha: ")

    if pin in usuarios and usuarios[pin]["senha"] == senha:
        print("Login bem-sucedido!")
        return pin
    else:
        print("PIN ou senha incorretos. Tente novamente.")
        return None

def menu_secundario(usuarios, usuario_encontrado):
    while True:
        print("\nMenu Secundário")
        print("1. Adicionar informações")
        print("2. Alterar informações")
        print("3. Consultar Informações")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_info_pulseira(usuarios, usuario_encontrado)
        elif escolha == '2':
            exibir_menu_alteracao(usuarios, usuario_encontrado)
        elif escolha == '3':
            consultar_por_pin(usuarios)
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def exibir_menu_alteracao(usuarios, usuario_encontrado):
    while True:
        print("\nMenu de Alteração:")
        print("1. Alterar email do tutor")
        print("2. Alterar senha do tutor")
        print("3. Alterar telefone do tutor")
        print("4. Alterar endereço do tutor")
        print("5. Alterar informações adicionais do tutor")
        print("6. Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            alterar_email_tutor(usuarios, usuario_encontrado)
        elif escolha == "2":
            alterar_senha_tutor(usuarios, usuario_encontrado)
        elif escolha == "3":
            alterar_telefone_tutor(usuarios, usuario_encontrado)
        elif escolha == "4":
            alterar_endereco_tutor(usuarios, usuario_encontrado)
        elif escolha == "5":
            alterar_info_adicional_tutor(usuarios, usuario_encontrado)
        elif escolha == "6":
            print("Saindo do menu de alteração.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def alterar_email_tutor(usuarios, usuario_encontrado):
    novo_email = input("Digite o novo email do tutor: ")
    usuario_encontrado["data_tutor"]["email_tutor"] = novo_email
    salvar_dados_json(usuarios)
    print("Email do tutor alterado com sucesso.")

def alterar_senha_tutor(usuarios, usuario_encontrado):
    novo_senha = input("Digite a nova senha do tutor: ")
    usuario_encontrado["senha"] = novo_senha
    salvar_dados_json(usuarios)
    print("Senha do tutor alterada com sucesso.")

def alterar_telefone_tutor(usuarios, usuario_encontrado):
    novo_telefone = input("Digite o novo telefone do tutor: ")
    usuario_encontrado["data_tutor"]["telefone_tutor"] = novo_telefone
    salvar_dados_json(usuarios)
    print("Telefone do tutor alterado com sucesso.")

def alterar_endereco_tutor(usuarios, usuario_encontrado):
    print("Digite as novas informações de endereço do tutor:")
    novo_rua = input("Rua: ")
    novo_numero = input("Número: ")
    novo_cep = input("CEP (formato xxxxxxxx): ")
    novo_bairro = input("Bairro: ")
    nova_cidade = input("Cidade: ")
    novo_estado = input("Estado: ")

    # Atualiza as informações de endereço do tutor
    endereco_tutor = usuario_encontrado["data_tutor"]["endereco_tutor"]
    endereco_tutor["rua_tutor"] = novo_rua
    endereco_tutor["numero_tutor"] = novo_numero
    endereco_tutor["cep_tutor"] = novo_cep
    endereco_tutor["bairro_tutor"] = novo_bairro
    endereco_tutor["cidade_tutor"] = nova_cidade
    endereco_tutor["estado_tutor"] = novo_estado

    salvar_dados_json(usuarios)
    print("Endereço do tutor alterado com sucesso.")

def alterar_info_adicional_tutor(usuarios, usuario_encontrado):
    print("Digite as novas informações adicionais do tutor:")
    novo_titulo = input("Título da informação adicional: ")
    nova_descricao = input("Descrição: ")

    # Atualiza as informações adicionais do tutor
    info_adicional_tutor = usuario_encontrado["data_tutor"]["informacoes_adicionais_tutor"]
    info_adicional_tutor["Titulo"] = novo_titulo
    info_adicional_tutor["Descricao"] = nova_descricao

    salvar_dados_json(usuarios)
    print("Informações adicionais do tutor alteradas com sucesso.")


def adicionar_info_pulseira(usuarios, usuario_encontrado):
    while True:
        print("\nAdicionar Informações:")
        print("1. Adicionar informações da pulseira")
        print("2. Adicionar condições médicas")
        print("3. Adicionar ocorrências médicas")
        print("4. Voltar ao menu anterior")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            adicionar_info_pulseira_opcao(usuarios, usuario_encontrado)
        elif escolha == "2":
            adicionar_condicoes_medicas(usuarios, usuario_encontrado)
        elif escolha == "3":
            adicionar_ocorrencias_medicas(usuarios, usuario_encontrado)
        elif escolha == "4":
            print("Voltando ao menu anterior.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def adicionar_info_pulseira_opcao(usuarios, usuario_encontrado):
    while True:
        print("\nMenu de Adição de Informações:")
        print("1. Adicionar informações sobre medicamentos")
        print("2. Adicionar informações sobre alergias")
        print("3. Adicionar informações sobre vacinas")
        print("4. Voltar ao menu anterior")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            adicionar_info_medicamentos(usuarios,usuario_encontrado)
        elif escolha == "2":
            adicionar_info_alergias(usuarios, usuario_encontrado)
        elif escolha == "3":
            adicionar_info_vacinas(usuarios, usuario_encontrado)
        elif escolha == "4":
            print("Voltando ao menu anterior.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_info_medicamentos(usuarios, usuario_encontrado):
    print("\nAdicionar informações sobre medicamentos:")
    usuario_encontrado["pulseira"]["dados"]["medicamentos"]["Nome"] = input("Nome do medicamento: ")
    usuario_encontrado["pulseira"]["dados"]["medicamentos"]["Tipo"] = input("Tipo de medicamento: ")
    usuario_encontrado["pulseira"]["dados"]["medicamentos"]["Quantidade"] = input("Quantidade: ")
    usuario_encontrado["pulseira"]["dados"]["medicamentos"]["Tempo"] = input("Tempo de uso: ")
    salvar_dados_json(usuarios)
    print("Informações sobre medicamentos atualizadas com sucesso.")

def adicionar_info_alergias(usuarios, usuario_encontrado):
    print("\nAdicionar informações sobre alergias:")
    usuario_encontrado["pulseira"]["dados"]["alergias"]["Alergia"] = input("Alergia: ")
    usuario_encontrado["pulseira"]["dados"]["alergias"]["Especificacao"] = input("Especificação: ")
    salvar_dados_json(usuarios)
    print("Informações sobre alergias atualizadas com sucesso.")

def adicionar_info_vacinas(usuarios, usuario_encontrado):
    print("\nAdicionar informações sobre vacinas:")
    usuario_encontrado["pulseira"]["dados"]["vacinas"]["nome"] = input("Nome da vacina: ")
    usuario_encontrado["pulseira"]["dados"]["vacinas"]["data"] = input("Data da vacinação (ddmmaaaa): ")
    usuario_encontrado["pulseira"]["dados"]["vacinas"]["descricao"] = input("Descrição: ")
    usuario_encontrado["pulseira"]["dados"]["vacinas"]["local"] = input("Local da vacinação: ")
    salvar_dados_json(usuarios)
    print("Informações sobre vacinas atualizadas com sucesso.")


def adicionar_condicoes_medicas(usuarios,usuario_encontrado):
    print("\nAdicionar Condições Médicas:")
    novas_condicoes_medicas = input("Informe as novas condições médicas/de vulnerabilidade que o usuário se encontra: ")
    usuario_encontrado["pulseira"]["condicoes_medicas"] = novas_condicoes_medicas
    salvar_dados_json(usuarios)
    print("Condições médicas atualizadas com sucesso.")


def adicionar_ocorrencias_medicas(usuarios, usuario_encontrado):
    print("\nAdicionar Ocorrências Médicas:")
    resposta_ocorrencia = input("\nDeseja adicionar alguma ocorrência médica posterior relevante? (s/n)\n").lower()

    if resposta_ocorrencia == 's':
        data_ocorrencia = input("Data da ocorrência (ddmmaaaa): ")
        local_ocorrencia = input("Local da ocorrência (hospital, clínica, etc.): ")
        relato_ocorrencia = input("Relato da ocorrência: ")
        sintomas_ocorrencia = input("Sintomas que levaram à ocorrência: ")

        # Informações sobre medicamentos da ocorrência
        print("\nInformações sobre medicamentos relacionados à ocorrência:")
        medicamentos_ocorrencia = {
            "Nome": input("Nome do medicamento: "),
            "Tipo": input("Tipo de medicamento: "),
            "Quantidade": input("Quantidade: "),
            "Tempo": input("Tempo de uso: ")
        }

        # Atualiza as ocorrências médicas da pulseira
        usuario_encontrado["pulseira"]["ocorrencias_medicas"] = {
            "Data": data_ocorrencia,
            "Local": local_ocorrencia,
            "Relato": relato_ocorrencia,
            "Sintomas": sintomas_ocorrencia,
            "Medicamentos": medicamentos_ocorrencia
        }

        salvar_dados_json(usuarios)
        print("Ocorrências médicas atualizadas com sucesso.")
    else:
        print("Nenhuma ocorrência médica adicionada.")


def consultar_por_pin(usuarios):
    pin_consulta = input("Digite o PIN do usuário que deseja consultar: ")

    if pin_consulta in usuarios:
        usuario_consultado = usuarios[pin_consulta]
        exibir_informacoes(usuario_consultado)
    else:
        print("PIN não encontrado.")
        
def exibir_informacoes(usuario):
    print("--------------------------")
    print("Informações do Usuário:")
    print("--------------------------")
    print(f"Nome: {usuario['pulseira']['dados']['nome']}")
    print(f"Nascimento: {usuario['pulseira']['dados']['nascimento']}")
    print(f"Tipo Sanguíneo: {usuario['pulseira']['dados']['tipo_sanguineo']}")
    print(f"Condições Médicas: {usuario['pulseira']['condicoes_medicas']}")
    print("--------------------------")
    print("Localização do bracelete:")
    coordenadas = gerar_coordenadas()
    print("Coordenadas da localização do dispositivo:", coordenadas)
    print("--------------------------")
    print("Medicamentos consumidos regularmente:")
    print(f"Nome: {usuario['pulseira']['dados']['medicamentos']['Nome']}")
    print(f"Tipo: {usuario['pulseira']['dados']['medicamentos']['Tipo']}")
    print(f"Quantidade: {usuario['pulseira']['dados']['medicamentos']['Quantidade']}")
    print(f"Tempo de Uso: {usuario['pulseira']['dados']['medicamentos']['Tempo']}")
    print("--------------------------")
    print("Alergias:")
    print(f"Alergia: {usuario['pulseira']['dados']['alergias']['Alergia']}")
    print(f"Especificação: {usuario['pulseira']['dados']['alergias']['Especificacao']}")
    
    print("--------------------------")
    print("Vacinas:")
    print(f"Nome: {usuario['pulseira']['dados']['vacinas']['nome']}")
    print(f"Data: {usuario['pulseira']['dados']['vacinas']['data']}")
    print(f"Descrição: {usuario['pulseira']['dados']['vacinas']['descricao']}")
    print(f"Local: {usuario['pulseira']['dados']['vacinas']['local']}")
    
    print("--------------------------")
    print("Ocorrências Médicas posteriores:")
    ocorrencias = usuario['pulseira']['ocorrencias_medicas']
    if isinstance(ocorrencias, dict):
        print(f"Data: {ocorrencias['Data']}")
        print(f"Local: {ocorrencias['Local']}")
        print(f"Relato: {ocorrencias['Relato']}")
        print(f"Sintomas: {ocorrencias['Sintomas']}")
        medicamentos_ocorrencia = ocorrencias['Medicamentos']
        print(f"Medicamentos Relacionados: {medicamentos_ocorrencia['Nome']}, {medicamentos_ocorrencia['Tipo']}, {medicamentos_ocorrencia['Quantidade']}, {medicamentos_ocorrencia['Tempo']}")
    else:
        print("Nenhuma ocorrência médica registrada.")


def main():
    usuarios = carregar_dados_json()

    while True:
        print("\nMenu Principal")
        print("1. Cadastrar novo usuário")
        print("2. Login")
        print("3. Consultar Informações")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            aceitar_termos_privacidade()
            cadastrar_usuario(usuarios)
        elif escolha == '2':
            pin_logado = login(usuarios)
            if pin_logado:
                usuario_encontrado = usuarios[pin_logado]
                menu_secundario(usuarios, usuario_encontrado)
        elif escolha == '3':
            consultar_por_pin(usuarios)
        elif escolha == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
