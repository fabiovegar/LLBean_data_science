#ejemplo de listas

lista=[10,4,90,70]

#para agregar al final

lista.append(88)
lista.extend([4,7,9])

print('El contenido de la lista es',lista)

#ejemplo de tuplas
#crear una tupla de 5 tipos de elementos diferentes

tupla=(1,'ocho',33,'mi caballo',True)
print(tupla)

tupla = tupla + (5,4)
print(tupla)

tupla+= (8,'c')
print(tupla)

#subtupla
#el segundo hasta el ultimo
print(tupla[1:-1])

#subtupla con saltos

print(tupla[::2])

#los elementos impares
print(tupla[1::2])

