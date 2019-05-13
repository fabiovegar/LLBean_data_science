# Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.
mis_valores = [5,6,10,13,3,4]
sum = 0
for i in mis_valores:
    sum+=i
print('El promedio es',sum/(len(mis_valores)))

#Considere si se tiene una lista que contiene las alturas de grupos de personas
#Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas
todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

maximo=max(todos)
print('La altura maxima es',max(maximo))
print('el grupo es', todos.index(maximo)+1)

