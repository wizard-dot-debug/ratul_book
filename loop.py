def loop(x):
    sum = 0
    for _ in range(x):
        sum += 1
    return f'Your Total Sum Is {sum}'

x = int(input('Entere your Range: '))
# print(loop(x))

def loop1(x):
    sum = 0
    for i in range(x+1):
        sum += i
    return f'Your Total Sum Is {sum}'

x = int(input('Entere your Range: '))
print(loop1(x))

y = int(input('Number: '))
def multiplyer(y):
    x = 1 
    while x <= 10:
        print(f'{y}*{x} = {y*x}')
        x += 1
    

multiplyer(y)
    
def square():
    x = int(input('Number: '))
    while True:
        if x == 0:
            raise ValueError('Error: We do not accept your fuckhing zero.')
        else:
            return f'Your Given Number Is {x}.The Square Of The Number Is {x**2}'
    

# print(square())

import sys 

def add(x,y):
    sum = x+y
    return sum

def sub(x,y):
    sub = x-y
    return  sub


def add_sub():
    x = float(input('Number1: '))
    y = float(input('Number1: '))
    z = input('1.Addition\n2.Substract:\n').lower()

    if z == 'addition':
        c = add(x,y)
        return f'Addition of these numbers are {c} '
    elif z == 'substract':
        d = sub(x,y)
        return f'Substract of these numbers are {d}'
    elif z != 'addition' and z != 'substract':
        sys.exit('Invalid Selection!.')
    else:
        print('Fuck You.')


# print(add_sub())


def fnc(x):
    y = 'inside my function '
    print(y.title(), x)
    x = 10
    print(y.title(), x)

# x = 20 
# fnc(x)

def my_fnc(x= 10, y=0, z=0):
    return f'x = {x}, y = {y}, z = {z}'

# x = 5
# y = 6
# z = 7
# print(my_fnc(x, y, z))


def fnc2():
    x = list(input('Number: '))
    s = 0
    for i in x:
        s += int(i)
    return f'Total Sum = {s}'


# print(fnc2())

def avg():
    x = list(input('Number: '))
    sum = 0
    for i in x:
        sum += int(i)
    avg = sum/2
    return f'Average Of The Numbers Is: {avg}'

# print(avg())

def mult(x = 1):
    y = 1
    while y <= 10:
        if x == 0:
            raise ValueError('Fuck You!!')
        else:
            print(f'{x}*{y} = {x*y}')
        y += 1

# x = int(input('Numbers: '))
# mult(x)

        
        

 
 