#P02-version 4: Mayor de tres números
print("Ingrese tres numeros")
A=int(input("Ingrese A= "))
B=int(input("Ingrese B= "))
C=int(input("Ingrese C= "))
if (A>B) and (A>C):
    print("A es mayor que B y C")
else:
    if (B>A) and (B>C):
        print("B es mayor que A y C")
    else:
        if (C>A) and (C>B):
            print ("C es mayor que A y B") 