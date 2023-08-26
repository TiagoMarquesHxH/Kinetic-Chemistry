import pygame
import random
import math

pygame.init()

# Simulação da caixa por meio de uma janela
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulação de Colisão de Partículas")

# Cores do fundo e particulas
black = (0, 0, 0)
blue = (0, 0, 255)

# Classe para representar as partículas
class Particle:
    def __init__(self, x, y, raio, massa):
        self.x = x
        self.y = y
        self.raio = raio
        self.massa = massa
        self.cor = blue 
        self.speed_x = 5 - massa
        self.speed_y = 6 - massa
        
    def movimento(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if (self.x - self.raio <= 0) or (self.x + self.raio >= width):
            self.speed_x *= -1
        if (self.y - self.raio <= 0) or (self.y + self.raio >= height):
            self.speed_y *= -1

    def desenho(self):
        pygame.draw.circle(window, self.cor, (int(self.x), int(self.y)), self.raio)

# Criando as partículas
particula_1 = Particle(width // 3, height - 100 // 2, 10, 2)
particula_2 = Particle(2 * width // 3, height // 2, 10, 3)

# Rodando a simulação
sim = True
c = pygame.time.Clock()

while sim:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sim = False

    window.fill(black)

    # Movendo e desenhando as partículas
    particula_1.movimento()
    particula_2.movimento()

    particula_1.desenho()
    particula_2.desenho()

    # Detectando colisão
    distancia = math.sqrt((particula_2.x - particula_1.x)**2 + (particula_2.y - particula_1.y)**2)
    if distancia <= particula_1.raio + particula_2.raio:
        impulso = ((2*particula_1.massa)*particula_2.massa*(dv * dr))
        particula_1.speed_x *= -1
        particula_1.speed_y *= -1
        particula_2.speed_x *= -1
        particula_2.speed_y *= -1

    pygame.display.update()
    c.tick(60)

pygame.quit()
