import sys
def positive_negetaive(x):
    if x >= 0:
        print(f'Your given number is {x}. Which is positive.')
    else:
        print(f'Your given number is {x}. Which is negative.')


def even_odd(x):
    if x % 2 == 0:
        print(f'Your given number is {x}. This number is even.')
    else:
        print(f'Your given number is {x}. This number is odd.')


def lipyear(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print(f'Your Given Year Is {x}.This Year Is Lip Year.')
            else:
                print(f'Your Given Year Is {x}.This Year Is not Lip Year.')
        else:
            print(f'Your Given Year Is {x}.This Year Is Lip Year.')
    else:
        print(f'Your Given Year Is {x}.This Year Is Lip Year.')



def choose():
    print('Welcome!!.')
    print('Choose From The Below Option.\n1.Find positive Or Negative?\n2.Want To Know The Number Type?\n3.Find lipyear.')
    x = int(input(''))
    if x != 1 and x != 2 and x != 3:
      sys.exit('Error:  You Must Choose From The Above Options.')  
    if x == 1:
        print('Welcome To The Program.\n')
        y = int(input('Enter your Number: '))
        positive_negetaive(y)
    elif x ==2:
        print('Welcome To The Program.\n')
        y = int(input('Enter your Number: '))
        even_odd(y)
    elif x == 3:
        print('Welcome To The Program.\n')
        y = int(input('Enter your Year: '))
        lipyear(y)

# choose()

import math

# m = math.sqrt(105)
# n = int(m) 
# print(n)

def prime4(x = 1013):
    # x = int(input('Enter Your Number: '))
    if x == 0:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    
    m = math.sqrt(x)
    n = int(m) + 1
    for i in range(3,n,2):
        if x % i == 0:
            return False
    return True
            
def prime3(x = 1013):
    # x = int(input('Enter Your Number: '))
    if x == 0:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
       return False

    prime = True
    for i in range(3,x,2):
        if x % i == 0:
            prime = False
            return prime
    return prime
    
import timeit
t1 = timeit.timeit(prime3)
t2 = timeit.timeit(prime4)
print(t1, t2, t1/t2)



