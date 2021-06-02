import numpy as np


def Bisection(f, a, b, n):
    liste = [a,b]    
    if a>b:
        a,b = b,a 
    
    if f(a)*f(b) >= 0:
        return None

    while n-2:
        print(n, a, b)
        m = (a+b)/2
        liste.append(m) 
        if f(m) == 0: break
        if(f(m)*f(a) <= 0 ):b = m
        if(f(b)*f(m) <= 0): a = m
        
        n -= 1
    return liste