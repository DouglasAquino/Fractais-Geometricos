import turtle

def drawSpiral(t, length, color):
    if length != 0:
        
        newcolor = (int(color[1:],16) + 2**20)%(2**24)
        newcolor = hex(newcolor)[2:]
        newcolor = "#"+("0"*(6-len(newcolor)))+newcolor
        
        t.color(newcolor)
        t.forward(length)
        t.left(90)

        drawSpiral(t, length -1 , newcolor)
        t.home()

def main():
    t = turtle.Turtle()
    t.shape("blank")
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(0,0)
    t.pendown()
    
    drawSpiral(t, 200, "#800000")
    t.left(30)
    drawSpiral(t, 200, "#FF4500")
    t.left(90)
    drawSpiral(t, 200, "#FF4500")
    t.left(270)
    drawSpiral(t, 200, "#800000")

    
    screen.exitonclick()

main()
