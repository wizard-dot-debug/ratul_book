# x = ' this i s a string. '
# # x.lstrip()
# # x.rstrip()
# y = x.strip()
# print(y)

def istr():
    x = str(input('Enter your string: '))
    capital = ''
    small = ''
    num = ''
    sp = ''
    for i in x:
        if i.isupper():
            capital += i
        elif i.islower():
            small += i
        elif i.isnumeric():
            num += i
        else:
            sp += i
    print(f'capital Letters: {capital},\nSmall Letters: {small},\nNumeric Letters: {num},\nSpecial Characters: {sp}.')

# istr()

def palindrome():
    x = input('Your Word: ')
    y = list(x.lower())
    check = []
    for i in y[::-1]:
        check += i
    if check == y:
        print(f'Your Given Word Is {x} Which Is A Palindrome.')
    else:
        print(f'Your Given Word Is {x} Which Is Not A Palindrome.')

# palindrome()

def reverse():
    x = input('Enter Your Word: ')
    y = list(x)
    even = []
    odd = []
    i = 0
    reversed = ''
    for j in range(len(x)):
        if (j+1) % 2 == 0:
            odd += y[i]
        else:
            even += y[i]
        i += 1
    # print(f'Even = {even}, Odd = {odd}.')
    for k in range(len(x)):
        
        if (k+1) % 2 == 0:
            r = 0
            reversed += even[r]
            even.remove(even[r])
            r += 1
        else:
            r = 0
            reversed += odd[r]
            odd.remove(odd[r])
            r += 1
    print(reversed)

# reverse()
def reverse_list():
    x = input('Enter Your Word: ')
    y = list(x)
    even = []
    odd = []
    i = 0
    reversed = []
    for j in range(len(x)):
        if (j+1) % 2 == 0:
            odd += y[i]
        else:
            even += y[i]
        i += 1
    # print(f'Even = {even}, Odd = {odd}.')
    for k in range(len(x)):
        
        if (k+1) % 2 == 0:
            r = 0
            reversed.append(even[r])
            even.remove(even[r])
            r += 1
        else:
            r = 0
            reversed.append(odd[r])
            odd.remove(odd[r])
            r += 1
    print(''.join(reversed))

# reverse_list()

#successfully did the project 😪😪.. It took me 3 Hours straight. I think i am dumb.😒😒


#List And it's Comprehension

def square_list():
    x = input('Enter: ')
    y = list(x)
    z = []
    for i in y:
        z.append(int(i)**2)
    print(f'Squared List: {z}')

# square_list()

def sqaure_com():
    x = list(input('Enter: '))
    y = [int(i) ** 2 for i in x]
    print(f'Squared List: {y}')

# sqaure_com() 

#set

def set():
    a = {1,2,3,4,5}
    b = {2,4, 6, 8}

    c = a&b #Intersection
    d = a|b #Union
    e = a^b #prints which are not in common in both set
    f = a-b #prints which are not in b set
    g = b-a #prints which are not in a set

    print(c,d,e,f,g)

# set()

x = {'Ratul':75,'Ratul':80,'Monira':90} #same key twice so the dict overwrite the lowest value and erase it.
print(x)





 
               

