import numpy
import sys

lato = input('Inserisci il lato corto: ')
a = float(lato)
lato = input('Inserisci il lato lungo: ')
b = float(lato)
area = a*b

infile='mydata.txt'
outfile='myout.txt'

indata = open( infile, 'r')

with open('mydata.txt') as f:
    contents = f.read()
    print(contents)

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')


with open('Input2.txt', 'r') as f:
  data = f.readlines() 
matrice = []
for raw_line in data :
  split_line = raw_line.strip().split(",")
  nums_ls = [int(x.replace('"', '')) for x in split_line]
  matrice.append(nums_ls)

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(X)):
   
   for j in range(len(Y[0])):
       
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

s = 4 
for i in range(len(X)):
  for j in range(len(X[0])) :
   result[i][j] = X[i][j]*s


class animali:
     
    
    attr1 = "asino"
    attr2 = "cane"
 
    
    def fun(self):
        print("Nel giardino c'è un", self.attr1)
        print("Non troviamo il ", self.attr2)
 

Roger = animali()
 

print(Roger.attr2)
Roger.fun()

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary