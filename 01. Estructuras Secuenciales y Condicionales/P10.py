#Calculo del valor de F
print("Bienvenido")
print("Ingrese cuatro numeros")
A=int(input("Ingrese A= "))
B=int(input("Ingrese B= "))
C=int(input("Ingrese C= "))
D=int(input("Ingrese D= "))
p=A+10
q=C-B*D
if q!=0:
    F=6*(p/q)
    print("F= ",F)
else:
    print("no es posible calcular el valor de F")