clientes = []

def obter_dados_cliente():
    nome_cliente = ("informe o nome do cliente: ")
    CPF_cliente = int(input("informe o CPF do cliente: "))
    RG_cliente = int(input("informe o RG do cliente: "))
    Data_de_nascimento = input("informe a data de nascimento do cliente: ")
    endereco_cliente = input("informe o endereço do cliente: ")
    Cidade_cliente = input("informe a cidade do cliente: ")
    Estado_cliente = input("informe o estad do cliente: ")
    Telefone_cliente = int(input("informe o telefone do cliente: "))
    Celular_cilente = int(input("informe o celular do cliente: "))
    Email_cliente = input("informe o email do cliente: ")

    cliente = {
        "Nome_cliente": nome_cliente,
        "CPF_cliente": nome_cliente,
        "RG_cliente": nome_cliente,
        "Data_de_nascimento" : nome_cliente,
        "Endereco_cliente": nome_cliente,
        "Cidade_cliente": nome_cliente,
        "Estado_cliente": nome_cliente,
        "Telefone_cliente": nome_cliente,
        "Celular_cliente": nome_cliente,
        "Email_cliente": nome_cliente
    }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clientes(dados_clientes):
    for clientes in dados_clientes:
        print(f"""
              nome do cliente: {clientes["nome_cliente"]}
        CPF do cliente: {clientes["CPF_cliente"]}
        RG do cliente: {clientes["RG_cliente"]}
        Data de nascimento do cliente: {clientes["Data de nascimento_cliente"]}
        Endereço do cliente: {clientes["Endereco_cliente"]}
        Cidade do cliente: {clientes["Cidade_cliente"]}
        Estado do cliente: {clientes["Estado_cliente"]}
        Telefone do cliente: {clientes["Telefone_cliente"]}
        Celular do cliente: {clientes["Celular_cliente"]}
        Email do cliente: {clientes["Email_cliente"]}
""")


def iniciar_sistema():
    while True:
        print("")
        print("="*80)
        print("opção 1 - Mostrar listade clientes")
        print("opção 2 - cadastrar clientes")
        print("opção 3 - sair do sistema")
        print("="*80)

        opcao = input("Escoçha umas das opções do menu: ")

        if opcao =="1":
            mostrar_dados_clientes(clientes)
        elif opcao =="2":
            cadastrar_cliente(obter_dados_cliente())
        elif opcao == "3":
            print("sistema finalizado!")
            break 
        else:
            print("opção invalida, escolha umas das opções no menu")

iniciar_sistema()
