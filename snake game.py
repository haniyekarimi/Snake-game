import turtle
import time
import random

#صفحه بازي
wn = turtle.Screen()
wn.title(":)مار بازي")
wn.bgcolor("DarkSeaGreen3")
wn.setup(width=600, height=600)
wn.tracer(0)

#سرمار
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "Stop"

#غذا
food = turtle.Turtle()
colors = random.choice(["red", "green", "black"])
shapes = random.choice(["square", "triangle", "circle"])
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

#نمايش امتياز
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0" , align="center", font =("candara", 24, "bold"))

#تنظيم دکمه هاي حرکت
def goup() :
    if head.direction != "down" :
        head.direction = "up"
def godown() :
    if head.direction != "up" :
        head.direction = "down"
def goleft() :
    if head.direction != "right" :
        head.direction =  "left" 
def goright () :
    if head.direction != "left" :
        head.direction = "right"
    
def move () :
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x+20)

#تعيين دکمه حرکت
wn.listen()
wn.onkeypress(goup,  "w" )
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")


segments = []
score = 0
high_score = 0
delay = 0.1

while True:
      wn.update()

      #بررسي برخورد به ديوار
      if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                #ريست شدن بازي
                 time.sleep(1)
                 head.goto(0, 0)
                 head.direction = "Stop"
                 for segment in segments:
                        segment.goto(1000, 1000)
                 segments.clear()
                 score = 0
                 delay = 0.1
                 pen.clear()
                 pen.write("Score : {} High Score : {} ".format( score, high_score), align="center", font=("candara", 24, "bold"))


      if head.distance(food) < 20:
               #جابه جايي غذا
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                food.goto(x, y)#امتيازدهي
                delay -= 0.001
                score += 10
                if score > high_score:
                        high_score = score
                pen.clear()
                pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("candara", 24, "bold"))

                        #ساختار بدن مار
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("blue")
                new_segment.penup()
                segments.append(new_segment)
        #حرکت بدن مار
      for index in range(len(segments)-1, 0, -1):
               x = segments[index-1].xcor()
               y = segments[index-1].ycor()
               segments[index].goto(x,y)
      if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
      move()
                

    
      for segment in segments:
             if segment.distance(head) < 20:
                      #ريست شدن بازي
                      time.sleep(1)
                      head.goto(0, 0)
                      head.direction = "Stop"
                      for segment in segments:
                             segment.goto(1000, 1000)
                      segments.clear()
                      score = 0
                      delay = 0.1
                      pen.clear()
                      pen.write("Score : {} High Score : {} ".format( score, high_score), align="center", font=("candara",24, "bold"))
      time.sleep(delay)
wn.mainloop()

    
        
    

