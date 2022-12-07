import math

co=str(input('escriba los valores de a b y c, cada uno ceparados por un espacio: '))
abc=co.split(' ')
a=float(abc[0])
b=float(abc[1])
c=float(abc[2])

re= b**2 - 4 * a * c
if re < 0:
    print('no hay ninguana raiz')
else:
    redre = math.sqrt(re)
    if redre == 0:
        print('tiene una raiz', -b/(2*a))
    else:
        r1=(-b-redre)/ (2*a)
        r2=(-b+redre)/ (2*a)

        print ('tiene dos raices', r1, r2)
