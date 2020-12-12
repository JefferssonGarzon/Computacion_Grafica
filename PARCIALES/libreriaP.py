import pygame
import math

ANCHO= 1000
ALTO= 600
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def ProdE(v, es):
    ls = []
    for comp in v:
        pe = comp*es
        ls.append(pe)
    return ls

def tras(p, T):
    xp= p[0]+T[0]
    yp= p[1]+T[1]
    return [xp,yp]

def Punto(p, pos):
    pygame.draw.circle(p,AZUL,pos,5)
    pygame.display.flip()

def Cart_Pant(centro, p):
    xp=centro[0] + p[0]
    yp=centro[1] - p[1]
    return [xp,yp]

def Escala(p, S):
    xp = p[0] * S[0]
    yp = p[1] * S[1]
    return [int(xp),int(yp)]

def rotacion(p, a):
    ar = math.radians(a)
    xr = (p[0] * math.cos(ar)) + (p[1] * math.sin(ar))
    yr = -(p[0] * math.sin(ar)) + (p[1] * math.cos(ar))
    return [int(xr), int(yr)]