#Calculo del importe a pagar
precioProducto=float(input("Ingrese el precio de un producto: "))
unidades=int(input("Ingrese el numero de unidades a comprar: "))
if unidades >= 5:
    total=precioProducto*unidades-precioProducto*0.10
else:
    total=precioProducto*unidades
print("Importe total a pagar: ", total)