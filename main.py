from tkinter import *
from tkinter import ttk

adicionar_acoes = Tk()
adicionar_acoes.title('Adcionar Ações')
adicionar_acoes.configure(bg='#363636')
adicionar_acoes.geometry('1080x720')
label_nome_acao = Label(adicionar_acoes, text='Coloque o nome da ação', bg='#363636', fg='white')
label_nome_acao.grid(column=0, row=1, padx=1, pady=1)
nome_acao = Entry(adicionar_acoes, width=8)
nome_acao.grid(column=0, row=2, padx=1, pady=1)

label_valor_acao = Label(adicionar_acoes, text='Coloque o valor da ação', bg='#363636', fg='white')
label_valor_acao.grid(column=0, row=3, padx=1, pady=1)
valor_acao = Entry(adicionar_acoes, width=8)
valor_acao.grid(column=0, row=4, padx=1, pady=1)

label_quantidade_acao = Label(adicionar_acoes, text='Coloque a quantidade de ações', bg='#363636', fg='white')
label_quantidade_acao.grid(column=0, row=5, padx=1, pady=1)
quantidade_acao = Entry(adicionar_acoes, width=8)
quantidade_acao.grid(column=0, row=6, padx=1, pady=1)


adicionar_acoes.mainloop()