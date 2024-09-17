import pygame
import constantes
from personaje import Personaje

jugador = Personaje(x=50, y=50)

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,
                                   constantes.ALTO_VENTANA))

pygame.display.set_caption('Mi primer juego')

mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False
    
#Controlar el frame rate
reloj = pygame.time.Clock()

run = True
while run == True:

    #Que vaya a 60 FPS
    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_FONDO)

    #Calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #Mover jugador
    jugador.movimiento(delta_x,delta_y)

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        #Para cerrar el juego
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()

pygame.quit()