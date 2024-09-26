
#  ATUALIZANDO O PIP =  python -m pip install --upgrade pip
# Service para o Webdriver se comunicar com os demais Programas.
import os
import openpyxl.workbook
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support  import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from datetime import datetime
import logging
from Funcao_Cores import Palheta_De_Cor
from dotenv import load_dotenv,find_dotenv
import pyautogui
import openpyxl
import pygame




'''
https://www.investidor.b3.com.br/login
Quero Desenvolver uma Automação ->
	Web scraping, onde o Boot ira raspar as informações do Site da B3 ( Àrea do investidor da b3) as próximas data e quais serão
	os ativos para pagamentos de Dividendos, ira trazer tanto a foto dos ativos, quanto detalhado no Excel.
	iria execultar 2 ou 3 vezes por semana, disponibilizando em um E-mai
	
	1°- Entra no Site (https://www.investidor.b3.com.br/login)
	2° Digite seu CPF (****************) da um Enter ou Entra
	3° Digitar a Senha (*************) da um Enter ou Entra
	4° Clicar no Campo( Não sou Robô)
	5° Entra- Portal 
	6° Pular TOUR ->
        7° Rejeitar Cookies 
	8° Clicar na Aba (Proventos)
	9° Radar 

https://www.investidor.b3.com.br/proventos/radar

'''
load_dotenv(find_dotenv())


logging.basicConfig(level=logging.INFO, filename=r'Arquivos_LOG_Temp' + os.sep + 'Log_de_Execucao.log',filemode='w', format='%(asctime)s - %(levelname)s -%(message)s', datefmt='%d/%m/%Y %H:%M')


class Dividendos:

    def __init__(self):

        self.func = Palheta_De_Cor()
        self.func.cores()
        eder_Options = Options()
        eder_Options.add_argument('--lang=pt-BR')
        eder_Options.add_argument('disable-notifications')
        eder_Options.add_argument('ignore-certificate-errors')
        eder_Options.add_argument('--ignore-ssl-errors')
        eder_Options.add_argument('--ignore-certificate-errors')
        self.usuario  = os.environ.get('Usuario')
        self.Senha    =  os.environ.get('password')
       
        print(os.linesep)
        print(f'{self.func.azul}=================================================================================')
        print(f'{self.func.ciano}================== AUTOMATIZANDO CARTEIRA DE DIVIDENDOS  =======================')
        print(f'{self.func.ciano}============================== BOOT-@REGIS |2024 ===============================')
        print(f'{self.func.ciano}=================================================================================')
        print(f'{self.func.azul}=================================================================================')
        print(os.linesep)
        print(os.linesep)
         # ======= Vai funcionar em qualquer Sistema Operacional =================
       
        self.webdriver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=eder_Options)
        self.wait = WebDriverWait(
            driver=self.webdriver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )
# Inicializa o mixer do pygame
#Local da Musica....... 
    local_da_Musica = r'MUSICA_2_PLANO' + os.sep + 'EiffelBlue_8_Minutos.mp3'
