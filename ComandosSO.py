import os,shutil


def criar_pasta(caminho):
    os.makedirs(caminho)
    return True

def apagar_pasta(caminho):
    shutil.rmtree(caminho)
    return True

def listar_arquivos(path):
    arquivos = os.listdir(path)
    return arquivos

def renomear_arquivos(original, renomeado):
    #print(f'{doc_original} renomeado para {doc_renomeado}.')
    os.rename(original, renomeado)
    return renomeado

