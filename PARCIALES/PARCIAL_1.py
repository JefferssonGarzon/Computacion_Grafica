import pygame
from libreriaP import *
import math

ANCHO = 600
ALTO = 600
AZUL = [0,0,255]
ROJO = [255,0,0]
VERDE = [0,255,0] 
BLANCO = [255,255,255]
NEGRO = [0,0,0]

if __name__ == '__main__':
    romper = False
    ox = 300
    oy = 300
    origen = [ox,oy]


    #declaracion de variables

    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.set_caption("PARCIAL_1") # Etiqueta de la ventana emergente
    clock = pygame.time.Clock()

    fin = False

    color = BLANCO
  

    # radios correspondientes de la elipse
    xRadius = 70 / 2 
    yRadius = 280 / 2

    # radio que abarcan los puntos puestos en las coordenadas
    xRadius_C = 180
    yRadius_C = 180

    # comienzo de grados
    grados = 0

    #ciclo principal de ejecucion
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        
        pantalla.fill(color)
        pygame.draw.line(pantalla, NEGRO,(0,oy),(1000,oy)) # linea con respecto al eje X
        pygame.draw.line(pantalla, NEGRO,(ox,0),(ox,1000))  # linea con respecto al eje Y
        pygame.draw.ellipse(pantalla,[255,0,0], (265,160,70,280), 1) # elipse
    
        
        if grados < 360:
            # ecuaciones de recorrido de la orbita de la elipse, punto (x1,y1)
            x1 = int(math.cos(grados*2*math.pi/360)*xRadius) + 300
            y1 = int(-math.sin(grados*2*math.pi/360)*yRadius) + 300

            #ecuaciones para seguir el punto de que el punto (x1,y1)
            x2 = int(math.cos(grados*2*math.pi/360)*xRadius_C) + 300
            y2 = int(-math.sin(grados*2*math.pi/360)*yRadius_C) + 300

            pygame.draw.circle(pantalla, (ROJO), [x1,y1], 4) # Punto que sigue el perimetro de la elipse
            pygame.draw.circle(pantalla, NEGRO , [300,y2], 3) # circulo que se mueve en el eje Y
            pygame.draw.circle(pantalla, NEGRO, [x2,300], 3) # circulo que se mueve en el eje X
            pygame.draw.line(pantalla, NEGRO,(x2,300),(300,y2)) # union de los puntos correspondientes a los ejes
            grados += 3 
            if grados == 360:
                grados = 0

        #refrescar pantalla
        pygame.display.flip()
        clock.tick(40)
 

    


        

    