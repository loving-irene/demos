import pygame

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode([width,height])
keep_going = True
pic = pygame.image.load('../imgs/baseball.png')

timer = pygame.time.Clock()
speedx = 5
speedy = 5

picx = 1
picy = 1
BLACK = (0,0,0)
WHITE = (255,255,255)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    if picx <= 0 or picx + pic.get_width() > width:
        speedx = -speedx

    if picy <= 0 or picy + pic.get_height() > height:
        speedy = -speedy

    if picx <= width:
        picx += speedx
        picy += speedy
    else:
        picx -= speedx
        picy -= speedy
    screen.fill(WHITE)
    screen.blit(pic,(picx,picy))
    pygame.display.update()
    timer.tick(60)

pygame.quit()