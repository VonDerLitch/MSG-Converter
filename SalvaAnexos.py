import os
import tkinter as tk
from tkinter import filedialog
from extract_msg import Message

def save_attachments_from_msg(msg_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        msg = Message(msg_file)
        for attachment in msg.attachments:
            attachment.save(customPath=output_folder)
            print(f"Anexo salvo: {attachment.longFilename}")
        print("Anexos salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao processar o arquivo .msg: {e}")

def select_msg_file():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo .msg",
        filetypes=[("Arquivos MSG", "*.msg")]
    )

    return file_path

if __name__ == "__main__":
    msg_file = select_msg_file()

    if msg_file:
        documentos_usuario = os.path.expanduser("~\\Documents\\Anexos")
        output_folder = documentos_usuario  
        save_attachments_from_msg(msg_file, output_folder)
