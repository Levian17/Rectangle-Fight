from random import randint
from pygame.locals import Rect

class MovingRect: # Constructor
    def __init__(self, rect, speed, color, screen_height, screen_width):
        self.rect = rect
        self.color = color
        self.speed = speed
        self.screen_height = screen_height
        self.screen_width = screen_width

    def move(self): 
        ''' Mueve el rectangulo hasta alcanzar un borde de la pantalla,
        una vez lo alcanza, invierte la direccion. '''
        self.rect.move_ip(self.speed)
        if self.rect.top > self.screen_height:
            self.speed[1] *= -1
        if self.rect.bottom < 0:
            self.speed[1] *= -1
        if self.rect.right > self.screen_width:
            self.speed[0] *= -1
        if self.rect.left < 0:
            self.speed[0] *= -1

def movingRects_generation(rect_num: int, screen_width: int, screen_height: int) -> list[MovingRect]:
    ''' Toma la altura y ancho de la pantalla y devuelve una lista con rect_num numero de MovingRects
    con posiciones y colores aleatorios.'''
    rect_list = []

    colors = {
        0 : (255, 0, 0), # RED
        1 : (0, 255, 0), # BLUE
        2 : (0, 0, 255), # GREEN
    }

    for _ in range(rect_num):
        # Generamos posicione aleatorias para los cuadrados
        x = randint(0, screen_width - 50)
        y = randint(0, screen_height - 50)
        color = colors[randint(0, 2)]
        rect_list.append(MovingRect(Rect(x, y, 50, 50), [1,1], color, screen_height, screen_width))

    return rect_list