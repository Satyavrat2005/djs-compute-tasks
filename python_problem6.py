#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      lloyd
#
# Created:     31/08/2023
# Copyright:   (c) lloyd 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        num1=0
        num2=1
        num=num1+num2
        series=[0,1,1]
        for i in range(3,n):
            num1=num2
            num2=num
            num=num1+num2
            series.insert(i+2,num)

    return series
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
