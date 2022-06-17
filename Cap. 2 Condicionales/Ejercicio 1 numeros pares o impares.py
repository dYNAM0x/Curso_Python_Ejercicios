#Ejercicio 1

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))


if((num1 == 0)  and (num2 == 0)):
    print("son valores incorrectos: ERROR 404 NOT FOUND %=&)(/)$=$")
elif (num1 % 2 == 0 and num2 % 2 == 0):
    print("ambos numeros son pares")
elif(num1 % 2 ==0 and num2 % 2 != 0):
    print(f"el par es {num1}")
elif (num1 % 2 != 0 and num2 % 2 == 0):
    print(f"el par es {num2}")
else: print("ninguno es par")