#Ejercicio 4
'''
calcular area y perimetro de circunferencia

'''
import math
r = float(input("Digite la longitud del radio de al circunferencia: "))

area= math.pi * (r**2)
longitud = 2 * math.pi * r

print(f"El area es: {area}")
print(f"La longitud de la circunferencia es: {longitud}")