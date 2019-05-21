lista=[]
pacientes={}
Numero=input('Cantidad de pacientes a ingresar:')
cantidad=int(Numero)
for i in range (cantidad):
    a=input('Identificacion del paciente:')
    b=input('Nombre del paciente:')
    c=input ('apellido del paciente:')
    d=input ('tel:')
    e=input('direccion:')
    f=input('lista de enfermedades tratadas:')
    f1=list(f.split(','))
    g=input('lista de medicamentos que toma:')
    g1=list(g.split(','))
    pacientes[a]=[b,c,d,e,f1,g1]
print(pacientes)

#Ingreso de un paciente nuevo
accion= input('Que desea hacer:agregar, borrar, modificar paciente:')
if accion =='agregar':
    a = input('Identificacion del paciente:')
    b = input('Nombre del paciente:')
    c = input('apellido del paciente:')
    d = input('tel:')
    e = input('direccion:')
    f = input('lista de enfermedades tratadas:')
    f1=list(f.split(','))
    g = input('lista de medicamentos que toma:')
    g1=list(g.split(','))
    pacientes[a]=[b,c,d,e,f1,g1]
    print(pacientes)
#borrar un paciente
elif accion == 'borrar':
    dele=input('Desea borrar un paciente: SI?')
    if dele == 'SI':
        a=input('Digite el id del paciente a borrar')
        del pacientes[a]
        print('La lista actualizada de pacientes es:',pacientes)
elif accion == 'modificar':
    id = input('digite el id del paciente:')
    ident=input('Que desea modificar: enfermedades o medicamentos?')
    if ident=='enfermedades':
        enf=input('Digite las enfermedades a agregar:')
        enf1=list(enf.split(','))
        pacientes[id][4].extend(enf1)
        print(pacientes)
    elif ident=='medicamentos':
        inf=input('Digite las medicamentos a agregar:')
        inf1=list(inf.split(','))
        pacientes[id][5].extend(inf1)
        print(pacientes)

#reporte de las enfermedades en la clinica
enfermedades=[]
for i in pacientes:
    enfermedades.extend(pacientes[i][4])
enfermedades1=set(enfermedades)
print('El reporte de las enfermedades tratadas es el siguiente:',enfermedades1)

#reporte de medicamentos entregados en la clinica
meds=[]
for i in pacientes:
    meds.extend(pacientes[i][5])
meds1=set(meds)
print('El reporte de las medicamentos recetados es el siguiente:',meds1)

#comparar dos pacientes en comun
comp=input('Desea comparar pacientes: si o no')
if comp =='si':
    id1=input('Digite el id del paciente1')
    id2=input('Digite el id del paciente2')
    a11 = set(pacientes[id1][4])
    b12 = set(pacientes[id2][4])
    c11 = set(pacientes[id1][5])
    d12 = set(pacientes[id2][5])
    print('Las enfermedades en comun son:',a11 & b12)
    print('Las enfermedades exclusivas del paciente %s son:'%id1,a11-b12)
    print('Las enfermedades exclusivas del paciente %s son:'%id2, b12-a11)
    print('Los medicamentos en comun son:', c11&d12)
    print('Los medicamentos exclusivos del paciente %s son:' % id1, c11-d12)
    print('Las medicamentos exclusivos del paciente %s son:' % id2, d12-c11)
