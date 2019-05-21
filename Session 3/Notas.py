#Funcion type, es para ver que tipo de datos tiene
#milista=a
#print('milist: {},type{}',format

a=[0,1,2,3]
b=[2.3,4]

print('a:{},b:{}'.format(a,b))

#en conjuntos se pueden usar las funciones de mate
#los sets permiten

#FUNCIONES:
#def nombre de la funcion (los parametros de la funcion) - con el & manejo la interseccion

a= [1,2,3]
b= [3,4,5,2]

def listaabs(x,y):
    x=set(x)
    y=set(y)
    return[list(x-y)]
y=listaabs(a,b)
print(y)
pass

mi_lista=[(1,2,3,4),(5,6,7,8),(9,10,11,12)]
pass

#si la dimension de una lista [:]principio a fin y [::-1] reversa
#si necesito invertir una tupla y la lista [p[::-1] for p in mi_lista[::-1]

#Diccionarios:
#dict.keys (llaves), dict.vale(valores), dict.item(keys:value)
    #dict={'keys':value}


#Funciones
#crear una funcion que me permita sumar los numeros que me pongan
#* para meter cantidad de valores, ** nombres de parametros

def sumar(*n):
    #return (n+=n)
pass
resultado=sumar(5,7,9,1)

#** nombres de parametros
resultado1=sumar(nombre='felix', apellido='arias', numero='10')
print(resultado)
#*i**n (variables y nombres de parametros
def sumar(*i,**n)


#con class se puede hacer cualquier cosa y permite crear tipos de datos

class Duck (definir quien nace)
    def quack (definir sus caracteristicas)
    def walk

creo un pato llamado Donald
donald=Duck()

#si ocupo hacer algo tengo que hacer un def_init_