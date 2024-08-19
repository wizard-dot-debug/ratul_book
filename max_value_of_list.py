def zz():
    x = [6,1,3,0,9,3,2,4]
    max = 0
    for i in x:
        if i > max:
            max = i
    print(max)

def divisible_by_5(x):
    sum = 0
    for i in range(x+1):
        if i % 5 == 0:
            sum += i
            print(f'Numbers Divisble By 5 Are: {i}')
    print(f'Total Sum: {sum}')

# x = int(input('Range: '))
# divisible_by_5(x)

# s = 'a quick brown fox jumps over the lazy dog'
# for c in 'abcdefghijklmnopqrstuvwxyz':
#     print(c, s.count(c))


 
 