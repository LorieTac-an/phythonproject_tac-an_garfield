import turtle as t

t.pensize(10)
t.speed(8)

def head():

	t.pensize(10)
	t.penup()
	t.goto(160,600)
	t.pendown()
	t.color("black","#F9B320")
	
	t.begin_fill()
	t.setheading(135)
	t.circle(220,90)
	
	t.setheading(220)
	t.circle(350,50)
	
	t.setheading(265)
	t.circle(150,110)
	
	t.penup()
	t.goto(160,600)
	t.pendown()
	
	t.setheading(320)
	t.circle(-350,50)
	
	t.setheading(275)
	t.circle(-150,110)
	
	t.color("#F9B320")
	t.goto(-88,174)
	t.end_fill()
	
	t.pensize(12)
	t.goto(160,600)
	
	
def body():
	
	t.pensize(10)
	t.penup()
	t.goto(140,150)
	t.pendown()
	t.color("black","#F9B320")
	
	t.begin_fill()
	t.setheading(135)
	t.circle(200,90)
	
	t.setheading(220)
	t.circle(320,50)
	
	t.setheading(265)
	t.circle(140,90)
	
	t.setheading(345)
	t.circle(520,32)
	
	t.setheading(20)
	t.circle(120,70)

	t.setheading(83.7)
	t.circle(350,51.5)

	t.end_fill()

def arms():

	t.pensize(10)
	t.penup()
	t.goto(-170,200)
	t.pendown()
	t.color("black","#F9B320")

	t.begin_fill() 
	t.setheading(195)
	t.circle(450,20)
	
	t.setheading(220)
	t.circle(50,80)
	
	t.setheading(300)
	t.circle(200,31)
	
	t.setheading(73)
	t.circle(-350,18)
	
	t.color("#F9B320")
	t.setheading(0)
	t.forward(385)
 
	t.color("black","#F9B320")
	t.setheading(300)
	t.circle(-350,18);

	t.setheading(10)
	t.circle(200,31)
	
	t.setheading(40)
	t.circle(50,80)
	
	t.setheading(135)
	t.circle(450,22)
	
	t.goto(-170,200)
	t.end_fill()
	
	t.penup()
	t.goto(-175,100)
	t.pendown()
	
	t.setheading(195)
	t.circle(200,23)
	
	t.penup()
	t.goto(-200,85)
	t.pendown()
	
	t.setheading(320)
	t.circle(15,80)
	
	t.penup()
	t.goto(155,110)
	t.pendown()
	
	t.setheading(345)
	t.circle(-200,27)
	
	t.penup()
	t.goto(180,95)
	t.pendown()
	
	t.setheading(220)
	t.circle(-15,80)


def leg1():
	
	t.pensize(10)
	t.penup()
	t.goto(-170,-220)
	t.pendown()
	t.color("black","#F9B320")
	
	t.begin_fill()
	t.setheading(275)
	t.forward(300)
	t.setheading(135)
	t.circle(18,130)
	
	t.penup()
	t.goto(-165,-535)
	t.pendown()
	
	t.setheading(165)
	t.circle(270,65)
	
	#toe1
	t.setheading(230)
	t.circle(40,165)
	
	t.color("#F9B320")
	t.goto(-395,-620)
	
	#toe2		
	t.color("black")
	t.setheading(230)
	t.circle(45,170)
	
	t.color("#F9B320")
	t.goto(-335,-630)
	
	#toe3	
	t.color("black")	
	t.setheading(230)
	t.circle(40,220)
	
	t.setheading(310)
	t.circle(50,110)
	
	t.setheading(4)
	t.forward(140)
	
	t.setheading(20)
	t.circle(40,120)
	
	t.setheading(145)
	t.forward(40)
	
	t.setheading(95)
	t.forward(310)
	
	t.color("#F9B320")
	t.goto(-170,-220)
	t.end_fill()
	
