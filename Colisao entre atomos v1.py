# Import das bibliotecas utilizadas e de arquivos.py
from sre_constants import JUMP
import pygame
import random as rd
import math
import numpy as np
import constantes as con
import classes
import funcoes as fn
import matplotlib.pyplot as plt

Plot_Do_Histograma_Vel = input("Quer Histograma ou não? O padrão é não, se quiser escreva Y. ")

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
    valores_p = fn.CriarParticulas(8,6,7,7,con.red,con.blue,"A","B")
    lista_particula.append(valores_p)

# Rodando a simulação
sim = True


c = pygame.time.Clock()

if Plot_Do_Histograma_Vel == "Y":
    lista_vel = []
    fig, ax = plt.subplots()
    ax.hist(lista_vel, bins=20)
    plt.show(block=False)

figo, axo = plt.subplots()
ax1 = []
ax2 = []
ax3 = []
ax4 = []
axo.plot(ax1,ax2,ax3,ax4)
plt.show(block=False)

while sim:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sim = False

    con.window.fill(con.black)

    # Movimento das particulas
    for p in lista_particula:
        p.movimento()
    # Para cada duas partículas na lista de partículas, calcular a colisão de uma à outra
    iteracao = True
    aaa = False
    while iteracao == True:
        lista = lista_particula.copy()
        for p in lista:
            for _ in lista:
                aicnatsid = math.sqrt((p.x - _.x)**2 + (p.y - _.y)**2)
                if p.elemento != _.elemento and aicnatsid <= p.raio + _.raio:
                    if p.elemento != "C" and _.elemento != "C" and p.elemento != "D" and _.elemento != "D":

                        momentox = ((p.momento_x) + (_.momento_x)) / (p.massa + _.massa)
                        momentoy = ((p.momento_y) + (_.momento_y)) / (p.massa + _.massa)
            
                        nova = classes.Particula(
                        (p.x),
                        (p.y),
                        con.MASSA_NOVA1,
                        momentox, # / (2*con.MASSA_NOVA1),
                        momentoy, # / (2*con.MASSA_NOVA1),
                        con.green,
                        "C"
                    )   
                        lista_particula.append(nova)
                        del lista_particula[lista_particula.index(p)]
                        del nova

                        nova = classes.Particula(
                        (_.x),
                        (_.y),
                        con.MASSA_NOVA2,
                        momentox / (2*con.MASSA_NOVA2),
                        momentoy / (2*con.MASSA_NOVA2),
                        con.yellow,
                        "D"
                    )
                        # lista_particula.append(nova)
                        del lista_particula[lista_particula.index(_)]
                        del nova
                        del lista

                        aaa = True
                        break
                    else:
                        p.colisao(_)

                else:
                    p.colisao(_)

            if aaa == True:
                aaa = False
                break

            iteracao = False

    if Plot_Do_Histograma_Vel == "Y":
        lista_vel = []
        for p in lista_particula:
            vel_True = math.sqrt((abs(p.speed_x))**2 + (abs(p.speed_y))**2)
            lista_vel.append(vel_True)
        ax.clear()
        ax.hist(lista_vel, bins = 20)
        ax.set_xlabel("Velocidade")
        ax.set_ylabel("Nº de Partículas")
        ax.set_title("Distribuição de Maxwell-Boltzmann")
        fig.canvas.draw_idle()
        fig.canvas.flush_events()
    
    c1,c2,c3,c4 = 0,0,0,0
    for p in lista_particula:
        if p.elemento == "A":
            c1 += 1
        if p.elemento == "B":
            c2 += 1
        if p.elemento == "C":
            c3 += 1
        if p.elemento == "D":
            c4 += 1
    axo.clear()
    ax1.append(c1)
    ax2.append(c2)
    ax3.append(c3)
    ax4.append(c4)
    axo.plot(ax1)
    axo.plot(ax2)
    axo.plot(ax3)
    axo.plot(ax4)
    axo.set_xlabel("Cada ciclo de simulation")
    axo.set_ylabel("consentarassaum")
    axo.set_title("Concentração de cada tipo de partícula")
    figo.canvas.draw_idle()
    figo.canvas.flush_events()

    # Desenho de cada partícula
    for p in lista_particula:
        p.desenho()

    pygame.display.update()
    c.tick(60) # Taxa de atualização do display

pygame.quit()
plt.close()