#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lloyd
#
# Created:     31/08/2023
# Copyright:   (c) lloyd 2023
# Licence:     <your licence>
import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    b=numpy.array([],float)
    for i in range(0,len(a)):
        b=numpy.append(b,a[len(a)-1-i])

    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)