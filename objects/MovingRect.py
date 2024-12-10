class MovingRect:
    def __init__(self, rect, speed, color, screen_height, screen_width):
        self.rect = rect
        self.color = color
        self.speed = speed
        self.screen_height = screen_height
        self.screen_width = screen_width

    def move(self):
        self.rect.move_ip(self.speed)
        if self.rect.top > self.screen_height:
            self.speed[1] *= -1
        if self.rect.bottom < 0:
            self.speed[1] *= -1
        if self.rect.right > self.screen_width:
            self.speed[0] *= -1
        if self.rect.left < 0:
            self.speed[0] *= -1