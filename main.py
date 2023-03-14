mayor = 0
residuo = 0
n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segudo numero"))
if n1 > mayor:
    mayor = n1
elif n2 > mayor:
    mayor = n2
print("el numero mayor es:",mayor)