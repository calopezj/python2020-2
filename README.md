# python2020-2

Taller de python

## 1 - Lectura de archivos .csv

a=open('data.csv','r').readlines()


## 2 - Split por tab:
a=[row.split('\t') for row in a]



## 3 - Ejemplo de diccionarios

miDic = {'E': 5, 'A': 9, 'B': 8, 'C': 2, 'D': 1}
print(miDic)

for key in miDic.keys():
    print(key + " - " +  str(miDic[key]))



## 4 - Llevar csv a un diccionarios, y agrupar por año (contando registros)

file = open('data.csv', 'r').readlines()
for l in file:
    print(l)
file = [row.split('\t') for row in file]
file = [[row[2].split('-')[0]] for row in file]

for i in file:
    print(i)

result = {}

for i in file:
    result[i[0]] = 0
print(result)

for i in file:
    result[i[0]] = result[i[0]] + 1
print(result)



## 5 - Ejercicio propuesto

file = open('data.csv', 'r').readlines()
file = [row[0:-1] for row in file]
file = [row.split('\t') for row in file]
file = [[row[0], row[4]] for row in file]
listaData = []
for i in file:
    #print(i[1].split(','))
    aux = 0
    for val in i[1].split(','):
        #print(val.split(':')[1])
        aux = aux + int(val.split(':')[1])
    print(i[0])
    print("aux:" , aux)
    print(i[0]+","+ str(aux))




