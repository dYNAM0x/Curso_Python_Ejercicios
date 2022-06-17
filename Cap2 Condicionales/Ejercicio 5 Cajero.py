#ejercicio 5 cajero
saldo=1000
opc = int(input("Su saldo inicial es de $1000 que desea hacer: "
      "\n 1 - Ingresar dinero "
      "\n 2 - Retirar dinero "
      "\n 3 - Mostrar dinero disponible"
      "\n 4 - Salir"
                "\n Seleccione opción: "))

if(opc == 1):
    ing=int(input("ingrese el dinero que depositará a su cuenta: "))
    ing+=saldo
    print(f"Se ha ingresado el deposito, su saldo es de {ing}")
elif(opc == 2):
    ret=int(input("ingrese el dinero que retirará de su cuenta: "))
    reT = saldo - ret
    print(f"Se ha retirado {ret}, su saldo es de {reT}")
    if(ret>saldo):
        print("no se puede retirar esa cantidad, no tiene saldo suficiente")
elif(opc == 3):
    print(f"su saldo es: {saldo}")
elif(opc == 4):
    print("gracias vuelva pronto")
else:
    print("opcion invalida")
