#lista
lista = ["lunes", "mártes","miércoles","jueves","viernes","sábado","domingo", 40, 5.8,[1,2,3]]
'''
puedes también con una función cuantos datos tienes guardados como la función "len"
'''
print(len(lista))


'''
con la funcion .append, solo que la agregará al final
'''
lista2 = [1,2,3,4,5]
lista2.append(6)
print(lista2)

'''
también puedes ingresar datos en un lugar específico con la funcion .insert
tomando 2 parametros primero se ingresando el lugar del indexado y luego el valor que le asignaremos
teniendo en cuenta que se recorrerá al siguiente indexado el dato que le sigue
'''
lista3 = [1,2,4,5]
lista3.insert(2,3)
print(lista3)


'''
si quieres agregar varios valores al final a la lista con la función .extend
'''

lista4 = [1,2,3,4,5]
lista4.extend([6,7,8])
print(lista4)

'''
podemos concatenar listas 
'''
lista5 = [1,2,3]
lista6 = [4,5,6]
lista7 = ["Alejandro", "Lima", "Percino"]
lista8 = lista5 + lista6 + lista7
print(lista8)

'''
podemos sabr si un dato si está en la lista con "in"
'''

lista9 = [1,2,3,4,5, "Alejandro","Lima","Percino"]

print("Alejandro" in lista9)



'''
también existe otra función de las listas la cual es .index, lo que hace retomar o buscar el elemento y mostrar su
posición en el indexado
'''

lista10 = [1,2,3,4,5,6, "Alejandro","Nube",45,67,100]
print(lista10.index(5))

'''
la función .count nos sirve para determinar cuantas veces se encuentra un elemento en la lista
'''

lista11 = [1,2,3,4,5,"Alejandro","Pedro", "Alejandro",2,3,4,"Alejandro","Pedro",1,2,3]
print(lista11.count("Alejandro"))


'''
la fucnión .pop solamente eliminará pero un valor en una posición de la lista 
en cambio la función .remove elimanrá el elemento dado de la lista partiendo desde el final del indexado
'''
lista12 = [1,2,3,4,5]
lista12.pop(3)
print(lista12)

lista13=[1,2,3,4,5,5,5,5,6,7,8]
lista13.remove(5)
print(lista13)

'''
podemos limpiar toda nuestra lista con .clear
'''

lista14=[1,2,3,4,5]
lista14.clear()
print(lista14)


'''
podemos voltear las listas con .reverse
'''

lista15=[1,2,3,4,5,"Holaa chat"]
lista15.reverse()
print(lista15)


'''
con la función .sort podemos ordenar las listas, podemos agregar parametros a la función como por ejemplo que invierta el orden de la lista
'''
lista16=[0,-3,-9,90,18,105,9]
lista16.sort()
print(lista16)

lista16.sort(reverse=True)
print(lista16)
