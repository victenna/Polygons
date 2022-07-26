import pygame,math
pygame.init()
screen = pygame.display.set_mode((900, 900))
timer=pygame.time.Clock()
screen.fill('violet')

class Polygon:
    def __init__(self,x0,y0,numSides,radius):
        self.x0=x0
        self.y0=y0
        self.angle=0
        self.numSides=numSides
        self.radius=radius
        self.q=-1
        #self.pol=[]
    def update(self,speed,delta):
        self.pol=[]
        self.angle=self.angle+speed*3.14159/180
        self.radius=self.radius+self.q*delta
        if self.radius<-100 or self.radius>100:
            self.q=self.q*-1
        for i in range(self.numSides):
            self.x1 = self.x0 + self.radius * math.cos(self.angle + math.pi * 2 *i/ self.numSides)
            self.y1 = self.y0 + self.radius * math.sin(self.angle + math.pi * 2 *i/ self.numSides)
            self.pol.append([int(self.x1),int(self.y1)])
    def update1(self,speed,delta):
        self.pol=[]
        self.pol1=[]
        self.angle=self.angle+speed*3.14159/180
        self.radius=self.radius+self.q*delta  #
        if self.radius<-100 or self.radius>100:   #
            self.q=self.q*-1   #
        for i in range(1,6):
            self.x1 = self.x0 + self.radius * math.cos(self.angle + math.pi/10 *(4*i-3))
            self.y1 = self.y0 + self.radius * math.sin(self.angle + math.pi/10 *(4*i-3))
            self.pol.append([int(self.x1),int(self.y1)])
        self.pol1.append(self.pol[0]); self.pol1.append(self.pol[3])
        self.pol1.append(self.pol[1]); self.pol1.append(self.pol[4])
        self.pol1.append(self.pol[2])
    def draw(self,color):
        pygame.draw.polygon(screen,color,self.pol)
    def draw1(self,color):
        pygame.draw.lines(screen,color,True,self.pol1,7)

octagon=Polygon(150,200,8,100)
hexagon=Polygon(400,200,6,70)
pentagon=Polygon(700,200,5,90)
triangle=Polygon(150,500,3,80)
square=Polygon(400,500,4,90)
nonagon=Polygon(700,500,10,70)
star=Polygon(150,750,8,100)
star2=Polygon(400,750,8,80)

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
        if abs(self.radius<2) or abs(self.radius)>120:
            self.q=self.q*-1
            self.k=-1
            self.pol.clear()
        teta0=(self.angle)
        teta=teta0*math.pi/180
        self.x1 = self.x0 + self.radius * math.cos(teta)
        self.y1 = self.y0 + self.radius * math.sin(teta)
        self.pol.append([int(self.x1),int(self.y1)])
    def draw_spiral(self,color):
        if self.k>2:
            pygame.draw.lines(screen,color,False,self.pol,5)

spiral=Spiral(700,750,100)# coord x, coord y, radius

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill('violet')
    octagon.update(5,2); octagon.draw('dark green')
    hexagon.update(3,1); hexagon.draw('blue')
    pentagon.update(-5,0); pentagon.draw('gold')
    triangle.update(-6,1); triangle.draw('red')
    square.update(9,2); square.draw('black')
    nonagon.update(-5,4);nonagon.draw('brown')
    star.update1(2,2); star.draw1('navy')
    star2.update1(-4,0); star2.draw1('brown')
    spiral.update_spiral(10,1)
    spiral.draw_spiral('red')
    pygame.display.update()
    timer.tick(50)
