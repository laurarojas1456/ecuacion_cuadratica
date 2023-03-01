# Programa para calcular una ecuacion cuadratica

import math 


print("----------------------------------------")
print("------ RESOLVER LA ECUACION CUADRATICA--")
print("----------------------------------------")

# input

a = int(input("Digite el valor de a: "))
b = int(input("Digite el valor de b: "))
c = int(input("Digite el valor de c: "))

# processing

d = b**2-4*a*c
if d == 0:
    *1 = (d/2*a)
    *2 = 1
    
    print(*1, *2)
if d > 0:
    *1 =(-b+math.sqrt(d))/(2*a)
    *2 =(-b-math.sqrt(d))/(2*a)
    print(*1, *2)
else:
    print("la solución es imaginaria")
