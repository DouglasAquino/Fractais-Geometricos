import turtle

def drawBranch(size, angle, color):
    turtle.fd(size)
    if size > 9:

        turtle.rt(angle/2)
        drawBranch(size*0.8, angle, color)
        turtle.lt(angle)
        turtle.color(color)
        drawBranch(size*0.8, angle, color)
        turtle.rt(angle/2)
        
        if size / 2 < 10 :
            turtle.color('#FFD700')
        else:
            turtle.color('brown')

    turtle.bk(size)

turtle.tracer(8,20)      
turtle.pu()
turtle.left(90)
turtle.color('Gold')
turtle.pensize(3) 
turtle.goto(0,-100)
turtle.pd()         
drawBranch(80, 50, "#FFFF00")
turtle.home()
turtle.exitonclick()



