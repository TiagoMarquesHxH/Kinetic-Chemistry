from pickletools import anyobject
import pygame
import random as rd
import math
import numpy as np

pygame.init()

# Simulação da caixa por meio de uma janela
width, height = 1100, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulação de Colisão de Partículas")

# Cores do fundo e partículas
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Classe para representar as partículas
class Particle:
    def __init__(self, x, y, massa, velocidade_x, velocidade_y):
        self.x = x
        self.y = y
        self.massa = massa
        self.raio = massa   
        self.cor = green 

        self.momento_x = massa * velocidade_x
        self.momento_y = massa * velocidade_y
        self.speed_x = velocidade_x
        self.speed_y = velocidade_y

    def movimento(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if (self.x - self.raio <= 0) or (self.x + self.raio >= width):
            self.speed_x *= -1
        if (self.y - self.raio <= 0) or (self.y + self.raio >= height):
            self.speed_y *= -1

    def colisao(self,other):
        distancia = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

        if distancia <= self.raio + other.raio:

            x_p1_futuro = self.x + self.speed_x
            y_p1_futuro = self.y + self.speed_y

            x_p2_futuro = other.x + other.speed_x
            y_p2_futuro = other.y + other.speed_y

            distancia_futura = math.sqrt((x_p2_futuro - x_p1_futuro)**2 + (y_p2_futuro - y_p1_futuro)**2)
            #print(distancia_futura, distancia)

            if distancia_futura < distancia:

                k2 = (-2 * other.massa)/(self.massa + other.massa)
                k1 = (-2 * self.massa)/(self.massa + other.massa) 

                esca1 = np.array([self.speed_x-other.speed_x, self.speed_y-other.speed_y])
                v1 = np.array([self.speed_x, self.speed_y])
                esca2 = np.array([self.x - other.x,self.y - other.y])
                v2 = np.array([other.speed_x, other.speed_y])

                esca3 = np.array([other.speed_x-self.speed_x, other.speed_y-self.speed_y])
                esca4 = np.array([other.x - self.x,other.y - self.y])
                prod1 = np.dot(esca1, esca2)
                prod2 = np.dot(esca3, esca4)

                #print(np.linalg.norm(esca2)**2)

                p_1vel = v2 - (k1 * (prod1/((np.linalg.norm(esca2)**2))) * esca2)
                p_2vel = v1 - (k2 * (prod2/((np.linalg.norm(esca4)**2))) * esca4)

                #print(p_1vel)
                #print(self.speed_y)
                self.speed_x = p_2vel[0]
                self.speed_y = p_2vel[1]
                #print(self.speed_y)
                other.speed_x = p_1vel[0]
                other.speed_y = p_1vel[1]
                #print (p_1.speed_x, p_1vel)

    def desenho(self):
        pygame.draw.circle(window, self.cor, (int(self.x), int(self.y)), self.raio)

# Criando as partículas

# List of strings
dic_particulas = {}

for i in range(60):
    dic_particulas['p_' + str(i)] = "iterationNumber=="+str(i)

locals().update(dic_particulas)

lista_p = list(dic_particulas.keys())

# Create an instance of the DynamicVariables class
class DynamicVariables:
    def __init__(self, variable_names):
        for name in variable_names:
            setattr(self, name, None)

variables = DynamicVariables(lista_p)

# Values to assign
values = []
for i in range(60):
    values.append(i)

# Assign values to the variables using a loop
for name, value in zip(lista_p, values):
    setattr(variables, name, value)

# Access the values

variable_list = [(name, getattr(variables, name)) for name in lista_p]

# Print the entire list containing names and values

def CriarParticulas(MASSA1,MASSA2,VEL_X_MAX, VEL_Y_MAX):
    p = Particle(rd.randint(20, width - 20),rd.randint(20, height - 20), rd.choice((MASSA1,MASSA2)),rd.randint(0,VEL_X_MAX), rd.randint(0,VEL_Y_MAX))
    return p

lista_particula = []

for name, value in variable_list:
    valor = CriarParticulas(10,4,3,3)
    lista_particula.append(valor)

# Rodando a simulação
sim = True
c = pygame.time.Clock()

while sim:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sim = False

    window.fill(black)

    # Movendo e desenhando as partículas
    for p in lista_particula:
        p.movimento()

    lista = lista_particula.copy()
    # print(lista)

    for p in lista:
        lista.remove(p)

        for _ in lista:
            p.colisao(_)
    
        lista.append(p)
    
    for p in lista_particula:
        p.desenho()

    pygame.display.update()
    c.tick(60)

pygame.quit()