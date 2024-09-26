
import pygame
import time
import os 
# pygame.mixer.music.load('CoffinDance1Hour.mp3')


# Inicializa o mixer do pygame
pygame.mixer.init()

#Local da Musica....... 
local_da_Musica = r'MUSICA_2_PLANO' + os.sep + 'EiffelBlue_8_Minutos.mp3'
# Carrega e toca a música
pygame.mixer.music.load(local_da_Musica)

# Toca a música em loop
pygame.mixer.music.play(-1)

# Automação rodando
for i in range(50):
    print(f"Automação rodando... {i}")
    time.sleep(2)  # Simulando uma tarefa

# Quando terminar a automação, você pode parar a música
pygame.mixer.music.stop()

