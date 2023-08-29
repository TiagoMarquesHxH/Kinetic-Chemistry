# Import das bibliotecas utilizadas e de arquivos .py
import pygame
import random as rd
import math
import numpy as np
import constantes as con
import classes
import funcoes as fn

pygame.init() # Iniciando a simulação
pygame.display.set_caption("Simulação de Colisão de Partículas") # Simulação da caixa por meio de uma janela

dic_particulas = {} # Dicionário que contém as partículas em forma de string
for i in range(con.numero): # Loop para adicionar novas partículas no dicionário, definidas pela constante "numero"
    dic_particulas['p_' + str(i)] = "iterationNumber=="+str(i)

locals().update(dic_particulas)

lista_p = list(dic_particulas.keys()) # Transformando as chaves (nomes das partículas) do dicionário em uma lista
variaveis = classes.TransformaVariaveis(lista_p) # Transforma a lista de nomes das partículas em variáveis com atributos

# Valores que serão atribuídos às novas variáveis
valores = []
for i in range(con.numero):
    valores.append(i)

# Loop que define valores para as variávies
for nome, valor in zip(lista_p, valores):
    setattr(variaveis, nome, valor)


# A lista de variaveis terá nomes e valores atribuidos a estes nomes, para cada nome da lista de particulas
lista_variaveis = [(nome, getattr(variaveis, nome)) for nome in lista_p]
lista_particula = []

# Criação das partículas pelos nomes e valores da lista de variáveis
for nome, valor in lista_variaveis:
    valores_p = fn.CriarParticulas(10,4,3,3)
    lista_particula.append(valores_p)

# Rodando a simulação
sim = True
c = pygame.time.Clock()

while sim:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sim = False

    con.window.fill(con.black)

    # Movimento das particulas
    for p in lista_particula:
        p.movimento()
    lista = lista_particula.copy()
    # Para cada duas partículas na lista de partículas, calcular a colisão de uma à outra
    for p in lista:
        for _ in lista:
            p.colisao(_)
    # Desenho de cada partícula
    for p in lista_particula:
        p.desenho()

    pygame.display.update()
    c.tick(60) # Taxa de atualização do display

pygame.quit()