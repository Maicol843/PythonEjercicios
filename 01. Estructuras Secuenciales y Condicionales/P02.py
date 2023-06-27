#Calculo del valor de Y
print("ingrese los valores de A,B y C")
A=float(input("Ingrese A= "))
B=float(input("Ingrese B= "))
C=float(input("Ingrese C= "))

if (B-C)!=0:
    Y=A/(B-C)
    print("Y= ",Y)
else:
    print("no es posible calcular el valor de Y")