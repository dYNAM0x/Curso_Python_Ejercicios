#Conjuntos
'''
Son otro tipo de colecciones solo que en estas los elementos son unicos y se agregan de manera aleatoria



si tenemos mismos elementos dentro de los conjuntos la máquina interpretará que se trata
de un solo elemento, ya que no puede haber repeticiones
'''
conjunto = set()
conjunto={1,2,3,4,5,"bobashas","gaspar nicolas", 2,3}
print(conjunto)

'''
poemos agregar elementos a un conjunto solo que aparecerá de manera aleatoria'''
conjunto.add("holaaaaaa")
print(conjunto)

'''
también podemos quitar elementos del conjunto 
'''
conjunto.remove(1)
print(conjunto)


