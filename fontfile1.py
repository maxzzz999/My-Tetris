import pygame, sys
from pygame.locals import *
FPS = 120
fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255,)
GREEN = (0, 255,0, 128)
BLUE = (0, 50, 124, 120)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250, 250)
pygame.mixer.music.load('classic.mp3')
pygame.mixer.music.play(-1, 0.0)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'


while True: # main game loop
    DISPLAYSURF.fill(BLUE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.draw.rect(DISPLAYSURF, WHITE, (150, 200, 200, 100), 2)
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'

    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
          direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)