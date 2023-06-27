#Ordenar en forma creciente
print("Ingrese tres números")
A = int(input("Ingrese el valor de A = "))
B = int(input("Ingrese el valor de B = "))
C = int(input("Ingrese el valor de C = "))
if (A > B) and (B > C):
    print(C,B,A)
elif (B > A) and (A > C):
    print(C,A,B)
elif (C > A) and (A > B):
    print(B,A,C)
elif (A > C) and (C > B):
    print(B,C,A)
elif (B > C) and (C > A):
    print(A,C,B)
elif (C > B) and (B > A):
    print(A,B,C)
else:
    print("No es posible ordenar ya que son iguales")