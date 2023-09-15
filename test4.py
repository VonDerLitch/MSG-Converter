import tkinter as tk
from tkinter import filedialog
import extract_msg
import os

# Função para extrair mensagens e anexos de um arquivo MSG
def extract_msg_contents(msg_file):
    try:
        msg = extract_msg.Message(msg_file)
        print("Assunto:", msg.subject)
        print("Remetente:", msg.sender)
        print("Data:", msg.date)
        print("Corpo da Mensagem:")
        print(msg.body)
        
        # Listar e salvar os anexos
        if msg.attachments:
            print("\nAnexos:")
            for i, attachment in enumerate(msg.attachments):
                attachment_filename = f"attachment_{i+1}.dat"
                print(attachment_filename)
                attachment.save(custom_filename=os.path.join(os.getcwd(), "anexos", attachment_filename))
    
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo {msg_file}: {str(e)}")

# Função para selecionar o arquivo MSG
def select_msg_file():
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos MSG", "*.msg")])
    if file_path:
        print(f"Arquivo selecionado: {file_path}")
        extract_msg_contents(file_path)
        root.quit()  # Encerrar o programa

# Crie uma janela para a interface gráfica
root = tk.Tk()
root.withdraw()  # Oculta a janela principal

# Chame a função para selecionar o arquivo MSG
select_msg_file()






