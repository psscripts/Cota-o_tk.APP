import requests
from tkinter import *
import os


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['ask']
    cotacao_euro = requisicao_dic['EURBRL']['bid']

    texto_resposta['text'] = f'''
    DÓLAR: {cotacao_dolar}
    EURO: {cotacao_euro}'''
    
janela = Tk()


janela.title("COTAÇÃO DE MOEDAS")#titulo

janela.resizable(False, False)

janela.configure(background="#006")

texto = Label(janela, font=('arial', 9, 'bold'),text="CLIQUE NO BOTÃO PARA VER AS COTAÇOES!", background="#009",foreground="#fff")#texto



texto_inst = Label(janela, font=("arial", 7, 'bold'), text="O app criado para te mostrar resultados da cotacao", background='#008', foreground='#fff')
texto_inst.place(x=30, y=900)


#texto.place(x=10,y=10,width=300,height=20)
texto.grid(column=0, row=0, padx=10, pady=19)


#Botoes
botao = Button(janela,font=('arial', 9, 'bold'),text="BUSCAR COTAÇÃO", command=pegar_cotacoes)#botão 
botao.grid(column=0, row=2, padx=10, pady=10)
botao.place(x=190, y=600)


#texto de respotas
texto_resposta = Label(janela, text="", background="#006",foreground="#fff")#texto
texto_resposta.place(x=220, y=700)

janela.mainloop()