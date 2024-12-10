import pygame
from pygame.locals import *
from objects.MovingRect import MovingRect, movingRects_generation

# Parametros iniciales
width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
running = True

# Definicion de los rectangulos
rects = movingRects_generation(5, width, height)

pygame.init() # Se inicia el ciclo
while running: # Ciclo frames
    # Detecta los eventos que ocurren (raton, teclas, etc)
    for event in pygame.event.get(): # Controla la salida, con la X y con ESC
        if event.type == pygame.QUIT:
                running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    for rect in rects: # Desplazamos los rects
        rect.move()

    screen.fill((0,0,0)) # Pintamos la pantalla de negro (actua como refresh)
    for rect in rects: # Pintamos los rectangulos por la pantalla
        pygame.draw.rect(screen, rect.color, rect)

    pygame.display.flip()

pygame.quit()