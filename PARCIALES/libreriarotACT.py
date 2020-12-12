import pygame
import math

ANCHO=1200
ALTO=800
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def Punto(p, pos, cl=BLANCO ):
    pygame.draw.circle(p,cl,pos,3)
    return p

def RotacionH(p,a):
    ar=math.radians(a)
    print("a: ",a)
    xp=(p[0]*math.cos(ar)) + (p[1]*math.sin(ar))
    yp= -(p[0]*math.sin(ar)) + (p[1]*math.cos(ar))
    return [ int(xp), int(yp)]

def Cart_Pant(centro,p):
    xp=centro[0] + p[0]
    yp=centro[1] - p[1]
    return [xp,yp]

def Escala(p,S):
    xp=p[0]*S[0]
    yp=p[1]*S[1]
    return [int(xp), int(yp)]

def Plano(pan, centro):
    x=centro[0]
    y=centro[1]
    #eje x
    p_ini=[0,y]
    p_fin=[ANCHO,y]
    pygame.draw.line(pan,BLANCO, p_ini, p_fin,1)
    #eje y
    p_ini=[x,0]
    p_fin=[x,ALTO]
    pygame.draw.line(pan,BLANCO, p_ini, p_fin,1)
    return pan
