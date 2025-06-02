import json
import os 

data = "funcionarios.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding= "utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    

funcionarios = carregar_dados()

for funcionario in funcionarios:
    if funcionario["salario"] >= 5500:
        print(f"Nome do funcinário: {funcionario["nome"]} Salário do funcionário: {funcionario["salario"]}")

    else:
        print("funcionario não encontrados. ")
