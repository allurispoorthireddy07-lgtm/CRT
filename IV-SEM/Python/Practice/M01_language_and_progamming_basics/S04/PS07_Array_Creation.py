''' import array
arr=array.array('i',[12,45,78,36])
print(arr,type(arr))
arr.append(40)
print(arr)
arr.append(12.45)
print(arr)
'''
'''import numpy
arr=numpy.array([12,45,78,36])
arr1=numpy.array([[1,2,3]
               ,[4,5,6],
               [7,8,9]])
print(arr.shape)
print(arr1.shape)
print(arr.dtype)'''
'''Array -->
it is a collection of homogenous data elements that can store a single variable
python does not support arrays
numpy-->
numpy-- numerical python
it can easily access arrays 
mainly uses in ML,DS,Ai applications
 
 The index value start with 0 and end with (n-1) ,n--size of array''' 
import numpy as np
arr=np.array([12,45,78,36])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(3))
print(np.arange(2,10,2)) #start ,end,step
print(np.linspace(1,10,2)) #start,end,no of values  
n=int(input("Enter the size of array:"))
ele=list(map(int,input("Enter the elements:").split()))
print(np.array(ele))
