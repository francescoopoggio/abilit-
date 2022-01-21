import numpy as np
import matplotlib as mpl
import array as ar
from scipy import fftpack

a = [1,2,3,4,5] 
a_numpy = np.array(a)

a = range(0,15) 
b = a.reshape(3,5) 
print (b)
a = np.ones((3,4))
print (a)

y = np.array([[1,3],[5,6]])
x = np.copy(y)
print (y)
print (x)
x = np.array([[1,2],[3,4]])
y = np.swapaxes(x,0,1)
print (y)
print (x)

newarr = ar.array('d', [2.1, 4.5, 5.5])
print(newarr)
newarr.append(4)
newarr.extend([5, 6, 7])

dispari = arr.array('i', [1, 3, 5])
pari = arr.array('i', [2, 4, 6])

num = arr.array('i')   
num = pari + dispari
print (num)

num.remove(6)
print(num) 
print(num.pop(2))  
print(num)  

a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)

a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])
print (a + b)

a = np.zeros((3, 3), np.int)
print(a.shape)
b = np.arange(3)

a = np.arange(100)
b = np.arange(100)
dot_product = np.dot(a, b)
outer_product = np.outer(a, b)
vector = np.multiply(a, b)
print (dot_product)
print (outer_product)
print (vector)

A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
print(C)


t = np.arange(0.0, 2.0, 0.1)
s = 1 + np.sin(2*np.pi*t)np.exp(-t)
plt.plot(t,s)

