def Imtihon_3():
    a = [5, 2, 7, 1, 3, 4, 6, 9, 10]
    b = []
    e = sorted(a)
    for x in range(1, 11):
        if x not in a:
            b.append(x)
            print(x)
print(Imtihon_3())