def leg2():
	
	t.pensize(10)
	t.penup()
	t.goto(130,-220)
	t.pendown()
	t.color("black","#F9B320")
	
	t.begin_fill()
	t.setheading(255)
	t.forward(280)
	
	t.penup()
	t.goto(50,-495)
	t.pendown()
	t.setheading(45)
	t.circle(-18,130)
	
	t.penup()
	t.goto(65,-510)
	t.pendown()

	t.setheading(15)
	t.circle(-240,65)
	
	#toe1
	t.setheading(300)
	t.circle(-50,100)
	
	t.color("#F9B320")
	t.goto(290,-595)
	
	#toe2		
	t.color("black")
	t.setheading(310)
	t.circle(-45,170)
	
	t.color("#F9B320")
	t.goto(230,-605)
	
	#toe3	
	t.color("black")	
	t.setheading(310)
	t.circle(-40,220)
	
	t.setheading(230)
	t.circle(-50,110)
	
	t.setheading(176)
	t.forward(130)
	
	t.setheading(150)
	t.circle(-40,120)
	
	t.setheading(50)
	t.forward(40)
	
	t.setheading(75)
	t.forward(265)
	
	t.color("#F9B320")
	t.goto(130,-220)
	t.end_fill()
	
	t.penup()
	t.goto(-99,-254)
	t.pendown()
	t.color("black")
	
	t.setheading(349)
	t.circle(520,18)
	
def tail():
	
	t.penup()
	t.goto(15,-260)
	t.pendown()
	t.color("black","#F9B320")
	
	t.begin_fill()
	t.setheading(250)
	t.forward(300)
	
	t.setheading(235)
	t.circle(-300,55)
	
	t.setheading(160)
	t.circle(-110,190)

	t.penup()
	t.goto(-250,-490)
	t.pendown()
	
	t.setheading(60)
	t.forward(30)
	t.setheading(45)
	t.circle(-13,130)
	
	t.penup()
	t.goto(-222,-490)
	t.pendown()
			
	t.setheading(60)		
	t.forward(295)
	t.goto(15,-260)
	t.end_fill()
	
	t.penup()
	t.goto(-85,-245)
	t.pendown()
	t.fillcolor("black")
	t.begin_fill()	
	t.setheading(300)
	t.circle(230,28)
	t.goto(15,-260)
	t.goto(-85,-245)
	t.end_fill()
	
	t.penup()
	t.goto(-202,-490)
	t.pendown()
	t.pensize(10)
			
	t.setheading(60)		
	t.forward(250)
	
	t.penup()
	t.goto(-185,-485)
	t.pendown()
	t.pensize(8)
			
	t.setheading(60)		
	t.forward(235)
	
	t.penup()
	t.goto(-175,-485)
	t.pendown()
	t.pensize(8)
			
	t.setheading(60)		
	t.forward(150)
	
	t.penup()
	t.goto(-247,-470)
	t.pendown()
	t.pensize(3)
	t.begin_fill()
	
	t.setheading(165)
	t.circle(120,35)
	
	t.setheading(5)
	t.circle(-120,30)
	
	t.setheading(165)
	t.circle(120,40)
	
	t.setheading(3)
	t.circle(-120,35)
	
	t.setheading(160)
	t.circle(120,45)
	
	t.setheading(5)
	t.circle(-120,35)
	
	t.setheading(160)
	t.circle(120,40)
	
	t.setheading(3)
	t.circle(-120,40)
	
	t.setheading(165)
	t.circle(120,35)
	
	t.setheading(5)
	t.circle(-120,30)
	
	t.setheading(200)
	t.forward(100)
	t.setheading(107)
	t.circle(-110,130)
	t.end_fill()
	
def hair():
	
	strand2(-198,65,235)
	strand(-230,-45,240,-220,-55)
	strand(-230,-140,272,-220,-135)
	
	strand(205,-10,80,190,-5)
	strand(210,-110,60,200,-105)
	strand(185 ,-200,35,180,-190)

