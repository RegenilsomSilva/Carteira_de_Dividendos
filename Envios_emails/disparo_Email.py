
import os
import glob
import logging
import smtplib
from email.message import EmailMessage
from datetime import datetime
from time import sleep
import random
from dotenv import load_dotenv,find_dotenv





print('''\u001b[32m
          _    _ _______ ____  __  __       _______ _____ ______         _   _ _____   ____         ____   ____   ____ _______   _____  ______ _____ _____  _____ 
     /\  | |  | |__   __/ __ \|  \/  |   /\|__   __|_   _|___  /   /\   | \ | |  __ \ / __ \       |  _ \ / __ \ / __ \__   __| |  __ \|  ____/ ____|_   _|/ ____|
    /  \ | |  | |  | | | |  | | \  / |  /  \  | |    | |    / /   /  \  |  \| | |  | | |  | |______| |_) | |  | | |  | | | |    | |__) | |__ | |  __  | | | (___  
   / /\ \| |  | |  | | | |  | | |\/| | / /\ \ | |    | |   / /   / /\ \ | . ` | |  | | |  | |______|  _ <| |  | | |  | | | |    |  _  /|  __|| | |_ | | |  \___ \ 
  / ____ \ |__| |  | | | |__| | |  | |/ ____ \| |   _| |_ / /__ / ____ \| |\  | |__| | |__| |      | |_) | |__| | |__| | | |    | | \ \| |___| |__| |_| |_ ____) |
 /_/    \_\____/   |_|__\____/|_|_ |_/_/    \_\_|  |_____/_____/_/    \_\_| \_|_____/ \____/       |____/ \____/ \____/  |_|    |_|  \_\______\_____|_____|_____/ 
               ____ |__ \ / _ \__ \| || |                                                                                                                         
              / __ \   ) | | | | ) | || |_                                                                                                                        
             / / _` | / /| | | |/ /|__   _|                                                                                                                       
            | | (_| |/ /_| |_| / /_   | |                                                                                                                         
             \ \__,_|____|\___/____|  |_|                                                                                                                         
              \____/                                                                                                                                              
                                                                                                                                                                  
\u001b[0m''')

load_dotenv(find_dotenv())


#  CÓDIGO DE MELHORIA VIA CHAT-GPT 
#  código Documentado......
logging.basicConfig(level=logging.INFO, filename=r'Arquivos_LOG_Temp' + os.sep + 'Log_de_Execucao.log', filemode='w', format='%(asctime)s - %(levelname)s -%(message)s', datefmt='%d/%m/%Y %H:%M')

class EmailSender:
   
    def __init__(self):
     
        # Vamos chamar o módulo de cores que está em outra pasta  
       
        # Configuration de Login
        print('O Dotenv é uma biblioteca Python que permite carregar variáveis de ambiente a partir de um arquivo .env.')
        print(f'Configuração de Login {os.linesep}')
        self.E_mail_address    = os.environ.get('email_address')
        self.Password          = os.environ.get('passwordd')
        self.recipients         = 'regenilsomfeliz@outlook.com', 'regenilsom.vcdevaprender@gmail.com'

        print(os.linesep)
        print('*************************************')
        print('*****AUTOMAÇÃO ENVIO DE E-MAILS *****')
        print('*************************************')
        print(os.linesep)

    def send_email(self):
        
        self.configure_email() # Configuração de E-mail 
        self.attach_files()    # Anexar Arquivos
        self.send()            # Envio de E-mail

    def configure_email(self):
        print(f'Criando e configurando E-mail para ser Enviado... {os.linesep}....Aguarde{os.linesep}')
        logging.info(f'Criando e configurando E-mail para ser Enviado... {os.linesep}....Aguarde{os.linesep}')
        self.message = EmailMessage()
        self.message['Subject'] = f'Solicitação Carteira de Dividendo  {datetime.now().strftime("%d-%m-%Y")}'
        self.message['From'] = self.E_mail_address           # Endereço de E-mail
        self.message['To'] = ', '.join(self.recipients)     # Destinatário
        self.message.set_content(
            'Prezados, Boa tarde or Bom Dia, 😊,\n\n🙌🙌🙌🙌 Segue anexo com todas as informações Atual Carteira de Investimento.\n\nSistema Automatizado @Regis_Silva ✔️ !!!')

    def attach_files(self):             # Anexar arquivos 
        print(f'**********CONFIGURAÇÃO DE ANEXOS **********{os.linesep}')
        print(f' 🙌🙌 Enviando E-mail com Anexo de Arquivo{os.linesep}.......Aguarde{os.linesep}')
        attachment_dir = os.path.join(os.getcwd(), 'Arquivos_LOG_Temp')  # Anexar arquivos 
        files = glob.glob(os.path.join(attachment_dir, '*'))  
        for file_path in files:
            with open(file_path, 'rb') as file:
                self.message.add_attachment(
                    file.read(), maintype='application', subtype='octet-stream', filename=os.path.basename(file_path))
        print(f'⏳ Acabamos de fazer a Manipulação dos arquivos...... ⏳{os.linesep}....Aguarde{os.linesep}')
        sleep(random.randint(1,2))        

    def send(self):                         # Envio de E-mail
        logging.info('Sending email...')
        print(f'⚙🔍 Configuração  de anexo via  E-mail...{os.linesep}....Aguarde ⚙🔍 {os.linesep}')
        logging.info(f'⚙🔍 Configuração  de anexo via  E-mail...{os.linesep}....Aguarde ⚙🔍 {os.linesep}')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(self.E_mail_address, self.Password)
            server.send_message(self.message)
            sleep(random.randint(8, 10))    
        logging.info('Email sent successfully.')  # Registro de Loog
        print(f'🤖🤖 Obrigado por Usar o nosso BOOT 🤖🤖🤖{os.linesep}') 
        print(f'Copyright Ano 2024')
        logging.info('Copyright Ano 2024')
       
                                                          
SendingMailing  = EmailSender()  
SendingMailing.send_email()






 
