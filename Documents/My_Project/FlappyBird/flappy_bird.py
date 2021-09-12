import pygame
import sys


def draw_floor():
    screen.blit(floor_surface, (floor_x, 650))
    screen.blit(floor_surface, (floor_x + 576, 650))


pygame.init()
screen = pygame.display.set_mode((576, 750))
clock = pygame.time.Clock()  # FPS

# Game variables
gravity = 0.25
bird_movement = 0


bg_surface = pygame.image.load(
    'C:/Users/Isaac Silva/Documents/My_Project/FlappyBird/assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
# Their is a short way to type this two lines above: bg_surface = pygame.transform.scale2x(pygame.image.load("C:/Users/Isaac Silva/Documents/My_Project/FlappyBird/assets/background-day.png"))
# convert() helps the pygame to read the game easier

floor_surface = pygame.image.load(
    'C:/Users/Isaac Silva/Documents/My_Project/FlappyBird/assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x = 0

bird_surface = pygame.image.load(
    'C:/Users/Isaac Silva/Documents/My_Project/FlappyBird/assets/redbird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
# It's going to creat a rectangle around the bird_surface. The rect command helps to make collision
bird_rect = bird_surface.get_rect(center=(100, 360))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 10

    screen.blit(bg_surface, (0, -250))  # It is calling the bg_surface

    bird_movement += gravity  # controlando o movimento do robo
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x -= 1
    draw_floor()  # It is going to make a loop of the floor, so it can not finish
    if floor_x <= -576:
        floor_x = 0

    # this command is going to write every past commands between while True and pygame.
    pygame.display.update()
    clock.tick(120)  # FPS