def strand(x,y,deg,x2,y2):
	t.pensize(3)
	
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color("black","black")
	
	t.begin_fill()
	t.setheading(deg)
	t.circle(90,50)
	t.setheading(deg+48)
	t.circle(6,170)
	t.setheading(deg-122)
	t.circle(-90,50)
	t.end_fill()
	
	t.penup()
	t.goto(x2,y2)
	t.pendown()
	
	t.begin_fill()
	t.setheading(deg)
	t.circle(50,50)
	t.setheading(deg+48)
	t.circle(4,180)
	t.setheading(deg-122)
	t.circle(-50,50)
	t.end_fill()	

def strand2(x,y,deg):
	
	t.pensize(3)
		
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color("black","black")	
	t.begin_fill()
	t.setheading(deg)
	t.circle(250,20)
	t.setheading(deg)
	t.circle(8,170)
	t.setheading(deg-149)
	t.circle(-250,20)
	t.end_fill()
	
	t.penup()
	t.goto(x+2,y-20)
	t.pendown()
	
	t.begin_fill()
	t.setheading(deg+10)
	t.circle(200,15)
	t.setheading(deg+10)
	t.circle(6,170)
	t.setheading(deg-142)
	t.circle(-200,15)
	t.end_fill()
	

def face():
	
	scale = (450-1)/400
	t.pensize(8)
	t.penup()
	t.goto(0*scale,550*scale)
	t.pendown()
	t.color("black","#F9B320")
	
	t.begin_fill()
	t.setheading(270)
	t.forward(280*scale)
	 
	t.setheading(210)
	t.circle(-100*scale,100)
	 
	t.setheading(105)
	t.circle(-260*scale,50)
	
	t.setheading(49)
	t.circle(-80*scale,84)
	t.end_fill()
	
	t.penup()
	t.goto(0*scale,550*scale)
	t.pendown()

	t.begin_fill()
	t.setheading(270)
	t.forward(280*scale)
	 
	t.setheading(330)
	t.circle(100*scale,100)
	 
	t.setheading(75)
	t.circle(260*scale,50)
	
	t.setheading(131)
	t.circle(80*scale,84)
	t.end_fill()
	
	
def mouth():
	
	#mouth
	scale = (450-13)/400
	t.penup()
	t.goto(-152*scale,380*scale)
	t.pendown()
	t.pensize(8)
	t.color("black","#FEF493")
	
	t.begin_fill()
	t.setheading(160)
	t.circle(60*scale,90)
	
	t.setheading(250)
	t.circle(30*scale,120)
	
	t.color("#FEF943")
	t.setheading(30)
	t.forward(20*scale)
	t.color("black","#FEF493")
	
	t.penup()
	t.goto(-180*scale,330*scale)
	t.pendown()
	
	t.setheading(240)
	t.circle(13*scale,100)
	
	t.penup()
	t.goto(-170*scale,320*scale)
	t.pendown()
	
	t.setheading(240)
	t.circle(90*scale,70)
	
	t.setheading(315)
	t.circle(100*scale,110)
	
	#e
	t.penup()
	t.goto(152*scale ,380*scale)
	t.pendown()
	t.pensize(8)
	
	t.setheading(20)
	t.circle(-60*scale,90)
	
	t.setheading(290)
	t.circle(-30*scale,120)
	
	t.color("#FEF493")
	t.setheading(150)
	t.forward(20*scale)
	t.color("black","#FEF493")
	
	t.penup()
	t.goto(180*scale,330*scale)
	t.pendown()
	
	t.setheading(300)
	t.circle(-13*scale,100)
	
	t.penup()
	t.goto(170*scale,320*scale)
	t.pendown()
	
	t.setheading(300)
	t.circle(-90*scale,70)
	
	t.setheading(225)
	t.circle(-100*scale,110)
	
	t.penup()
	t.goto(152*scale,380*scale)
	t.pendown()
	t.goto(-152*scale,380*scale)
	t.end_fill()
	
