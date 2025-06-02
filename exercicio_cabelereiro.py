import json
import os 

agendamento = "agenda_cabeleireiro.json"

def carregar_dados():
    if os.path.exists(cadastro):
        with  open(cadastro, "r", encoding="utf-8)") as arq_json:
            return json.looad(arq_json)
    else:
        return []
def obter_dados():
    nome = input("informe seu nome: ")
    serviço_desejado = ("escolha o serviço desejado: ")
    data_do_agendamento = ("escolha o dia do corte: ")
    horario_do_agendamento = ("escolha o horario do corte")
    opções = ("escolha as observações do corte: ")