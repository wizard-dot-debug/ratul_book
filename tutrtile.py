import turtle
# #For Square
# # turtle.shape('turtle')
# # turtle.speed(2)
# # turtle.forward(200)
# # turtle.left(90)
# # turtle.forward(200)
# # turtle.left(90)
# # turtle.forward(200)
# # turtle.left(90)
# # turtle.forward(200)
# # turtle.exitonclick
# #For rambash
# turtle.shape('turtle')
# turtle.speed(2)
# turtle.forward(200)
# turtle.left(45)
# turtle.forward(200)
# turtle.left(135)
# turtle.forward(200)
# turtle.left(45)
# turtle.forward(200)
# turtle.exitonclick
# #Somobaho Trivuj
# turtle.shape('turtle')
# turtle.speed(2)
# turtle.forward(215)
# turtle.left(130)
# turtle.forward(170)
# turtle.left(100)
# turtle.forward(170)
# turtle.exitonclick
# for i in range(50,100,10):
#     for j in range(4):
#         turtle.forward(i)
#         turtle.left(90)
# turtle.exitonclick


# turtle.color('blue')

# x = 0
# while x < 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     x += 1
# turtle.exitonclick   
# x = 7
# y = 4
# turtle.penup()
# for i in range(x):
#     for j in range(y):
#         turtle.dot()
#         turtle.forward(20)
#     turtle.backward(20*y)
#     turtle.right(90)
#     turtle.forward(20)
#     turtle.left(90)
# turtle.exitonclick 

# def squar(x):
#     for _ in range(4):
#         turtle.color('red')
#         turtle.forward(x)
#         turtle.left(90)


# def xyz():
#     x = 0
#     while x < 90:
#         squar(100)
#         turtle.left(4)
#         turtle.color('green')
#         x += 1
#     turtle.exitonclick


# # xyz()


# def st():
#     x = float(input('Length: '))
#     for _ in range(3):
#         turtle.forward(x)
#         turtle.left(120)
#     turtle.exitonclick

# st()
# def turtle():
# x = turtle.textinput('x', 'What is your name?\n').lower()
# if x.startswith('mr'):
#     print('Hello Sir, how aare you?')
# elif x.startswith('mrs') or x.startswith('miss') or x.startswith('ms'):
#     print('Hello Mam, how are you?')
# else:
#     print(f'Hi {x}! How are you?')
# turtle.exitonclick()

# print(turtle())

# turtle.color('red','green')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.position())< 1:
#         break
# # turtle.end_fill()
# # turtle.done()

# turtle.begin_fill()
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)
# turtle.left(120)
# # turtle.forward(200)
# turtle.end_fill()


# def fib():
#     x = int(input('Number: '))
#     fib_x = 1 
#     fib_next = 1
#     if x <= 2:
#         fib_n = 1
#     else:
#         i = 3 
#         while i <= x:
#             i +=1
#             fib_temp = fib_x + fib_next
#             fib_x = fib_next
#             fib_next = fib_temp
#         fib_n = fib_next
#     return fib_n

# print(fib())
    
def fib():
    x = int(input('Number: '))
    f1 = 1
    f2 = 1
    fib = 0
    if x <= 2:
        fib = f1
    else:
        i = 3
        while i <= x:
            i += 1
            fib = f1 + f2
            f2 = fib
            f1 = f2
        fib = f2
    return fib

print(fib())

        