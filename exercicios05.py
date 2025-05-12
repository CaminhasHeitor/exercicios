from exercicios04 import somar_pares

def cadastrar_aluno(nome, email, serie,  nota01, nota02, nota03):
    alunos = []

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
    
print(cadastrar_aluno("caminhão", "00001107322145", "2ºTB"))






