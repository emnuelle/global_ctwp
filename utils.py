import re
import random

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


def gerar_codigo_pulseira():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(6))