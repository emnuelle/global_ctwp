import re
import random
import json

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


def validar_cep(cep):
    # Regex para validar o formato do CEP xxxxxxxx
    padrao = re.compile(r'^\d{5}\d{3}$')
    return bool(padrao.match(cep))

# Função para validar e obter uma senha do usuário
def senha():
    while True:
        senha = input("Digite uma senha (com pelo menos um número e um caractere especial): ")
        confirmacao_senha = input("Digite novamente a senha para confirmar: ")

        if senha == confirmacao_senha and any(c.isdigit() for c in senha) and any(c in "!@#$%^&*()-_+=<>,.?/:;|[]{}`~" for c in senha):
            return senha
        else:
            print("Senha inválida. Certifique-se de que ela contenha pelo menos um número e um caractere especial, e que as duas inserções sejam iguais.")



def gerar_codigo_pulseira():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(6))

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
    
