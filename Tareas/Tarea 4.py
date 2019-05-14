hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]


def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
print(b)
print(len(b[1]))

#parte1


#mi_dict= {'ave':lambda x,y,z,a:x+y+z/a,'sum'=lambda x,y,z:x+y+z,'mult':lambda x,y,z: x*y,z}

mi_dict= {'ave':lambda x,y,z,a:(x+y+z)/a,'sum':lambda x,y,z:x+y+z,'multi':lambda x,y,z:x*y*z,'imp':list(map(lambda x:x*1.2,b[2]))}

#parte2

#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.
#2. La suma de todas las deudas
#3. la multiplicación de todos los crédito entre si

print('El promedio de lo que tienen las personas es:',mi_dict['ave'](b[1][0],b[1][1],b[1][2],len(b[1])))

print('La suma de la deuda es:',mi_dict['sum'](b[2][0],b[2][1],b[2][2]))

print('La multiplicación del credito es:',mi_dict['multi'](b[3][0],b[3][1],b[3][2]))

#Parte 3
#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20% (esto es multiplicar por 1.2)
#a toda la fila de créditos usando el diccionario de funciones.

print('El valor actualizado de los creditos es:',mi_dict['imp'])