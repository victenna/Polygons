import pygame,math
pygame.init()
screen = pygame.display.set_mode((900, 900))
timer=pygame.time.Clock()
screen.fill('violet')
class Spiral:
    def __init__(self,x0,y0,radius):
        self.x0=x0
        self.y0=y0
        self.angle=0
        
        self.radius=radius
        self.q=-1
        self.pol=[]
        self.k=-1
    def update_spiral(self,speed,delta):
        self.k=self.k+1
        self.angle=self.angle+10
        self.radius=self.radius+self.q*delta
        #if self.k==100:
        if abs(self.radius<2) or abs(self.radius)>200:
            self.q=self.q*-1
            self.k=-1
            self.pol.clear()
        teta0=(self.angle)
        teta=teta0*math.pi/180
        self.x1 = self.x0 + self.radius * math.cos(teta)
        self.y1 = self.y0 + self.radius * math.sin(teta)
        self.pol.append([int(self.x1),int(self.y1)])
        #print(len(self.pol),self.radius,self.k)
        print(teta0)
    def draw_spiral(self,color):
        if self.k>2:
            pygame.draw.lines(screen,color,False,self.pol,5)

spiral=Spiral(400,400,100)# coord x, coord y, radius

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('violet')
    spiral.update_spiral(10,1)
    spiral.draw_spiral('red')
    pygame.display.update()
    timer.tick(50)
