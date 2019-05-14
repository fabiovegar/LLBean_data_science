size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)
sizelist=len(lista)
delete=input('la palabra a eliminar es:')
for i in lista:
    for j in lista:
        if i==delete:
            lista.remove(delete)
print('la nueva lista es:', lista)