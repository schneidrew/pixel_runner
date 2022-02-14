import pygame as pg
from sys import exit
from settings import *
from random import randint, choice
from player import Player
from obstacle import Obstacle


def display_score():

    current_time = pg.time.get_ticks() - start_time
    score_num = current_time // 100
    score_surf = test_font.render(f'SCORE: {score_num}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return score_num


def collision_sprite():
    if pg.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


# def obstacle_movement(obstacle_list:list, surf, speed:int=5):
#
#     if obstacle_list:
#         for rect_ in obstacle_list:
#             rect_.x -= speed
#             screen.blit(surf, rect_)
#
#         obstacle_list = [obst for obst in obstacle_list if obst.right > 0]
#
#         return obstacle_list
#     else: return []
#
#
# def obstacle_collision(player, *obstacles):
#     is_active = True
#     if obstacles:
#         for obst in obstacles:
#             if obst:
#                 for rect in obst:
#                     if player.colliderect(rect):
#                         is_active = False
#
#     return is_active


# def player_animation(surf, index):
#     # play walking animation if player is on the floor
#     # display jump surface when player is not on the floor
#
#     if player_rect.bottom < 300:
#         surf = player_jump
#     else:
#         index += 0.1
#         surf = player_walk[int(index) % 2]
#
#     return surf, index


pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption(game_title)
clock = pg.time.Clock()
test_font = pg.font.Font('font/Pixeltype.ttf', 50)

game_active = False
start_time = 0
score_num = 0
bg_music = pg.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

player = pg.sprite.GroupSingle()
player.add(Player())

obstacle_group = pg.sprite.Group()

sky_surf = pg.image.load('graphics/Sky.png').convert()
ground_surf = pg.image.load('graphics/ground.png').convert()

# score_surf = test_font.render("MY GAME", False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(400, 50))

# #Snail
# snail_frame_1 = pg.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pg.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surf = snail_frames[snail_frame_index]
#
# #Fly
# fly_frame_1 = pg.image.load('graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = pg.image.load('graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surf = fly_frames[fly_frame_index]
#
# snail_rect_list = []
# fly_rect_list = []
#
# player_walk_1 = pg.image.load('graphics/player/player_walk_1.png').convert_alpha()
# player_walk_2 = pg.image.load('graphics/player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
#
# player_jump = pg.image.load('graphics/player/jump.png').convert_alpha()
#
# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(midbottom=(80, 300))
# player_grav = 0

#intro screen
player_stand = pg.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pg.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center=(400,80))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pg.USEREVENT + 2
pg.time.set_timer(snail_animation_timer, 500)

fly_animation_time = pg.USEREVENT + 3
pg.time.set_timer(fly_animation_time, 300)

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if game_active:
            # if event.type == pg.KEYDOWN:
            #     if event.key == pg.K_SPACE:
            #         if player_rect.bottom == 300:
            #             player_grav = -20
            #
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos):
            #         player_grav =-20

            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail'])))

            # if event.type == snail_animation_timer:
            #     snail_frame_index = (snail_frame_index + 1) % 2
            #     snail_surf = snail_frames[snail_frame_index]
            #
            # if event.type == fly_animation_time:
            #     fly_frame_index = (fly_frame_index + 1) % 2
            #     fly_surf = fly_frames[fly_frame_index]

        else:
            if event.type == pg.KEYDOWN:
                game_active = True
                # snail_rect.left = 800
                start_time = pg.time.get_ticks()

    if game_active:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0, 300))
        score_num = display_score()


        # pg.draw.rect(screen, '#c0e8ec', score_rect)
        # pg.draw.rect(screen, '#c0e8ec', score_rect,10)
        # screen.blit(score_surf, score_rect)

        # player_grav += 1
        # player_rect.bottom += player_grav
        # if player_rect.bottom >=300:
        #     player_rect.bottom = 300
        #
        # player_surf, player_index = player_animation(player_surf, player_index)
        # screen.blit(player_surf, player_rect)

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

        # Obstacle movement
        # snail_rect_list = obstacle_movement(snail_rect_list,snail_surf, randint(4,7))
        # fly_rect_list = obstacle_movement(fly_rect_list, fly_surf, randint(5,8))
        #
        # game_active = obstacle_collision(player_rect, snail_rect_list, fly_rect_list)

    else:

        fly_rect_list = []
        snail_rect_list = []

        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        # player_rect.midbottom = (80,300)
        # player_grav=0

        score_message = test_font.render(f'Your Score: {score_num}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score_num == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pg.display.update()
    clock.tick(fps_)

