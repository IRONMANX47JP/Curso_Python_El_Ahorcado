# Recordar que es índice 0
lista=[1, 5, "casa", 3.3, True]
print("Lista:", lista)
print("Elemento de la lista:", lista[2])
# slice como con las cadenas
print("Slice del 1 (incluido) al 3 (no incluido): ", lista[1:3])
print("Hasta el elemento 4 no incluido: ",lista[:4])
print("Desde el 3 (inc)", lista[3:])
print("El 2do elem de la derecha: ", lista[-2])
print("Desde el 0 hasta el final, de 2 en 2!:", lista[0::2])
cadena="Hola mundo ustedes como estan"
print(cadena[::2])