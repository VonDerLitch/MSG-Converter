import os
import pathlib

def mkdir():
    # Obtém o caminho da pasta "Documentos" do usuário
    documentos_usuario = os.path.expanduser("~\\Documents")

    # Cria o caminho completo para a pasta "anexos" dentro de "Documentos"
    pasta_anexos = os.path.join(documentos_usuario, "anexos")

    # Verifica se a pasta "anexos" já existe, se não, a cria
    if not os.path.exists(pasta_anexos):
        os.mkdir(pasta_anexos)
        print(f"Pasta 'Anexos' criada em '{pasta_anexos}'")
    else:
        print(f"A pasta 'Anexos' em '{pasta_anexos}' já existe.")