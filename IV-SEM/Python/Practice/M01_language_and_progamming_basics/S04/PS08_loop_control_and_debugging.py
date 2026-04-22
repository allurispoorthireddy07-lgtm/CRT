''' Bug is an error
finding and fixing OF ERRORS is called debugging
Types of errors:
1. Syntax error
2.runtime error
3.logical error'''
''' a=int(input())
b=int(input())
c=a+b
print('a:',a)
print('b:',b)
print('c:',c)
'''
'''try:
    a=int(input())
    print(10/a)
except ZeroDivisionError:
    print('cant divisible bt zero')
except ValueError:
    print("invalid input")'''

import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a=int(input())
b=int(input())
print(add(a,b))
