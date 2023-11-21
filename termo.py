# Temo de privacidade 
def aceitar_termos_privacidade():
    print("\nTermos de Privacidade\n")
    
    print("Por favor, leia atentamente.\n")

    print("Ao utilizar o aplicativo Health Tag, você concorda com os seguintes termos de privacidade. Estes termos detalham como suas informações pessoais serão coletadas, usadas, compartilhadas e protegidas.\n")
    
    print("""
    >Coleta de Informações:

    O Health Tag coleta informações fornecidas por você durante o processo de cadastro, incluindo nome, e-mail, telefone e endereço.Dados de saúde, como condições médicas, ocorrências médicas, alergias, vacinas recentes e medicamentos, são armazenados para
    fornecer serviços personalizados.
        
    > Uso de Informações:

    As informações coletadas são usadas para criar perfis de saúde personalizados e fornecer funcionalidades relevantes dentro do aplicativo.
    Seus dados de saúde podem ser compartilhados com profissionais de saúde em situações de emergência, com o objetivo de fornecer
    cuidados adequados e rápidos.
        
    > Segurança:

    Implementamos medidas de segurança rigorosas para proteger suas informações contra acesso não autorizado, divulgação, alteração e destruição.
    O acesso às suas informações é restrito a membros autorizados da equipe do Health Tag e, quando apropriado, a profissionais de saúde.
        
    > Compartilhamento de Informações:

    Suas informações não serão vendidas, alugadas ou compartilhadas com terceiros para fins comerciais.
    Em situações de emergência médica, suas informações de saúde podem ser compartilhadas com profissionais de saúde para garantir a prestação de cuidados adequados.
        
    > Armazenamento de Dados:

    As informações coletadas são armazenadas de forma segura em servidores protegidos, seguindo as melhores práticas de segurança de dados.
        
    > Acesso e Atualização:

    Você tem o direito de acessar, corrigir ou excluir suas informações pessoais a qualquer momento.
    Mantenha suas informações atualizadas para garantir que os serviços do Health Tag sejam precisos e relevantes.
        
    > Termos de Aceitação:

    Ao usar o Health Tag, você concorda expressamente com estes termos de privacidade.
    Se você não concordar com estes termos, por favor, não utilize o aplicativo.
    Alterações nos Termos de Privacidade:

    O Health Tag se reserva o direito de modificar estes termos de privacidade a qualquer momento. Alterações significativas serão comunicadas de maneira apropriada.
        
    """)
    
    while True:
        aceitar = input("Você aceita os termos de privacidade? (s/n): ").lower()
        
        if aceitar == "s":
            print("Termos de privacidade aceitos. Prossiga com o cadastro.")
            break
        elif aceitar == "n":
            print("Você precisa aceitar os termos de privacidade para continuar.")
        else:
            print("Opção inválida. Por favor, digite 's' para aceitar ou 'n' para recusar.")