def prime():
    x = int(input('Enter Your Number: '))
    prime = True
    for i in range(2,x):
        if x == 0:
            prime = False
            break
        elif x == 2 or x == 1:
            prime = True
            break
        elif x % i == 0:
            prime = False
            break
        else:
            prime = True
            continue
    
    if prime == True:
        print(f'Your Given Number Is {x} Which Is A Prime Number.')
    else:
        print(f'Your Given Number Is {x} Which Is Not A Prime Number.')

# prime()

def prime2():
    x = int(input('Enter Your Number: '))
    prime = True
    if x == 0:
        prime = False
    elif x == 2:
        prime = True
    elif x % 2 == 0:
        prime = False

    for i in range(3,x,2):
        if x % i == 0:
            prime = False
            break
    

    if prime == True:
        print(f'Your Given Number Is {x} Which Is A Prime Number.')
    else:
        print(f'Your Given Number Is {x} Which Is Not A Prime Number.')

# prime2()

def prime3():
    x = int(input('Enter Your Number: '))
    prime = True
    if x == 0:
        prime = False
    elif x == 2:
        prime = True
    elif x % 2 == 0:
        prime = False

    mid = (x // 2) + 1
    for i in range(3,mid,2):
        if x % i == 0:
            prime = False
            break
    

    if prime == True:
        print(f'Your Given Number Is {x} Which Is A Prime Number.')
    else:
        print(f'Your Given Number Is {x} Which Is Not A Prime Number.')

# prime3()

import math
def prime4():
    x = int(input('Enter Your Number: '))
    prime = True
    if x == 0:
        prime = False
    elif x == 2:
        prime = True
    elif x % 2 == 0:
        prime = False
    
    m = math.sqrt(x)
    n = int(m) + 1
    for i in range(3,n,2):
        if x % i == 0:
            prime = False
            break
        else:
            prime = True
    
    if prime == True:
        print(f'Your Given Number Is {x} Which Is A Prime Number.')
    else:
        print(f'Your Given Number Is {x} Which Is Not A Prime Number.')
    
# prime4()
import math
def prime5():
    x = int(input('Small Number: '))
    y = int(input('Large Number: '))
    n = y + 1
    primes = []
    p = ''
    for i in range(x,n,1):
        prime = True
        if i < 2:
            continue
        elif i == 2:
            prime = True
        elif i % 2 == 0:
            prime = False
        m = math.sqrt(i)
        n = int(m) + 1
        for j in range(3,n,2):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            primes.append(str(i))
        else:
            continue
    print(','.join(primes))

prime5()

def prime6():
    x = int(input('Small Number: '))
    y = int(input('Large Number: '))
    primes = []
    for i in range(x, y + 1):
        if i < 2:
            continue
        prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(str(i))
    print(', '.join(primes))

# prime6()