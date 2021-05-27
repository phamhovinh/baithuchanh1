import turtle,random
colors =["red","green","blue","onrange","purple","pink","yelow"]
painter= turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color=random.choice(colors)
    painter.pencolor(color)
    painter.cricle(100)
    painter.right(30)
    painter.Left(60)
    painter.setposition(0,0)
