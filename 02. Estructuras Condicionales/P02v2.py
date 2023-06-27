#P02-version 2: Mayor de tres números
print("Ingrese tres numeros")
A=int(input("Ingrese A= "))
B=int(input("Ingrese B= "))
C=int(input("Ingrese C= "))
if (A>B) and (A>C):
    print("A es mayor que B y C")
elif (B>A) and (B>C):
    print("B es mayor que A y C")
else:
    print ("C es mayor que A y B") 