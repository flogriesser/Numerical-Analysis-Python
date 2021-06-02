import numpy as np


def Regula_falsi(f, a, b, n):
    list = [a,b]
    while b-a != 0 and n-2:
        denominator = f(b) - f(a)
        if(denominator == 0):
            break
        m = a - (b-a)/(denominator)*f(a)
        
        if f(m) == 0: break
        if(f(m)*f(a) <= 0 ):b = m
        if(f(b)*f(m) <= 0): a = m
            
        list.append(m) 
        n -= 1
    return list