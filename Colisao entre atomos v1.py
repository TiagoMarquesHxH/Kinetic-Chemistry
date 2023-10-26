# Import das bibliotecas utilizadas e de arquivos.py
from cProfile import label
from sre_constants import JUMP
import pygame
import random as rd
import math
import numpy as np
import constantes as con
import classes
import funcoes as fn
import matplotlib.pyplot as plt
import pandas as pd
# from scipy.interpolate import splrep, BSpline


Plot_Do_Histograma_Vel = " "
SalvarConcentracoes = "Y"

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
    valores_p = fn.CriarParticulasRd(8,6,7,7,con.red,con.blue,"A","B")
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

c1,c2,c3,c4 = 0,0,0,0
for p in lista_particula:
    if p.elemento == "A":
        c1+=1
    if p.elemento == "B":
        c2+=1
    if p.elemento == "C":
        c3+=1
    if p.elemento == "D":
        c4+=1
ax1.append(c1)
ax2.append(c2)
ax3.append(c3)
ax4.append(c4)

contador = 0

while sim:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sim = False

    con.window.fill(con.black)

    # Movimento das particulas
    for p in lista_particula:
        p.movimento()
    
    for p in lista_particula:
        for n in lista_particula:
            aicnatsid = math.sqrt((p.x - n.x)**2 + (p.y - n.y)**2)
            if ((aicnatsid <= p.raio + n.raio) and (p.elemento == "A" and n.elemento == "B")):
                p.elemento = "C"
                p.cor = con.green
                p.massa = con.MASSA_NOVA1
                n.elemento = "D"
                n.cor = con.yellow
                n.massa = con.MASSA_NOVA2

                p.colisao(n)

            else:
                p.colisao(n)

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
    a1 = axo.plot(ax1, label="A")
    a2 = axo.plot(ax2, label="B")
    a3 = axo.plot(ax3, label="C")
    a4 = axo.plot(ax4, label="D", linestyle = "dotted")
    axo.set_xlabel("Tempo")
    axo.set_ylabel("Partículas")
    axo.set_title("Concentração")
    axo.legend()
    figo.canvas.draw_idle()
    figo.canvas.flush_events()

    # Desenho de cada partícula
    for p in lista_particula:
        p.desenho()

    contador += 1

    pygame.display.update()
    c.tick(60) # Taxa de atualização do display

tempo = range(0,contador+1)

# print (contadorreacao)
df = pd.DataFrame({"C1": ax1, "C2": ax2, "C3": ax3, "C4": ax4, "Tempo": tempo})

df.to_csv(r"C:\Users\tiago220053\OneDrive - ILUM ESCOLA DE CIÊNCIA\4° Semestre\Cinetica Quimica\Kinetic-Chemistry\conc.csv", index=False, header=True)


pygame.quit()
plt.close()