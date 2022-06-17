#Ejercicio 1

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))


if((num1 <= 0)  and (num2 <= 0)):
    print("son valores incorrectos: ERROR 404 NOT FOUND %=&)(/)$=$")
elif (num1 % 2 == 0 and num2 % 2 == 0):
    print("ambos numeros son pares")
elif(num1 % 2 ==0):
    print("el primer numero es par")
elif(num2 % 2 == 0):
    print("el segundo numero es par")
else: print("ninguno es par")