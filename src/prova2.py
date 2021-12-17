import numpy

l = ['viva']*4
print(l)
l2 = l[2]
tab = [3,6,9,12,15,18,21,27,30]
a = tab[3::]
print(a)
b = tab[8:0:-2]
print(b)
x = list(range(1,18,2))
#for n in x:
print(x)
c = len(x)
a = 44
x2 = x.insert(5,a)
#coda = x2.append(7)
#coda = coda.pop(0)
#print(coda)
tup = ('p','r','o','g','r','a','m','m','a')
print(tup[1:4])
tup2 = (2, 4, 9)
tup = tup +tup2

di = {
  "frutto": "mela",
  "tipo": "fuji",
  "anno": 2021
}
print(di["frutto"])

di['anno'] = 2022

di2 = di.copy()
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
  squares[i] = squares[i] +1 
  #print(squares[i])

  


