import pygame

# Cores do fundo e partículas

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255,255,0)

# Tamanho da caixa de simulação

width, height = 600, 600
window = pygame.display.set_mode((width, height))

# N° de partículas

numero = 500

MASSA_NOVA1 = 6
MASSA_NOVA2 = 4