import turtle

def drawSpiral(t, length, color):
    if length < 100:
        
        newcolor = (int(color[1:],16) + 2**20)%(2**24)
        newcolor = hex(newcolor)[2:]
        newcolor = "#"+("0"*(6-len(newcolor)))+newcolor
        
        t.color(newcolor)
        t.forward(length)
        t.left(10)

        drawSpiral(t, length + 0.09, newcolor)

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(400)
    t.penup()
    t.pensize(3)
    t.goto(0,0)
    t.pendown()
    drawSpiral(t, 0, "#959CD")
    screen.exitonclick()

main()
