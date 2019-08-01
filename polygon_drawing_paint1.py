import turtle,math,time
wn=turtle.Screen()
wn.setup(800,800)
wn.bgcolor('gold')
import time
time.sleep(1)
t1=turtle.Turtle('triangle')
t1.up()
t1.hideturtle()
t1.speed(0)
t1.pensize(1)
box=25
t2=turtle.Turtle()
t2.hideturtle()
t4=turtle.Turtle()
t4.hideturtle()
t4.up()
Text_font=('Arial',20,'bold')
Text_font1=('Arial',10,'bold')
t4.goto(-250,350)
t4.color('blue')
t4.write('Draw Polygon and Calculate Area', font=Text_font)
t4.up()
t4.goto(50,320)
t4.write('To draw polygon click a mouse on the the screen',\
         font=Text_font1)
t5=turtle.Turtle()
t5.hideturtle()
t5.up()
t5.color('blue')
def grid(dir,a,b,c,d):
     
     for j in range (-11,12):
          t1.setheading(dir)
          t1.penup()
          t1.goto(a*box*j-11*box*b,-box*11*c+box*j*d)
          t1.pendown()
          if j==0:
               t1.pensize(3)
               t1.fd(2*box*11.5)
               t1.stamp()
               t1.fd(-2*box*11.5)
          t1.pensize(1)
          t1.fd(2*box*11)
grid(90,1,0,1,0)
grid(0,0,1,0,1)
t2.goto(-11*box,0)
def numbers(axis):
    for i in range (-11,12):
        t2.write(i)
        t2.fd(box)
        if i==11:
            t2.write(axis,font=('Arial',30,'bold'))
numbers('X')
t2.penup()
t2.goto(5,-11*box)
t2.setheading(90)
numbers('Y')
t3=turtle.Turtle('circle')
t3.shapesize(0.3)
t3.color('blue')
t3.pensize(3)
q=int(wn.textinput('Draw Polygon,Calculate Area','Number of vertices= '))
Q=q-1
n=0
coordX=[0]
coordY=[0]
coord=[]
def click(x,y):
     
    global n,q,coordX,coordY
    if n==0:
         t3.begin_fill()
    n=n+1
    #print(n)
    if n<=(q-1):
        t3.down()
        t3.stamp()
        t3.goto(x,y)
        coordX.append(x/box)
        coordY.append(y/box)
        coordX[n]=round(coordX[n])
        coordY[n]=round(coordY[n])
        coord=tuple(list(zip(coordX,coordY)))
        print (coord)
        if n==(q-1):
             
             t3.stamp()
             t3.goto(0,0)
             coordX.append(0)
             coordY.append(0)
             t3.end_fill()  
    if n==(q-1):
        Sum1=0
        Sum2=0
        print('SUM',Sum1,Sum2)
        for i in range(q):
            Sum1=Sum1+coordX[i]*coordY[i+1]
            Sum2=Sum2+coordY[i]*coordX[i+1]
        Area=abs((Sum1-Sum2)/2)

        t5.goto(-100,-350)
        t5.down()
        t5.write('Polygon Area=',font=Text_font)
        t5.up()
        t5.goto(120,-350)
        t5.write(Area,font=Text_font)
        time.sleep(4)
        t3.clear()
        t5.clear()
        del coordX[:]
        del coordY[:]
        coordX=[0]
        coordY=[0]
        q=int(wn.textinput('Draw Polygon,Calculate Area','Number of vertices= '))
        Q=q-1
        n=0
wn.onclick(click)   
