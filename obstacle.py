import pygame as pg
from random import randint


class Obstacle(pg.sprite.Sprite):
    def __init__(self, type_:str = 'snail'):
        super().__init__()

        if type_ == 'fly':
            fly_1 = pg.image.load('graphics/fly/Fly1.png').convert_alpha()
            fly_2 = pg.image.load('graphics/fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            self.y_pos = 210
            self.speed = 6
        else:
            snail_1 = pg.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pg.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            self.y_pos = 300
            self.speed = 5

        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), self.y_pos))

    def __del__(self):
        print("Object is being deleted")
        return

    def animation_state(self):

        self.animation_index += 0.1

        self.image = self.frames[int(self.animation_index) % 2]

        return

    def obstacle_movement(self):

        self.rect.x -= self.speed

        return

    def update(self):

        self.animation_state()
        self.rect.x -= self.speed
        self.destroy()

        return

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

