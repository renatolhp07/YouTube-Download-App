import os
from time import sleep

#coding UTF-8

def importar_libs():

    try:

        print("Iniciando a instalação das bibliotecas necessárias. Por favor, aguarde...")
        sleep(2)
        os.system("cls")
        os.system("pip install --upgrade pip")
        os.system("pip install pytube")
        
        print("Instalação concluída com sucesso")

    except ValueError:
        print("Algo inesperado aconteceu... Por favor tente novamente")