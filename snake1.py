from tkinter import*
import turtle
import time
import random
from tkinter import messagebox
#def m1():
    #root.quit()
    #sys.exit()
    #exit()
def m2():
        root.destroy()
        delay=0.2
        score=0
        high_score=0

        wn=turtle.Screen()
        wn.title("snake game")
        wn.bgcolor("black")
        wn.setup(width=500,height=500)
        wn.tracer(0)

#for head
   
        head=turtle.Turtle()
        head.speed(0)
        head.shape("circle")
        head.color("red")
        head.penup()
        head.goto(0,0)
        head.direction="up"

    #for  food

        food=turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("white")
        food.penup()
        food.goto( x=random.randint(-240,240),
         y=random.randint(-240,240))

        segment=[]     


        pen=turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle() 
        pen.goto(0,210)
        pen.write("Score: 0   High score: 0",align="center",font=("courier",24,"normal"))

#for movement

        def go_up():
           if head.direction!="down":
             head.direction="up"
        def go_down():
           if head.direction!="up":
             head.direction="down"
        def go_left():
           if head.direction!="right":
             head.direction="left"
        def go_right():
           if head.direction!="left":
              head.direction="right"
        def move():
           if head.direction=="up":
              y=head.ycor()
              head.sety(y+20)
           if head.direction=="down":
              y=head.ycor()
              head.sety(y-20)
           if head.direction=="left":
              x=head.xcor()
              head.setx(x-20)
           if head.direction=="right":
              x=head.xcor()
              head.setx(x+20)

        wn.listen()
        wn.onkeypress(go_up,"w")        
        wn.onkeypress(go_down,"s")        
        wn.onkeypress(go_left,"a")        
        wn.onkeypress(go_right,"d")        

        while True:
            wn.update()

            if head.xcor()>240 or head.xcor()<-240  or head.ycor()>240 or  head.ycor()<-240:
              time.sleep(1)
              head.goto(0,0)
              head.direction="stop"
         
      
              for segments in segment:
                  segments.goto(1000,1000)

              segment.clear()   

              messagebox.showwarning("oops","Game over")
              answer=messagebox.askquestion("Game over","Do u want to quit the game")
              #print(answer)
              if answer=="yes":
                  #wn.exit()
                  sys.exit()
              #else:
                   #m3()


              score=0 

              delay=0.2

              pen.clear()
              pen.write("score: {}  High score: {}".format(score,high_score),align="center",font=("courier",20,"normal"))   

              head.direction="up"



            if head.distance(food)<20:
              x=random.randint(-240,240)
              y=random.randint(-240,240)
              food.goto(x,y)

              new_segment=turtle.Turtle()
              new_segment.speed(0)
              new_segment.shape("circle")
              new_segment.color("green")
              new_segment.penup()
              segment.append(new_segment)

              delay-=0.001

              score+=10

              if score>high_score:
                high_score=score

              pen.clear()
              pen.write("score: {}  High score: {}".format(score,high_score),align="center",font=("courier",20,"normal"))   

            for index in range(len(segment)-1,0,-1):
               x=segment[index-1].xcor()
               y=segment[index-1].ycor()
               segment[index].goto(x,y)


            if len(segment)>0:
               x=head.xcor()
               y=head.ycor()
               segment[0].goto(x,y)    


            move()

            for segments in segment:
                if segments.distance(head)<20:
                   time.sleep(1)
                   head.goto(0,0)
                   head.direction="stop"

                   for segments in segment:
                        segments.goto(1000,1000)

                   segment.clear()   

                   messagebox.showwarning("oops","Game over")
                   answer=messagebox.askquestion("Game over","Do u want to quit the game")
              
                   if answer=="yes":
                    #wn.exit()
                      sys.exit()
                    #else:
                     #m3()
                   #segments.clear() 
            
                   score=0
                   delay=0.2
                   pen.clear()
                   pen.write("score: {}  High score: {}".format(score,high_score),align="center",font=("courier",20,"normal"))

                   head.direction="up"

            time.sleep(delay)
        wn.mainloop()
        root.quit()
root=Tk()
root.geometry("500x500+200+100")
root.config(background="black")
root.title("Rules")
l1=Label(root,text="Instruction for playing game....",font=("Baloo Bhai",24),bg="black",fg="white")
l1.pack()
l2=Label(root,text="1.press 'w' for go up direction\n2.press 's' for downward direction\n3.press 'a' for left direction\n4.press 'd' for right direction\n5.If the snake touches the boundary \n or it's own body game will over",font=("Baloo Bhai",20),bg="black",fg="white")
l2.pack(pady=10)
l3=Label(root,text="Are you ready to start the game?",font=("Baloo Bhai",20),bg="black",fg="red")
l3.pack()
b1=Button(root,text="YES",font=("Baloo Bhai",14),bg="pink",fg="black",width=12,command=m2)
b1.pack(pady=10)
b2=Button(root,text="NO",font=("Baloo Bhai",14),bg="pink",fg="black",width=12,command=root.destroy)
b2.pack()
root.mainloop()