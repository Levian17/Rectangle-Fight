import pygame
from pygame.locals import *
from objects.MovingRect import MovingRect

# CONSTS COLORES
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

# Parametros iniciales
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
running = True

# Definicion de los rectangulos
rect1 = MovingRect(Rect(100, 100, 50, 50), [1, 1], BLUE, height, width) # Se define el cuadrado
rect2 = MovingRect(Rect(200, 100, 50, 50), [2, 2], GREEN, height, width) # Se define el cuadrado
rect3 = MovingRect(Rect(300, 100, 50, 50), [3, 3], RED, height, width) # Se define el cuadrado
rects = [rect1, rect2, rect3]

pygame.init() # Se inicia el ciclo
while running: # Ciclo
    # Detecta los eventos que ocurren (raton, teclas, etc)
    for event in pygame.event.get(): # Controla la salida, con la X y con ESC
        if event.type == pygame.QUIT:
                running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    for rect in rects:
        rect.move()

    screen.fill((0,0,0))
    for rect in rects:
        pygame.draw.rect(screen, RED, rect)

    pygame.display.flip()

pygame.quit()