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