# Carrega e toca a música
    pygame.mixer.music.load(local_da_Musica)

    # Toca a música em loop
    pygame.mixer.music.play(-1)

    
    def Inicio(self):
        
        self.Entra_Portal()
        self.Criacao_De_Planilha()
        self.Radar_de_Proventos()
        


    def Entra_Portal(self):

        print(os.linesep)
        # 1°- Entra no Site (https://www.investidor.b3.com.br/login)
        self.webdriver.maximize_window()
        # self.webdriver.get('https://www.apple.com/br/shop/buy-iphone/iphone-16-pro/tela-de-6,9-polegadas-512gb-tit%C3%A2nio-natural')   
        self.webdriver.get('https://www.investidor.b3.com.br/login') 
        print(os.linesep)

        # habilitar_os_cookies =  self.webdriver.find_elements(
        #     'xpath', '//*[starts-with(text(),"ACEITAR TODOS OS COOKIES")]')
        # # button id="onetrust-accept-btn-handler"
        habilitar_os_cookies = self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH,'//*[starts-with(text(),"ACEITAR TODOS OS COOKIES")]')
            )
        )   

        if habilitar_os_cookies is not None:
            print(os.linesep)
            print(' 🤗 Encontramos a Opção de Habilitar os Cookies....')
            logging.info(f'🤗 Encontramos a Opção de Habilitar os Cookies....')
            self.webdriver.execute_script("arguments[0].click()",habilitar_os_cookies)
            print('iremos Clicar.... em habilitar...\n Concluido com Sucesso....✅')
            logging.info('iremos Clicar.... em habilitar...\n Concluido com Sucesso....✅')
            sleep(random.randint(3, 6))
            print(os.linesep)

        # 2° Digite seu CPF (****************) da um Enter ou Entra
        Digitar_Usuario =  self.wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH,'//input[@aria-label="Digite seu CPF/CNPJ"]')
            )
        )
        sleep(random.randint(5, 8))                                
        if Digitar_Usuario is not None :
            
            print(os.linesep)
            print(' 🤗 Encontramos a Opção Digitar o CPF ou CNPJ...')
            logging.info(f'🤗 Encontramos a Opção Digitar o CPF ou CNPJ...')
            self.webdriver.execute_script("arguments[0].click()",Digitar_Usuario)
            sleep(random.randint(5, 8))
            Digitar_Usuario.send_keys(self.usuario)
            print(f'Foi digitado com sucesso ✅')
            logging.info(f'Foi digitado com sucesso ✅')
            Digitar_Usuario.send_keys(Keys.ENTER)
            print(os.linesep)

         # 3° Digitar a Senha (*************) da um Enter ou Entra
        Digitar_password =  self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,'//div[@class="form__control"]//input[@type="password"]')
            )
        )
       
        sleep(random.randint(5, 8))   

        if Digitar_password is not None:
            print(os.linesep)
            print(' 🤗 Encontramos a Opção de Digitar a Senha ou Password ....')
            logging.info(f'🤗 Encontramos a Opção de Digitar a Senha ou Password ....')
            self.webdriver.execute_script("arguments[0].click()",Digitar_password)
            sleep(random.randint(3, 5))
            Digitar_password.send_keys(self.Senha)
            print(f'Foi digitado com sucesso ✅')
            logging.info(f'Foi digitado com sucesso ✅')
            sleep(random.randint(2, 3))
            print(os.linesep)

        # 4° Clicar no Campo( Não sou Robô)
    #  iremos utilizar o Pyautoguir para Sleecionar a caixa de texto | Não sou robor
        Nao_sou_Robo = []
        if Nao_sou_Robo is not None:
                
                print('Opção de Não sou Robô está Visivél.... Vamos Clicar')
                pyautogui.click(x=239,y=684,duration=2)  # Mova o mouse para as coordenadas XY e clique nele.
                print(f'Foi selecionado com sucesso ✅')

      
        Entra_Na_Aplicacao = []
        if Entra_Na_Aplicacao is not None:
              print(os.linesep)
              print(f' {self.func.cianoNegrito} 🤗 Encontramos a Opção de Entra na Aplicação ....')
              pyautogui.click(x=383,y=874,duration=2)  # Mova o mouse para as coordenadas XY e clique nele.
              print(f'{self.func.cianoNegrito} Foi selecionado com sucesso ✅')
              sleep(random.randint(3, 6))
              print(os.linesep)
              print(os.linesep)

        # 6° Pular TOUR -> 
             
    def Criacao_De_Planilha(self):
        try:
            # Vamos criar uma planilha para ser enviada via E-mail pela automação 
            # Com Isso o nosso Boot será capaz de enviar as informações via Log terminal e também via E-mail
            self.workbook                 =       openpyxl.load_workbook('dividendo_a_pagar.xlsx') # Este é a versão mais nova do OpenPyxel
            #  Criando uma variavél workbook 
            # self.CriacaoPlanilha          =       self.workbook['Dividendo'] # Planilha1
            self.CriacaoPlanilha          =       self.workbook['Planilha2'] # Planilha1
            self.CriacaoPlanilha['B1'] = 'TIPOS DE EVENTOS'
            self.CriacaoPlanilha['C1'] = 'DATA-COM'
            self.CriacaoPlanilha['D1'] = 'DATA- PAGAMENTO DIVIDENDOS'
            self.CriacaoPlanilha['E1'] = 'PREÇO UNITARIO'
            self.CriacaoPlanilha['F1'] = 'PREÇO DE FECHAMENTO DA AÇÃO'
            self.CriacaoPlanilha['G1'] = 'DATA DA AUTOMAÇÃO'
            # 👆🏼 Acessando a Página Dentro da Planilha Workbook

            print(f'🤖🤖Obrigado por usar o Nosso Boot Criação de Planilhas Excel 🤖🤖🤖 as {datetime.now()}{os.linesep}')
            logging.info(f'🤖🤖Obrigado por usar o Nosso Boot Criação de Planilhas Excel 🤖🤖🤖 as {datetime.now()}{os.linesep}')
            print('Criação da Planilha Efetuado com sucesso..')
            logging.info('Criação da Planilha Efetuado com sucesso..')
            print(os.linesep)
        except:
            print('Erro ao Montar a Criação de Planilha')
            logging.warning('Erro ao Montar a Criação de Planilha')
            print('Tente Novamente, depois de corrigir o Erro...')
            logging.warning('Tente Novamente, depois de corrigir o Erro...')
            print(os.linesep) 
                    
