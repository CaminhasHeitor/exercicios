from exercicios04 import somar_pares
 
alunos = []

def obter_dados_aluno():
    nome_aluno = input("informe o nome do aluno: ")
    email_aluno = input("informe o email do aluno: ")
    serie_aluno = input("informe a serie do aluno: ")
    nota01 = int(input("informe a primeira nota do aluno: "))
    nota02 = int(input("informe a segunda nota do aluno: "))
    nota03 = int(input("informe a terceira nota do aluno: "))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01, nota02, nota03)
def cadastrar_aluno(nome, email, serie,  nota01=0, nota02=0, nota03=0):

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
       "email": email,
       "serie": serie,
       "nota": [nota01, nota02, nota03],
       "media": somar_pares(notas)
    }
    alunos.append(aluno)
    
    return alunos 
    


def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
            print(f"Nome do Aluno: {aluno["nome"]} | Email do aluno: {aluno["email"]}  | Série do aluno:{aluno["serie"]} | Notas do aluno: {aluno["notas"]} | Média do aluno: {aluno["media "]}")

    return 


def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 => mostrar alunos cadastrados.")
        print("Opção 2 => cadastrar alunos.")
        print("Opção 3 => sair do sistema.")
        print("="*80)
        
        opcao = input("Escolha uma das opcções acima: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_aluno()
        else:
            print("sistema finalizado.")
            break

iniciar_sistema()






