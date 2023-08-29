import pygame
import random as rd
import math
import numpy as np
import classes
import constantes as con

# Função que cria a partícula, considerando massas e velocidades máximas
def CriarParticulas(MASSA1,MASSA2,VEL_X_MAX, VEL_Y_MAX, COR1, COR2):
    Massa = rd.choice((MASSA1,MASSA2))
    if Massa == MASSA1:
        Cor = COR1
    else:
        Cor = COR2
    p = classes.Particula(
        rd.randint(Massa, con.width - Massa), 
        rd.randint(Massa, con.height - Massa),
        Massa,
        rd.randint(0,VEL_X_MAX),
        rd.randint(0,VEL_Y_MAX),
        Cor
    )
    return p