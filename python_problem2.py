#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lloyd
#
# Created:     31/08/2023
# Copyright:   (c) lloyd 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

n=int(input())
if 1<=n<=20:
    for i in range(0,n):
        print(i**2)
else:
    print("Invalid Input")