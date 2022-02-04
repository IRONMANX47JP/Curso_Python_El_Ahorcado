l1=[1,2,3,4,5]
#es mutable
l1[0]=42
print("Lista mutada: ", l1)
suma=l1+l1
print("Suma: ", suma)
mult=l1*4
print("Mult:", mult)
l1.append(24) #añadir al final un elemento
print("Lista extendida:", l1)
print("Largo de lista", len(l1))
# Agregar elemento en el medio
l1.insert(3, 500)
print("Le agregamos un elemento en el medio: ", l1)
# Modificamos un slice
l1[2:4]=[100, 200]
print("Modif de slice: ", l1)