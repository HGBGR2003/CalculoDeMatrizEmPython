import numpy as np
print(np.__version__)

def calculo_matriz():
    try:
        ln1 = int(input("Inseri um valor para linha 1"))
        ln2 = int(input("Inseri um valor para linha 2"))
        ln3 = int(input("Inseri um valor para linha 3"))
        ln4 = int(input("Inseri um valor para linha 4"))
    except IndexError:
        print("Erro de Valor Incorreto.")