def whiteeyes():
	
	scale = (450-1)/400
	t.penup()
	t.goto(0*scale,310*scale)
	t.pendown()
	t.color("black","white")
	
	t.begin_fill()
	t.setheading(180)
	t.circle(-1000*scale,8.3)

	t.pensize(3)
	t.setheading(290)
	t.circle(100*scale,100)
	t.goto(0*scale ,310*scale)
	t.end_fill()
	
	t.penup()
	t.goto(0*scale, 310*scale)
	t.pendown()
	t.color("black","white")
	
	t.pensize(8)
	t.setheading(180)
	t.circle(-1000*scale,8.3)
	
	t.setheading(290)
	t.circle(100*scale,100)
	t.goto(0*scale,310*scale)
	
	#whiteeyes2
	t.penup()
	t.goto(0*scale,310*scale)
	t.pendown()
	t.color("black","white")
	
	t.begin_fill()
	t.setheading(360)
	t.circle(1000*scale,8.3)

	t.pensize(3)
	t.setheading(250)
	t.circle(-100*scale,100)
	t.goto(0*scale,310*scale)
	t.end_fill()
	
	t.penup()
	t.goto(0*scale,310*scale)
	t.pendown()
	t.color("black","white")
	
	t.pensize(8)
	t.setheading(360)
	t.circle(1000*scale,8.3)
	
	t.setheading(250)
	t.circle(-100*scale,100)
	t.goto(0*scale,310*scale)
	
	#iris
	
	t.penup() 
	t.goto(-60*scale,313*scale)
	t.pendown()
	t.fillcolor("black")
	
	t.begin_fill()
	t.setheading(305)
	t.circle(30*scale,105)
	t.pensize(3)
	t.goto(-60*scale,310*scale)
	t.end_fill()
	
	t.penup() 
	t.goto(60*scale ,310*scale)
	t.pendown()
	t.fillcolor("black")
	
	t.begin_fill()
	t.setheading(235)
	t.circle(-30*scale,105)
	t.pensize(3)
	t.goto(60*scale,310*scale)
	t.end_fill()
	
	#nose
	t.penup()
	t.goto(-35*scale,240*scale)
	t.pendown()
	t.pensize(6)
	t.fillcolor("#FDD2CC")
	
	t.begin_fill()
	t.setheading(313)
	for _ in range(2):
		t.circle(50*scale,90)
		t.circle(20*scale,90)
	t.end_fill()
	
def ears():
	
	t.color("black","#F9B320")
	t.penup()
	t.goto(0,660)
	t.pendown()
	t.pensize(8)
	
	t.begin_fill()
	t.setheading(135)
	t.circle(160,55)
	t.goto(0,600)
	
	t.penup()
	t.goto(0,660)
	t.pendown()
	t.pensize(8)
	
	t.setheading(45)
	t.circle(-160,50)
	t.goto(0,600)
	t.end_fill()
	
	#1
	t.penup()
	t.goto(0,600)
	t.pendown()
	t.pensize(8)
	
	t.begin_fill()
	t.setheading(110)
	t.circle(160,50)
	
	t.setheading(150)
	t.circle(60,110)
	
	t.setheading(265)
	t.circle(140,53)
	t.end_fill()
	
	#2
	t.penup()
	t.goto(0,600)
	t.pendown()
	t.pensize(8)
	
	t.begin_fill()
	t.setheading(70)
	t.circle(-160,50)
	
	t.setheading(30)
	t.circle(-60,110)
	
	t.setheading(275)
	t.circle(-140,53)
	t.end_fill()
	
	#details
	t.penup()
	t.goto(-110,700)
	t.pendown()
	t.pensize(3)
	t.fillcolor("black")
	
	t.begin_fill()
	t.setheading(325)
	t.circle(-230,20)
	
	t.setheading(135)
	t.circle(230,23)
	
	t.setheading(320)
	t.circle(-230,15)

	t.setheading(145)
	t.forward(60)
	
	t.setheading(305)
	t.forward(55)
	
	t.setheading(147)
	t.circle(-230,15)
	
	t.setheading(290)
	t.circle(230,15)
	
	t.setheading(143)
	t.circle(-230,14)
	
	t.setheading(290)
	t.circle(230,15)
	
	t.setheading(143)
	t.circle(-230,14)
	
	t.setheading(290)
	t.circle(230,15)
	
	t.setheading(143)
	t.circle(-230,13)
	
	t.setheading(100)
	t.circle(-60,113)
	t.end_fill()
	
	#details2
	t.penup()
	t.goto(110,700)
	t.pendown()
	t.pensize(3)
	t.fillcolor("black")
	
	t.begin_fill()
	t.setheading(215)
	t.circle(230,20)
	
	t.setheading(45)
	t.circle(-230,23)
	
	t.setheading(220)
	t.circle(230,15)

	t.setheading(35)
	t.forward(60)
	
	t.setheading(230)
	t.forward(55)
	
	t.setheading(33)
	t.circle(230,15)
	
	t.setheading(250)
	t.circle(-230,15)
	
	t.setheading(37)
	t.circle(230,14)
	
	t.setheading(250)
	t.circle(-230,15)
	
	t.setheading(37)
	t.circle(230,14)
	
	t.setheading(250)
	t.circle(-230,15)
	
	t.setheading(37)
	t.circle(230,11)
	
	t.setheading(70)
	t.circle(60,113)
	t.end_fill()

