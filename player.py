import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = pg.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pg.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_jump = pg.image.load('graphics/player/jump.png').convert_alpha()

        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80,300))
        self.gravity = 0

        self.jump_sound = pg.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.05)

    def player_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
        return

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
        return

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1

            self.image = self.player_walk[int(self.player_index) % 2]

        return

    def update(self) -> None:
        self.player_input()
        self.apply_gravity()
        self.animation_state()

        return
