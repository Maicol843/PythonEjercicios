#P01-version 2: Numero entre 1 y 3
import os
os.system('cls')
numero=int(input("Ingrese un numero entre 1 y 3: "))
if (numero>=1) and (numero<=3):
    if numero==1:
        print("Uno")
    elif numero==2:
        print("Dos")
    else:
        print("Tres")        
else:
    print("No es 1, 2 ni 3")