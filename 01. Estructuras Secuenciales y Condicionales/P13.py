#Calculo de las raíces de una ecuación de segundo grado
import math 
print('ingrese los valores de ecuacion cuadratica')
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
if a!=0:
    d=b**2-4*a*c
    if d>=0:
        e=math.sqrt(d)
        x1=(-b+e)/(2*a)
        x2=(-b-e)/(2*a)
        if x1==x2:
            print('raiz unica')
            print('x=', x1)
        else:
            print('las raices reales son: ')
            print('x1= ',x1)
            print('x2= ',x2)
    else:
        e=(-d)
        y1=(-b)/(2*a)
        x1=e/(2*a)
        x2=(-e)/(2*a)
        print('las raices imaginarias son: ')
        print('x1= ',y1,'+',x1,'i')
        print('x2= ',y1,x2,'i')
else:
    print('no es una ecuacion de segundo grado')