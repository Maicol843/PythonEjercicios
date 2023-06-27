#P01-Version 1: Numero entre 1 y 3
numero=int(input("Ingrese un numero entre 1 y 3: "))
if numero == 1:
    print("Uno")
if numero==2:
    print("Dos")
if numero==3:
    print("Tres")
if (numero<=0)or(numero>3):
    print("No es 1, 2 ni 3")
