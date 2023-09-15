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
                attachment.save(custom_filename=os.path.join("anexos", attachment_filename))
    
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo {msg_file}: {str(e)}")

# Caminho completo para o arquivo MSG que você deseja processar
msg_file = r"C:\Users\kelvin.silveira\Desktop\Projetos\MSG\teste.msg"

# Crie um diretório para salvar os anexos
if not os.path.exists("anexos"):
    os.makedirs("anexos")

# Processar o arquivo MSG
print(f"Processando arquivo: {msg_file}")
extract_msg_contents(msg_file)