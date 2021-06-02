import numpy as np

def Sekantenverfahren(f, a, b, delta, n):
    list = [a,b]
    #while n != 0 and delta <= abs((b-a)):
    while n-2:
        denominator = f(b) - f(a)
        if(denominator == 0):
            break
        m = b-(b-a)/denominator*f(b)
        a=b
        b=m
        list.append(m)
        n -= 1
    return list