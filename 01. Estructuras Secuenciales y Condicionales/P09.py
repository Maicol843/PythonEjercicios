#F es negativo o E es no negativo pero no ambos a la vez
F=int(input("Ingrese E= "))
E=int(input("Ingrese F= "))
p=(F<0)
q=not(E<0)
resultado=p and q
print(resultado)