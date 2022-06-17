#ejercicio 2

num1 = int(input("No.1: "))
num2 = int(input("No.2: "))
num3 = int(input("No.3: "))

if (num2 and num3 < num1 ):
    print(f"el mayor es {num1}")
elif (num1 and num3 < num2 ):
    print(f"el mayor es {num2}")
elif (num1 and num2 < num3 ):
    print(f"el mayor es {num3}")
else:
    print("no son numeros validos")