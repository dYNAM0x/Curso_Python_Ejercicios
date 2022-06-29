#listas
'''
también conocidos como vectores, sirven para guardar datos de forma indexada
'''
lista = [ "lunes", "mártes","miércoles","jueves","viernes","sábado","domingo", 40, 5.8]
print(lista)

'''
tambien se pueden presentar los datos de forma que mostrará el primer o ultimo valor y podemos indicar que mustre los demas
'''
lista = [ "lunes", "mártes","miércoles","jueves","viernes","sábado","domingo", 40, 5.8]
print(lista[:5])
#llega hasta el dia viernes, ya que considera solo los valores que pide

lista = [ "lunes", "mártes","miércoles","jueves","viernes","sábado","domingo", 40, 5.8]
print(lista[3:])
#llega hasta el dia viernes, ya que considera solo los valores que pide

'''
tambien podemos seleccionar desde cierto punto de la indexación solo que MOSTRARÁ UN VALOR MENOS AL INDEXADO
'''
lista = [ "lunes", "mártes","miércoles","jueves","viernes","sábado","domingo", 40, 5.8]

print(lista[2:5])
'''
como aqui se ve parte del indice 2 pero solo mostrara hasta el indice cuatro ya que muestra un valor menos al indicado
'''


'''los resultados de los 3 casos serán los siguientes

['lunes', 'mártes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo', 40, 5.8]
['lunes', 'mártes', 'miércoles', 'jueves', 'viernes']
['jueves', 'viernes', 'sábado', 'domingo', 40, 5.8]
['miércoles', 'jueves', 'viernes']

'''