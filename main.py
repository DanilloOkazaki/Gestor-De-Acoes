from sql import *
#criar a janela lista de ações
lista_de_acoes = Tk()
lista_de_acoes.title('Lista de Ações')
lista_de_acoes.configure(bg='#363636')
lista_de_acoes.geometry('500x400')

#criar  a janela para adicionar ações
adicionar_acoes = Tk()
adicionar_acoes.title('Adcionar Ações')
adicionar_acoes.configure(bg='#363636')
adicionar_acoes.geometry('500x400')

#cria uma label para o nome da ação
label_nome_acao = Label(adicionar_acoes, text='Coloque o nome da ação', bg='#363636', fg='white')
label_nome_acao.grid(column=0, row=1, padx=1, pady=1)
nome_acao = Entry(adicionar_acoes, width=8)
nome_acao.grid(column=0, row=2, padx=1, pady=1)

#cria uma label para o valor da ação
label_valor_acao = Label(adicionar_acoes, text='Coloque o valor da ação', bg='#363636', fg='white')
label_valor_acao.grid(column=0, row=3, padx=1, pady=1)
valor_acao = Entry(adicionar_acoes, width=8)
valor_acao.grid(column=0, row=4, padx=1, pady=1)

#cria uma label para quantidade de ações
label_quantidade_acao = Label(adicionar_acoes, text='Coloque a quantidade de ações', bg='#363636', fg='white')
label_quantidade_acao.grid(column=0, row=5, padx=1, pady=1)
quantidade_acao = Entry(adicionar_acoes, width=8)
quantidade_acao.grid(column=0, row=6, padx=1, pady=1)
#botão adicionar
botao_adicionar = Button(adicionar_acoes, text='Adicionar', command='')
botao_adicionar.grid(column=0, row=7, padx=1, pady=1)

#fim janela adicionar ações



#trocar de janelas
menu_principal = Menu(lista_de_acoes)
lista_de_acoes.config(menu=menu_principal)

menu_opcoes = Menu(menu_principal, tearoff=False)
menu_principal.add_cascade(label="Opções", menu=menu_opcoes)
menu_opcoes.add_command(label="Adicionar Ações", command=lambda: Janelas(lista_de_acoes, adicionar_acoes))
menu_opcoes.add_separator()

menu_principal2 = Menu(adicionar_acoes)
adicionar_acoes.config(menu=menu_principal2)

menu_opcoes2 = Menu(menu_principal2, tearoff=False)
menu_principal2.add_cascade(label="Opções", menu=menu_opcoes2)
menu_opcoes2.add_command(label="Lista de ações", command=lambda: Janelas(lista_de_acoes, adicionar_acoes))
menu_opcoes2.add_separator()





adicionar_acoes.withdraw()
lista_de_acoes.mainloop()

