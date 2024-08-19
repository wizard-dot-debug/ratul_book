import random
import sys
import turtle

# x = random.random() #prints random number between 0-1
# print(x)

# y = random.randint(1,39) #print random number between given 2 arguments inside the paranthesis.
# print(y)

# turtle.speed(4)
# z = ['red', 'green', 'blue', 'violet']
# turtle.penup()
# for i in range(20):
#     x = random.randint(-200,200)
#     y = random.randint(-200,200)
#     turtle.setposition(x,y)
#     i = random.randint(0,len(z)-1)
#     turtle.dot(z[i])
# turtle.done()

def ranom():
    x = random.randint(1,100)
    life = 0
    while True:
        y = int(input('Number: '))
        life += 1
        if y == x:
            print('Yes.')
        elif y > x:
            print('Incorrect.Try smaller number.')
        else:
            print('Incorrect.Try Larger number.')
        print(f'You Tried {life} times to find the correct number.')

ranom()
