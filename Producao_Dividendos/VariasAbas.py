
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions
from selenium.common.exceptions import *
import time
import os

# Defina as opções do Edge
options = Options()
options.use_chromium = True  # Para Edge baseado em Chromium
options.add_argument('--lang=pt-BR')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--cert_verify_proc_builtin.cc')
options.add_argument('--CertVerifyProcBuiltin')




# Configuração do Selinum Webdriver
webdriver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=options)
wait = WebDriverWait(
            driver=webdriver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )
webdriver.maximize_window()
# Abre a primeira página
primeira_pagina = 'https://www.bol.uol.com.br/' 

Segunda_página_Com_Aba = 'https://www.smiles.com.br/mfe/promocao' 

Terceira_página_Com_Aba = 'https://www.investidor.b3.com.br/login'
print(os.linesep)

if primeira_pagina is not None:
    webdriver.get(primeira_pagina)
    print('Primeira página foi aberta Juntamente com uma Aba')
    # Depois que abriu a primeira página - Vamos abri uma outra Aba
    habilitar_os_cookies = wait.until(
            expected_conditions.presence_of_element_located(
                # (By.XPATH,'//*[starts-with(text(),"ACEITAR TODOS OS COOKIES")]')
                (By.XPATH,'//button[@class="banner-lgpd-consent__accept"]')
            )
        )   
    print(os.linesep)
    print(' 🤗 Encontramos a Opção de Habilitar os Cookies....')
    webdriver.execute_script("arguments[0].click()",habilitar_os_cookies)
    print('iremos Clicar.... em habilitar...\n Concluido com Sucesso....✅')

           
    print(os.linesep)
    time.sleep(15)
    print(os.linesep)

# Abra uma nova aba (segunda aba)
if Segunda_página_Com_Aba is not None:
    webdriver.execute_script(f"window.open('{Segunda_página_Com_Aba}');")
    webdriver.switch_to.window(webdriver.window_handles[1])
    print('Segunda Aba foi aberta')
    habilitar_cookiesAba02 = wait.until(
            expected_conditions.presence_of_element_located(
                # (By.XPATH,'//*[starts-with(text(),"ACEITAR TODOS OS COOKIES")]')
                (By.XPATH,'//button[@id="onetrust-accept-btn-handler"]')
            )
        )
    print(' 🤗 Encontramos a Opção de Habilitar os Cookies....')
    webdriver.execute_script("arguments[0].click()",habilitar_cookiesAba02)
    print('iremos Clicar.... em habilitar...\n Concluido com Sucesso....✅')   

    time.sleep(15)
    print(os.linesep)

# Abra uma terceira aba
if Terceira_página_Com_Aba is not None:
    print(os.linesep)
    print(' Vamos abri a terceira Aba')
    webdriver.execute_script(f"window.open('{Terceira_página_Com_Aba}');")
    webdriver.switch_to.window(webdriver.window_handles[2])
    print('Terceira  Aba foi aberta com sucesso ...')


   


time.sleep(180)
