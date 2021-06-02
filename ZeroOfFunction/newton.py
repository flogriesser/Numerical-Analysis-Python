def Newton(f, df, a, delta, n):
    list = [a]
    #while n != 0 and delta <= abs(f(a)):
    while n-1:
        if(df(a) == 0): break
        x = a -(f(a)/df(a))
        list.append(x)
        if abs(a - x) <= abs(delta): break
        a = x            
        n -= 1
    return list