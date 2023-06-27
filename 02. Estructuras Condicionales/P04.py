#P04: Estado final de cursado de un alumno
import os
os.system('cls')
print("Bienvenido")
asistencia=int(input("ingrese el porcentaje de asistencia del alumno[0-100]: "))
if asistencia>=80:
    primerParcial=float(input("ingrese la nota del primer parcial del alumno: "))
    segundoParcial=float(input("ingrese la nota del segundo parcial del alumno: "))
    examenes=0.3*primerParcial+0.7*segundoParcial
    if (examenes>=7):
        tp=input("presento la carpeta de trabajos practicos?s/n: ")
        if tp=="s":
            print("estado final del alumno: PROMOCION")
            print("promedio: ",examenes)
        else:
            print("no presento los trabajos practicos")
            print("estado final del alumno: REGULAR")
            print("promedio: ",examenes)
    elif (examenes>=5) and (examenes<7):
            print("estado final del alumno: REGULAR")
            print("promedio: ",examenes)
    else:
        print("estado final del alumno: LIBRE")
        print("promedio: ",examenes)
else:
    print("estado final del alumno: LIBRE")        
    print("no cumplio con la asistencia minima obligatoria")