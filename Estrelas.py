import turtle

def drawSpiral(t, length, color):
    if length != 0:

        newcolor = (int(color[1:],16) + 2**20)%(2**24)
        newcolor = hex(newcolor)[2:]
        newcolor = "#"+("0"*(6-len(newcolor)))+newcolor
        
        t.color(newcolor)
        t.forward(length)
        t.left(200)
        drawSpiral(t, length - 1, newcolor)

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(-100,0)
    t.pendown()
    drawSpiral(t, 200, "#A52A2A")
    drawSpiral(t, 300, "#A52A2A")
    screen.exitonclick()

main()
