#Informe de cobro
print("Bienvenido")
digito=int(input("Ingrese el ultimo digito del documento: "))
if digito%2==0:
    print('es par')
    print('cobra por cajero')
else:
    print('es impar')
    print('cobra por ventanilla')