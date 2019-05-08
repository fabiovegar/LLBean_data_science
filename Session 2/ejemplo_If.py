
pixel= [0.6,0.3,0.4]

a=pixel[0]+pixel[1]+pixel[2]
n=len(pixel)
promedio=a/n
print('suma=',a,'n=',n,'promedio=',promedio)

#solucion mediante ciclos
p=0
for numero in pixel:
    p+=numero

p=p/len(pixel)
print('El promedio es',p)

#usando sum
print('El promedio es:',sum(pixel)/len(pixel))


if(p>0.5):
    print('el pixel es blanco')
else:
    print('el pixel es negro')


