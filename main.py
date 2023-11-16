from cadastro import cadastrar_usuario
from utils import carregar_usuarios, salvar_usuarios
from login import login
from consulta import consulta

while True:
    print("\nHealth Tag")
    print("\nDigite uma opção:")
    print("(1) Login")
    print("(2) Cadastrar-se como Tutor")
    print("(3) Consultar")
    print("(4) Sair")

    escolha = input("\nEscolha uma opção: ")

    usuarios = carregar_usuarios()

    if escolha == "1":
        login(usuarios)
    elif escolha == "2":
        usuarios = cadastrar_usuario()
        salvar_usuarios(usuarios)
        print("Cadastro concluído. Retornando ao menu inicial.")
    elif escolha == "3":
        consulta()
    elif escolha == "4":
        print("Saindo do sistema. Até logo!")
        salvar_usuarios(usuarios)
        break
    else:
        print("Por favor, escolha uma opção válida...")
