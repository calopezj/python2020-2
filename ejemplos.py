file = open('data.csv', 'r').readlines()

#for l in file:
    #print(l)

file = [row.split('\t') for row in file]
for l in file:
    print(l)


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
