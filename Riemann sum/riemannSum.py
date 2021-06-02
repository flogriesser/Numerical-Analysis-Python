import math
import numpy as np

def R(f, a, b):
    return f((a + b)/2)*(b-a)

def T(f, a, b):
    return ((f(a)+f(b))/2)*(b-a)


def Rh(f, a, b, n):
    h = (b-a)/n
    summe = RSum(f, a, n, h)
    return h*summe


def Th(f, a, b, n):
    h = (b-a)/n
    summe = TSum(f, a, n, h)
    return h*((f(a)+f(b))/2 + summe)

def S(f, a, b):
    return (b-a)*(f(a) + 4*f((a+b)/2) + f(b))/6

def Sh(f, a, b, n):
    h = (b-a)/n
    return h*(f(a) + f(b) +2*TSum(f, a, n, h) + 4*RSum(f, a, n, h))/6


def RSum(f, a, n , h):
    summe = 0
    for i in range(0, n-1):
        summe = summe + f(a + i*h + h/2)
    return summe

def TSum(f, a, n, h):
    summe = 0
    for i in range(1, n-1):
        summe += f(a + i*h)
    return summe

def phi(x):
    return math.exp((-x**2)/2)/(math.sqrt(2*math.pi))
