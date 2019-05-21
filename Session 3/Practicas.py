lista=[]
Numero=input('Cantidad de pacientes a ingresar:')
cantidad=int(Numero)
for i in range (cantidad):
    a=input('Identificacion del paciente:')
    b=input('Nombre del paciente:')
    c=input ('apellido del paciente:')
    d=input ('tel:')
    e=input('direccion:')
    f=input('lista de enfermedades tratadas:')
    g=input('lista de medicamentos que toma:')
    lista.append([a,b,c,d,e,f,g])

print(lista)

pacientes= dict((i[0],i[1:])for i in lista)
print(pacientes)
a=input('id')
print(pacientes[a][3])