mayor = 0
residuo = 0

n1 = int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segudo numero"))
if n1 > mayor:
    mayor = n1
elif n2 > mayor:
    mayor = n2
print("el numero mayor es:",mayor)

mayor %= 2

if mayor == 0:
   print('el numero es par')
elif mayor >= 0:
    print('el numero es impar proque el reciduo es:', mayor)
    
inicial = 1
while inicial <= mayor:
    print(inicial)
    inicial += 1
