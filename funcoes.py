import pygame
import random as rd
import math
import numpy as np

import classes
import constantes as con

def CriarParticulas(MASSA1,MASSA2,VEL_X_MAX, VEL_Y_MAX):
    p = classes.Particle(rd.randint(20, con.width - 20),rd.randint(20, con.height - 20), rd.choice((MASSA1,MASSA2)),rd.randint(0,VEL_X_MAX), rd.randint(0,VEL_Y_MAX))
    return p