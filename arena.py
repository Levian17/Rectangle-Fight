import pygame
from pygame.locals import *
from random import randint

width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
entity_list: list[pygame.Rect] = []
moving_entities_list: list[pygame.Rect] = []
rect_dimensions = (3, 3)
rect_color = (255, 197, 130)

def spawn_rect(position: tuple):
    random_area_radius = 25
    rect = Rect(position[0] + randint(-random_area_radius, random_area_radius), position[1] - randint(-random_area_radius, random_area_radius), rect_dimensions[0], rect_dimensions[1]) # frame_x, frame_y, height, width
    moving_entities_list.append(rect)
    pygame.draw.rect(screen, rect_color, rect)

def controlador_mouse():
    if pygame.mouse.get_pressed()[0]:
        spawn_rect(pygame.mouse.get_pos())

def colides_with_other_entities(rect: pygame.Rect) -> bool:
    for element in entity_list:
        if rect.colliderect(element):
            return True
    return False

def gravity():
    if moving_entities_list:
        for entity in moving_entities_list:
            if not colides_with_other_entities(entity) and entity.bottom <= 720:
                pygame.draw.rect(screen, (0, 0, 0), entity)
                entity.move_ip(0, 5)
                pygame.draw.rect(screen, rect_color, entity)
            else:
                entity_list.append(entity)
                moving_entities_list.remove(entity)


pygame.init() # Inicio del ciclo
while running: 
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Controla la salida con la X
                running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE: # Controla la salida con ESC
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Controla el click del usuario
            print(event.button)    

    controlador_mouse()
    gravity()
    pygame.display.flip()
pygame.quit() # Cierre del ciclo