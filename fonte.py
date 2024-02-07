import re
import random


def gerar_coordenadas():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude


def validar_cd_pulseira(cpf):
    
    pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

    if pattern.match(cpf):
        
        cpf_numeros = re.sub(r'[^\d]', '', cpf)

        soma = 0
        for i in range(9):
            soma += int(cpf_numeros[i]) * (10 - i)
        resto = (soma * 10) % 11 if soma % 11 != 0 else 0

        if resto == int(cpf_numeros[9]):
            soma = 0
            for i in range(10):
                soma += int(cpf_numeros[i]) * (11 - i)
            resto = (soma * 10) % 11 if soma % 11 != 0 else 0

            if resto == int(cpf_numeros[10]):
                return True
    return False

def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin

def validar_data_nascimento(data):
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


def cad_senha():
    while True:
        senha = input("Digite uma senha para o acesso (com pelo menos um número e um caractere especial): ")
        confirmacao_senha = input("Digite novamente a senha para confirmar: ")

        if senha == confirmacao_senha and any(c.isdigit() for c in senha) and any(c in "!@#$%^&*()-_+=<>,.?/:;|[]{}`~" for c in senha):
            return senha
        else:
            print("Senha inválida. Certifique-se de que ela contenha pelo menos um número e um caractere especial, e que as duas inserções sejam iguais.")

def validar_cpf(cpf):
    """
    Valida um CPF no formato 'xxx.xxx.xxx-xx', onde x é um dígito.
    Retorna True se o CPF for válido, False caso contrário.
    """
    # Expressão regular para validar CPF
    pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

    # Verifica se o CPF corresponde ao padrão
    if pattern.match(cpf):
        # Remove pontos e traço para obter apenas os dígitos
        cpf_numeros = re.sub(r'[^\d]', '', cpf)

        # Verifica se o CPF é válido usando a fórmula específica
        soma = 0
        for i in range(9):
            soma += int(cpf_numeros[i]) * (10 - i)
        resto = (soma * 10) % 11 if soma % 11 != 0 else 0

        if resto == int(cpf_numeros[9]):
            soma = 0
            for i in range(10):
                soma += int(cpf_numeros[i]) * (11 - i)
            resto = (soma * 10) % 11 if soma % 11 != 0 else 0

            if resto == int(cpf_numeros[10]):
                return True

    return False

