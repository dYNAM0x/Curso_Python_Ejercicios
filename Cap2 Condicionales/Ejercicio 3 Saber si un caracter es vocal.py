#ejercicio 3

letra = input("digite un caracter: ").lower()#.lower es un método para transformar en minuscula

if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print(f"la letra: {letra} es una vocal")
else:
    print("no es un vocal")
