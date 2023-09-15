import shutil
import os

documentos_usuario = os.path.expanduser("~\\Documents")
shutil.move("teste.txt", documentos_usuario + "\\Anexos")