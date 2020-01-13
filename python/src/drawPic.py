import pygame

pygame.init()

width = 800
height = 600

WHITE = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
radius = 5
mousedown = False

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('click to draw')

keep_going = True
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen,YELLOW,spot,radius)
        pygame.display.update()

pygame.quit()