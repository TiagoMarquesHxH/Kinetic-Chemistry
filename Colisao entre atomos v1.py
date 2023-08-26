import pygame
import random as rd
import math
import numpy as np
import constantes as con
import classes
import funcoes as fn

pygame.init()

# Simulação da caixa por meio de uma janela
pygame.display.set_caption("Simulação de Colisão de Partículas")

# List of strings
dic_particulas = {}

for i in range(con.numero):
    dic_particulas['p_' + str(i)] = "iterationNumber=="+str(i)

locals().update(dic_particulas)

lista_p = list(dic_particulas.keys())

variables = classes.DynamicVariables(lista_p)

# Values to assign
values = []
for i in range(con.numero):
    values.append(i)

# Assign values to the variables using a loop
for name, value in zip(lista_p, values):
    setattr(variables, name, value)

# Access the values

variable_list = [(name, getattr(variables, name)) for name in lista_p]

lista_particula = []

for name, value in variable_list:
    valor = fn.CriarParticulas(10,4,3,3)
    lista_particula.append(valor)

# Rodando a simulação
sim = True
c = pygame.time.Clock()

while sim:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sim = False

    con.window.fill(con.black)

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