def hair2():
	
	smallstrand2(-148,585,214)
	single(-148,585,214,50)
	smallstrand2(-215,500,235)
	single(-210,500,235,50)
	single(-200,490,240,90)
	stranding(-255,310,260,-245,310)
	single(-230,320,270,120)
	stranding(-215,220,305,-205,230)
	
	smallstrand2(210,525,122)
	single(210,525,110,50)
	smallstrand2(250,420,95)
	single(241,445 , 95,50)
	single(230,440,100,90)
	stranding(250,250,50,240,260)
	single(225,270,50,120)
	stranding(160,180,10,160,195)

def stranding(x,y,deg,x2,y2):
	t.pensize(3)
	
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color("black","black")
	
	t.begin_fill()
	t.setheading(deg)
	t.circle(90,50)
	t.setheading(deg+48)
	t.circle(6,170)
	t.setheading(deg-122)
	t.circle(-90,50)
	t.end_fill()
	
	t.penup()
	t.goto(x2,y2)
	t.pendown()
	
	t.begin_fill()
	t.setheading(deg)
	t.circle(50,50)
	t.setheading(deg+48)
	t.circle(4,180)
	t.setheading(deg-122)
	t.circle(-50,50)
	t.end_fill()	

def smallstrand2(x, y, deg):
    
    scaling_factor = (250 - 50) / 250
    t.pensize(3 * scaling_factor)  # Scaling the pen size

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    t.setheading(deg)
    t.circle(250 * scaling_factor, 20)
    t.setheading(deg)
    t.circle(8 * scaling_factor, 170)
    t.setheading(deg - 149)
    t.circle(-250 * scaling_factor, 20)
    t.end_fill()
    
def single(x,y,deg,size):
    scaling_factor = (250 - size) / 250
    t.penup()
    t.goto(x - 3  * scaling_factor, y - 20 * scaling_factor)
    t.pendown()

    t.begin_fill()
    t.setheading(deg + 10)
    t.circle(200 * scaling_factor, 15)
    t.setheading(deg + 10)
    t.circle(6 * scaling_factor, 170)
    t.setheading(deg - 142)
    t.circle(-200 * scaling_factor, 15)
    t.end_fill()
    
def single2(x,y,deg,size):
    
    scaling_factor = (250 - size) / 250
    t.penup()
    t.goto(x - 3  * scaling_factor, y - 20 * scaling_factor)
    t.pendown()

    t.begin_fill()
    t.setheading(deg + 340)
    t.circle(-200 * scaling_factor, 15)
    t.setheading(deg + 340)
    t.circle(-6 * scaling_factor, 170)
    t.setheading(deg - 228)
    t.circle(200 * scaling_factor, 15)
    t.end_fill()
	
def whiskers():
	
	t.color("black","black")
	single(-180,600,125, -187)
	single(-190,590,140, -187)
	single(-200,580,155, -187)
	
	single2(195,600,60,-187)
	single2(205,590,45,-187)
	single2(215,580,30,-187)
	
	

tail()
body()
leg2()
leg1()
arms()
head()
hair()
mouth()
hair2()
ears()
face()
whiteeyes()
whiskers()




t.hideturtle()
t.done()