hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]


def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
print(b)

#parte1

for i in range (b):
promedio = list(map(lambda x: sum(x)/len(i+1), b[i+1]))
print(promedio)


