import math


def quadratic(a, b, c):
    p1 = b*b-4*a*c
    if p1 >= 0:
        x1 = (-b+math.sqrt(p1))/(2*a)
        x2 = (-b-math.sqrt(p1))/(2*a)
        print('The answer to the equation: a*x^2 + b*x + c = 0 is: \n' +
              'x1 =', x1, '\n' +
              'x2 =', x2, '\n')
        return(x1, x2)
    else:
        print('No answers to the equation.')
