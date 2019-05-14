agenda_hosp=[]
persona = ('Juan', 'Mora', 100103111,65 , 81118811, 'dolor')
agenda_hosp.append(persona)
persona= ('Ana', 'Jimenez', 32415116,50 , 46261266, 'consulta')
agenda_hosp.append(persona)
persona= [('Sofia',   'Alfaro',   32415116,   36 , 51161161, 'consulta'),
          ('Carlos',  'Sanchez',  33411151,   15 , 41655161, 'dolor'),
          ('Felipe',  'Perez',    12243151,   42 , 65151111, 'documento'),
          ('Melissa', 'Alvarado', 734114144,  10 , 87421312, 'dolor'),
          ('Pedro',   'Castro',   4372124141, 2 ,  99313131, 'dolor')]
agenda_hosp.extend(persona)


#Primera pregunta Cuantos pacientes llegaron en total?
print('#1.Llegaron %i pacientes!'%(len(agenda_hosp)))

#Segunda pregunta Cuantas personas llegaron por dolor?
cant=0
for i in range (len(agenda_hosp)):
    for j in range (len(agenda_hosp[i])):
        if(agenda_hosp[i][j]=='dolor'):
            cant+=1
print('#2.Llegaron %i pacientes con dolor.'%cant)


#Tercera pregunta Suponga que se atienden con orden de prioridad por edad, empezando por el adulto mayor.
#Ordene la lista desde el más adulto al más joven
lista1= sorted(agenda_hosp, key=lambda i:i[3],reverse=True)
print ('#3.',lista1)


#Cuarta Pregunta
#Cuantos pacientes son mayores de edad? cuantos menores?

mayores=0
menores=0
for i in range (len(agenda_hosp)):
    if agenda_hosp[i][3]>=18:
        mayores+=1
    else:
        menores+=1

print('#4.Hay %i pacientes mayores de edad y %i menores de edad'%(mayores,menores))



#Quinta Pregunta
#Suponga que se atienden con orden de prioridad por gravedad de consulta, empezando por los que tienen dolor
#y luego por edad (mas viejo al joven), empezando por el adulto mayor. Ordene la lista empenzando por los que tienen mayor prioridad.

lista2=[]
lista3=[]
for i in range (len(agenda_hosp)):
    if agenda_hosp[i][5]=='dolor':
        lista2.append(agenda_hosp[i])
    else:
        lista3.append(agenda_hosp[i])
lista_dolor=sorted(lista2, key=lambda x:x[3],reverse=True)
lista_otros=sorted(lista3, key=lambda x:x[3],reverse=True)
lista_final=lista_dolor+lista_otros
print('#5.',lista_final)



#Sexta pregunta
#Suponga que los que tienen dolor mueren :( Como queda la lista de pacientes vivos por atender ordenados por orden de edad desde el joven al viejo.
new=[]
for i in range (len(agenda_hosp)):
    if agenda_hosp[i][5]!='dolor':
        new.append(agenda_hosp[i])
print('#6.',(sorted(new, key=lambda x:x[3])))


#Segunda parte

#Ejercicio 1
size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print (lista)

size1=input('Digame cuantas palabras tiene la lista:')
size1=int(size1)
if(size1)!=len(lista):
    print("imposible")
else:
    print('Es correcto')

#Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)

keyword= input('Digame la palabra a buscar')
conteo=lista.count(keyword)
if conteo>=1:
    print('la palabra aparece %i vez'%conteo)
else:
    print('la palabra no aparece')

#Escriba un programa que permita crear una lista de palabras y que,
# a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)

size2= len(lista)
old=input('la palabra a sustituir es')
new=input('por la palabra')
for i in lista:
    if i==old:
        lista[lista.index(i)]=new
print('la nueva lista es:',lista)

#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.
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
print('la nueva lista es:',lista)

#Escriba un programa que permita crear dos listas de palabras y que,
# a continuación, elimine de la primera lista los nombres de la segunda lista.

size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)

size=input('Cuantas palabras quiere eliminar de la lista?')
size=int(size)
lista2=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista2.append(palabra)
print ('La lista de palabras a eliminar es:',lista2)

lista3=[]
for i in lista:
    if i not in lista2:
        lista3.append(i)
print ('La nueva lista:',lista3)

#Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista
# igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).

size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)
lista2=[]
for i in lista:
      lista2.insert(0,i)
print('la nueva lista es:',lista2)

#Escriba un programa que permita crear una lista de palabras y que, a continuación,
# elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
lista3=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)
for i in lista:
     if i not in lista3:
         lista3.append(i)
print('La lista absoluta es:',lista3)

#Escriba un programa que permita crear dos listas de palabras y que,
# a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):

size=input('Cuantas palabras tiene la lista?')
size=int(size)
lista=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista.append(palabra)
print ('La lista creada es:',lista)

size=input('Cuantas palabras tiene la segunda lista?')
size=int(size)
lista2=[]
for i in range (size):
    palabra=input('escriba la palabra {}:'.format(i+1))
    lista2.append(palabra)
print ('La segunda lista es:',lista2)

lista3=[]
for i in lista:
    if i in lista2:
        if i not in lista3:
            lista3.append(i)
print('Las palabras que aparecen en las dos listas son:',lista3)

lista4=[]
for i in lista:
    if i not in lista2:
        if i not in lista4:
            lista4.append(i)
print('Las palabras que solo aparecen en la lista 1 son:',lista4)

lista5=[]
for i in lista2:
    if i not in lista:
        if i not in lista5:
            lista5.append(i)
print('Las palabras que solo aparecen en la lista 2 son:',lista5)

lista6=list(set(lista+lista2))
print('La lista de todas las palabras es',lista6)