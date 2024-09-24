from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicialize o WebDriver (por exemplo, usando o Chrome)
driver = webdriver.Chrome()

# Abra a primeira página
driver.get("https://www.uol.com.br/")

# Abra uma nova aba (segunda aba)
driver.execute_script("window.open('');")
time.sleep(15)

# Troque para a nova aba aberta
driver.switch_to.window(driver.window_handles[1])

# Navegue para uma nova URL na nova aba
driver.get("https://www.r7.com/")

# Abra uma terceira aba
driver.execute_script("window.open('');")
time.sleep(15)

# Troque para a terceira aba
driver.switch_to.window(driver.window_handles[2])

# Navegue para outra URL na terceira aba
driver.get("https://www.yahoo.com")

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
driver.quit()
