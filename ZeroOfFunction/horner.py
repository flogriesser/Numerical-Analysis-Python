def Hornerschema(a, x0):
    faktor = 0
    list = []
    for i in range(len(a)):
        list.append(a[i] + faktor)
        faktor = x0 * list[i]
    return list