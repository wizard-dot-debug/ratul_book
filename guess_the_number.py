import random
import sys
def random_game(computer):
    x = int(input('Guess The Number Between 1 To 100: '))
    if x == computer:
        print('Congrats Fucker!! You Guessed It Motherfucking R8😘😘.\n')
        while True:   
            d = int(input('1.Play Again?\n2.Exit?\n\n'))
            if d == 1:
                co()
            else:
                break
    elif x < computer:
        print('Your Dick Is Too Small.😂')
    elif x > computer:
        print('Your Dick Is Not That Big As You Think😒.')

def co():
    life = 0
    r = random.randint(1,100)
    while True:
        if life < 5:
            random_game(r)
        else:
            print('Fuck You Looser🤣🤣.')
            break
        life += 1

def continiue():
    print('Welcome To the Guess The Fucking Word Game.\nThis Is An One Hell Of A Annoying Game You Will Be Ever playing.\nNow Best Of Luck Mother Fucker👌👌.')
    y = input('Write Start/Exit To Start/Exit The Game: ').lower()
    if y == 'start':
        co()
        while True:   
            x = int(input('1.Play Again?\n2.Exit?\n'))
            if x == 1:
                co()
            else:
                print('You Are In Luck Today.')
                break
    else:
        print('You Are In Luck Today.')
    

continiue()




    

