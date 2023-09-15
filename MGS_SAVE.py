import os
import tkinter as tk
from tkinter import filedialog
from extract_msg import Message

def save_attachments_and_print_msg(msg_file, output_folder):
    #criação da pasta
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        msg = Message(msg_file)

        #salvando anexos
        for attachment in msg.attachments:
            attachment.save(customPath=output_folder)
            print(f"Anexo salvo: {attachment.longFilename}")

        print("Anexos salvos com sucesso.")

        print("Conteúdo da Mensagem:")
        #conteudo da mensagem
        print(msg.body)

    except Exception as e:
        print(f"Erro ao processar o arquivo .msg: {e}")

def select_msg_file():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal


    #Escolhe o arquvo
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo .msg",
        filetypes=[("Arquivos MSG", "*.msg")]
    )

    return file_path

if __name__ == "__main__":
    print("Este programa extrai anexos de um arquivo .msg e imprime o conteúdo da mensagem do Outlook.")
    msg_file = select_msg_file()

    if msg_file:
        output_folder = os.path.expanduser("~\\Documents\\Anexos") 
        save_attachments_and_print_msg(msg_file, output_folder)