# /proventos/radar
    def Radar_de_Proventos(self):

        sleep(random.randint(20, 40))
        Pular_TOUR = self.wait.until(
             expected_conditions.presence_of_element_located(
                  (By.XPATH,'//button[@aria-label="Pular"]')
             )   
       )
        if Pular_TOUR is not None:
            
            print(os.linesep)
            print(' 🤗 Encontramos a Opção de  Pular TOUR....')
            logging.info(f' 🤗 Encontramos a Opção de  Pular TOUR....')
            self.webdriver.execute_script("arguments[0].click()",Pular_TOUR)
            print('Clicado com sucesso....')
            logging.info('Clicado com sucesso....')
            print(os.linesep)
            logging.info(os.linesep)

        # 8° Clicar na Aba (Proventos)   
        Proventos = self.wait.until(
             expected_conditions.presence_of_all_elements_located(
                  (By.XPATH,'//li[@class="b3i-menu-principal__nav__menu__item ng-tns-c860703811-1"]')
             )
        )
        if Proventos is not None:
            print(os.linesep)
            print(' 🤗 Encontramos a Opção de  Proventos....')
            logging.info(f'🤗 Encontramos a Opção de  Proventos...')
            Proventos[3].click()
            print('Clicado com sucesso....')
            logging.info('Clicado com sucesso....')
            print(os.linesep)

    # 9° Radar 
        print(f'{self.func.resetar}')
        logging.info(f'{self.func.resetar}')
        print(f'{self.func.verde}')
        logging.info(f'{self.func.verde}')

        Radar_de_Compras_de_Proventos_Dividendos = self.wait.until(
             expected_conditions.presence_of_element_located(
                  (By.XPATH,'//a[@id="Radar"]')
             )
        )
        # O_Que_E_Radar_De_Proventos = f'O "Radar de Proventos" estima pagamentos futuros de investimentos, incluindo dividendos e juros sobre capital próprio, \noferecendo uma visão clara de cada evento.\n Esta ferramenta facilita a tomada de decisão de investimento e o planejamento financeiro.'
        # print(f'{O_Que_E_Radar_De_Proventos}')

        if Radar_de_Compras_de_Proventos_Dividendos is not None:
            
            print(os.linesep)
            print(f'  🤗 Encontramos a Opção de  Proventos....')
            logging.info(f'🤗 Encontramos a Opção de  Proventos....')
            sleep(random.randint(2, 3))
            self.webdriver.execute_script("arguments[0].click()",Radar_de_Compras_de_Proventos_Dividendos)
            print('Clicado com sucesso....')
            logging.info('Clicado com sucesso....')
            sleep(random.randint(2, 3))
            pyautogui.scroll(-950)
            print(os.linesep)
            print('O "Radar de Proventos" estima pagamentos futuros de investimentos, incluindo dividendos e juros sobre capital próprio')
            logging.info('O "Radar de Proventos" estima pagamentos futuros de investimentos, incluindo dividendos e juros sobre capital próprio')
            print(os.linesep)

        # Produto
        Produto = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//td[@class="cdk-cell cdk-column-codigoNegociacaoComRazaoSocial ng-untouched ng-pristine ng-valid ng-star-inserted"]')
            )
        )
        if Produto is not None:
            print(os.linesep)
            print('Show de Bola... Encontramos os Produtos')
            logging.info('Show de Bola... Encontramos os Produtos')

        
        # Tipo_De_Evento
        Tipo_De_Evento = self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH,'//td[@class="cdk-cell cdk-column-nomeEvento ng-untouched ng-pristine ng-valid ng-star-inserted"]')
            )
        )
        if Tipo_De_Evento is not None:
            print(os.linesep)
            print('Encontramos o Tipo de Eventos.....')
            logging.info('Encontramos o Tipo de Eventos.....')
        
        # Data_Com
        Data_Com =  self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH,'//td[@class="cdk-cell cdk-column-dataCOM ng-untouched ng-pristine ng-valid ng-star-inserted"]')
            )
        )
        if Data_Com is not None:
            print(os.linesep)
            print(' Encontramos a Data para Compra as Ações e Adquiri os Dividendos ou o JCP....')
            logging.info(' Encontramos a Data para Compra as Ações e Adquiri os Dividendos ou o JCP....')
            print(os.linesep)

        # Data_Pagamento
        Data_Pagamento_Dividendos  = self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH,'//td[@class="cdk-cell cdk-column-dataPagamento ng-untouched ng-pristine ng-valid ng-star-inserted"]')
            )
        )
        if Data_Pagamento_Dividendos is not None:
            print(os.linesep)
            print('Encontramos a Data que a Empresa pagará os Dividendos ou o JCP... ')
            logging.info('Encontramos a Data que a Empresa pagará os Dividendos ou o JCP... ')
            print(os.linesep)    

        # Preco_Unitario_Bruto
        Preco_Unitario_Bruto = self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH,'//td[@class="cdk-cell cdk-column-valorBruto ng-untouched ng-pristine ng-valid ng-star-inserted"]')
            )
        )
        if Preco_Unitario_Bruto is not None:
            print(os.linesep)
            print('Encontramos o Valor dos Dividendos...')
            logging.info('Encontramos o Valor dos Dividendos...')

        # Preco_Fechamento        
        Preco_Fechamento  = self.wait.until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH,'//td[@class="cdk-cell cdk-column-valorPrecoFechamento ng-untouched ng-pristine ng-valid ng-star-inserted"]')
            )
        )
        if Preco_Fechamento is not None:
            print(os.linesep)
            print('...Preço sugerido para Compra as Açoes e ter o beneficío de ser pago o Dividendo....')
            logging.info('...Preço sugerido para Compra as Açoes e ter o beneficío de ser pago o Dividendo....')
            print(os.linesep)   

    # Vamos interar sobre cada iten, que o nosso Boot Encontra, e para isso vamos uzar a função zip
        for Produtos,Tipo_De_Eventos, Data_de_Compra,Data_Pagamento_Dividendo, Preco_Unitario_Brutos,Preco_Fechamentos in zip(Produto,Tipo_De_Evento,Data_Com,Data_Pagamento_Dividendos,Preco_Unitario_Bruto ,Preco_Fechamento):
            
            print(os.linesep)
            logging.info(os.linesep)
            print(Produtos.text)
            logging.info(Produtos.text)
            prod = Produtos.text
            print(Tipo_De_Eventos.text)
            tipEvent = Tipo_De_Eventos.text
            logging.info(Tipo_De_Eventos.text)
            print(Data_de_Compra.text)
            dayCompra = Data_de_Compra.text
            logging.info(Data_de_Compra.text)
            print(Data_Pagamento_Dividendo.text)
            logging.info(Data_Pagamento_Dividendo.text)
            dayPagDivi = Data_Pagamento_Dividendo.text
            print(Preco_Unitario_Brutos.text)
            logging.info(Preco_Unitario_Brutos.text)
            unitPreco = Preco_Unitario_Brutos.text
            print(Preco_Fechamentos.text)
            logging.info(Preco_Fechamentos.text)
            fechamentPreco = Preco_Fechamentos.text
            Data_Atual = datetime.now().strftime('%d/%m/%Y')

            
            self.CriacaoPlanilha.append([prod,tipEvent,dayCompra,dayPagDivi,unitPreco,fechamentPreco,Data_Atual])
        logging.info('Planilha foi salva com sucesso...')
        # self.workbook.save(f'dividendo_a_pagar.xlsx') 
        self.workbook.save(r'Arquivos_LOG_Temp' + os.sep + 'dividendo_a_pagar.xlsx') 
        
        print(f'🤖🤖Obrigado por usar o Nosso Boot 🤖🤖🤖')   
     
    def Modulo_De_Envio(self):
        try:
           
            from Envios_emails.disparo_Email import EmailSender
            transmitir = EmailSender()
            transmitir.send_email()
            Hora_Atual  = datetime.now().strftime('%H:%M') 

            print(f'Buscando Módulo De envio de E-mails {Hora_Atual} ')
            print('Elemento encontrado com Sucesso !!!')
            logging.info('Elemento encontrado com Sucesso !!!')
            print(os.linesep)
            logging.info(f'{os.linesep}')

        except:
            NameError(f'Não Foi possivel Fazer o Envio de E-mail')
            logging.critical(f'Não Foi possivel Fazer o Envio de E-mail')
            NameError('Porém daremos continuidade...!')
            logging.critical('Porém daremos continuidade...!')
                                
              
    

start = Dividendos()
start.Inicio()
start.Modulo_De_Envio()
pygame.mixer.music.stop()

sleep(180)

