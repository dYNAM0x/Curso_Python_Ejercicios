#ejercicio 4 calculadora

print("ESTO ES UNA CLACULADORA SELECCIONE QUE QUIERE REALIZAR:  "
      "\n\n S,s - Suma "
      "\n R,r - Resta "
      "\n M,m - Multiplicación"
      "\n D,d - División")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
opc = input("Eliga opción: ")


if (opc == 'S' or opc == 's'):
    suma = num1 + num2
    print(f"La suma es: {suma:.2f}")
elif (opc == 'R' or opc == 'r'):
    resta = num1 - num2
    print(f"La resta es: {resta:.2f}")
elif (opc == 'M' or opc == 'm'):
    multpl = num1 * num2
    print(f"La multiplicación es: {multpl:.2f}")
elif (opc == 'D' or opc == 'd'):
    divis = num1 / num2
    print(f"La division es: {divis:.2f}")
else:
    print("no es una opción valida")