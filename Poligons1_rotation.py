import pygame,sys,math
from pygame.locals import *
pygame.init()
size = [900, 900]
screen = pygame.display.set_mode(size)
keep_going=True
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
PURPLE=(128,0,128)
LIME=(0,255,0)
GREY=(128,128,18)
TEAL=(0,128,128)
radius=50
timer=pygame.time.Clock()
screen.fill('violet')
numSides=6
tiltAngle=0  #degrees
tiltAngle=tiltAngle*3.14159/180

radius=100
radius1=100
screen.fill('violet')

x0,y0=400,400
def p_olygon(tiltAngle):
    global x
    global y
    
    
keep_going=True
while keep_going: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('violet')
    tiltAngle=tiltAngle+10*3.14159/180
    
    x01,y01=400,400
    radius1=100
    numSides1=6
    pts1 = []
    for i in range(numSides1):
        x1 = x01 + radius1 * math.cos(tiltAngle + math.pi * 2 * i / numSides1)
        y1 = y01 + radius1 * math.sin(tiltAngle + math.pi * 2 * i / numSides1)
        pts1.append([int(x1), int(y1)])

    x02,y02=100,300
    radius2=60
    numSides2=8
    pts2 = []
    for i in range(numSides2):
        x2 = x02 + radius2 * math.cos(tiltAngle + math.pi * 2 * i / numSides2)
        y2 = y02 + radius2 * math.sin(tiltAngle + math.pi * 2 * i / numSides2)
        pts2.append([int(x2), int(y2)])

    x03,y03=600,500
    radius3=90
    numSides3=5
    pts3 = []
    for i in range(numSides3):
        x3 = x03 + radius3 * math.cos(tiltAngle + math.pi * 2 * i / numSides3)
        y3 = y03 + radius3 * math.sin(tiltAngle + math.pi * 2 * i / numSides3)
        pts3.append([int(x3), int(y3)])
    
    pygame.draw.polygon(screen, 'gold', pts1)
    pygame.draw.polygon(screen, 'brown', pts2)
    pygame.draw.polygon(screen, 'red', pts3)
    pygame.display.update()
    timer.tick(10)




