import numpy as np
import matplotlib as mpl
import array as ar
from scipy import fftpack

a = [1,2,3,4,5] 
a_numpy = np.array(a)

a = range(0,15) 
b = a.reshape(3,5) 
a = np.ones((3,4))

y = np.array([[1,3],[5,6]])
x = np.copy(y)
x = np.array([[1,2],[3,4]])
y = np.swapaxes(x,0,1)

newarr = ar.array('d', [2.1, 4.5, 5.5])
print(newarr)
newarr.append(4)
newarr.extend([5, 6, 7])

dispari = arr.array('i', [1, 3, 5])
pari = arr.array('i', [2, 4, 6])

num = arr.array('i')   
numb = pari + dispari

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


