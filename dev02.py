from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support  import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import random

eder_Options = Options()
eder_Options.use_chromium = True  # Para garantir que o Edge Chromium seja usado
eder_Options.add_argument('--lang=pt-BR')
eder_Options.add_argument('disable-notifications')
eder_Options.add_argument('ignore-certificate-errors')
eder_Options.add_argument('--ignore-ssl-errors')
eder_Options.add_argument('--ignore-certificate-errors')
eder_Options.add_argument('--ignore-Renderer')

webdriver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=eder_Options)
wait = WebDriverWait(
            driver=webdriver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                                ElementNotVisibleException,
                                ElementNotSelectableException]
        )

      
# Inicialize o WebDriver (por exemplo, usando o Chrome)

# Abra a primeira página
webdriver.get("https://www.uol.com.br/")
sleep(random.randint(10, 60))
# Abra uma nova aba (segunda aba)
webdriver.execute_script("window.open('');")


# Troque para a nova aba aberta
webdriver.switch_to.window(webdriver.window_handles[1])
sleep(random.randint(10, 60))
# Navegue para uma nova URL na nova aba
webdriver.get("https://www.r7.com/")

# Abra uma terceira aba
webdriver.execute_script("window.open('');")
sleep(random.randint(10, 60))

# Troque para a terceira aba
webdriver.switch_to.window(webdriver.window_handles[2])

# Navegue para outra URL na terceira aba
webdriver.get("https://www.yahoo.com")
# Navegue para outra URL da 1° aba
sleep(random.randint(10, 60))
webdriver.switch_to.window(webdriver.window_handles[0])
sleep(random.randint(10, 60))


# Fechar as abas depois de um tempo
'''
Para abrir várias abas no mesmo navegador usando o Selenium com Python, 
você pode utilizar o comando driver.execute_script para simular a abertura de novas abas e alternar 
entre elas com o comando driver.switch_to.window().
 Abaixo está um exemplo de como fazer isso:
driver.execute_script("window.open('');"): Abre uma nova aba no navegador.
driver.switch_to.window(driver.window_handles[index]): Muda o foco para a aba desejada. window_handles retorna uma lista com os identificadores de todas as abas abertas, onde index é a posição da aba (0 para a primeira, 1 para a segunda, e assim por diante).
driver.get(url): Abre uma página na aba ativa.
'''

time.sleep(180)
webdriver.quit()
