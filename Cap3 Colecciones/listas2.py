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

lista9 = [1,2,3,4,5, "Alajandro","Lima","Percino"]

print(10 in lista9)