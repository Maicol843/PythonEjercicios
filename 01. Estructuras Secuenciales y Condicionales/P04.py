#Expresiones lógicas
A=int(input("ingrese A= "))
B=int(input("ingrese B= "))
p=(A>-11)
q=(B>-A)
r=True
s=False
t=(r or s)
u=(not q or  t)
v=not(u)
resultado= not p or (v and r)
print(resultado) 