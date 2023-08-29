import pygame
import random as rd
import math
import numpy as np
import constantes as con

# Classe para representar as partículas

class Particula:
    def __init__(self, x, y, massa, velocidade_x, velocidade_y):
        # Propriedades da partícula
        self.x = x
        self.y = y
        self.massa = massa
        self.raio = massa
        self.area_min = massa * 10
        self.cor = con.green 
        self.momento_x = massa * velocidade_x
        self.momento_y = massa * velocidade_y
        self.speed_x = velocidade_x
        self.speed_y = velocidade_y

    def movimento(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Inverte a direção da partícula caso colida com uma parede
        if (self.x - self.raio <= 0) and (self.speed_x <= 0):
            self.speed_x *= -1
        if (self.x + self.raio >= con.width) and (self.speed_x >= 0):
            self.speed_x *= -1
        if (self.y - self.raio <= 0) and (self.speed_y <= 0):
            self.speed_y *= -1
        if (self.y + self.raio >= con.height) and (self.speed_y >= 0):
            self.speed_y *= -1

    def colisao(self,other):
        # Distância Euclidiana
        distancia = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if distancia <= self.raio + other.raio:

            x_p1_futuro = self.x + self.speed_x
            y_p1_futuro = self.y + self.speed_y
            x_p2_futuro = other.x + other.speed_x
            y_p2_futuro = other.y + other.speed_y

            distancia_futura = math.sqrt((x_p2_futuro - x_p1_futuro)**2 + (y_p2_futuro - y_p1_futuro)**2)
            #print(distancia_futura, distancia)

            if distancia_futura < distancia:
                
                # Constantes de massa
                k2 = (-2 * other.massa)/(self.massa + other.massa)
                k1 = (-2 * self.massa)/(self.massa + other.massa) 
                
                # Velocidades das partículas
                esca1 = np.array([self.speed_x-other.speed_x, self.speed_y-other.speed_y])
                v1 = np.array([self.speed_x, self.speed_y])
                esca2 = np.array([self.x - other.x,self.y - other.y])
                v2 = np.array([other.speed_x, other.speed_y])

                esca3 = np.array([other.speed_x-self.speed_x, other.speed_y-self.speed_y])
                esca4 = np.array([other.x - self.x,other.y - self.y])
                prod1 = np.dot(esca1, esca2)
                prod2 = np.dot(esca3, esca4)

                # Colisão entre partículas, tomando como argumentos os vetores velocidade e posição
                p_1vel = v2 - (k1 * (prod1/((np.linalg.norm(esca2)**2))) * esca2)
                p_2vel = v1 - (k2 * (prod2/((np.linalg.norm(esca4)**2))) * esca4)
                self.speed_x = p_2vel[0]
                self.speed_y = p_2vel[1]
                other.speed_x = p_1vel[0]
                other.speed_y = p_1vel[1]
    
    # Desenho da partícula
    def desenho(self):
        pygame.draw.circle(con.window, self.cor, (int(self.x), int(self.y)), self.raio)

# Classe para transformar strings em variáveis com atributos
class TransformaVariaveis:
    def __init__(self, nomes_variaveis):
        for nome in nomes_variaveis:
            setattr(self, nome, None)