from lib import *

def Janelas(lista, adicionar):
    janela1= lista
    janela2 = adicionar
    if janela1.winfo_ismapped():
        janela1.withdraw()  # Esconde a janela 1
        janela2.deiconify()  # Exibe a janela 2
    else:
        janela2.withdraw()  # Esconde a janela 2
        janela1.deiconify()  # Exibe a janela 1