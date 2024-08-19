import turtle
x = int(input('Enter Your Steps: '))
for i in range(x):
    turtle.shape('turtle')
    turtle.speed(1)
    if (i+1) % 2 == 0:
        turtle.forward(200)
        turtle.left(45)
        turtle.exitonclick
    else:
        turtle.forward(200)
        turtle.left(135)
        turtle.exitonclick

