import pip._vendor.requests as requests#Importando requests
from tkinter import *#importando a biblioteca python tkinter

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

janela = Tk()#Dizendo para o python que janela é uma 'tk'
janela.title("Cotação Atual de Moedas")#Alterando o título da janela
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")#definindo uma label
texto.grid(column=0, row=0, padx=10, pady=10)#definindo o tamanho de 'texto'

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)#definindo um botão e suas características
botao.grid(column=0, row=1, padx=10, pady=10)#definindo o tamanho do botão

texto_resposta = Label(janela, text="")#definindo a label que recebe a resposta
texto_resposta.grid(column=0, row=2, padx=10, pady=10)#definindo o tamanho do label de resposta


janela.mainloop()#definindo que a janela deve ficar rodando