#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lloyd
#
# Created:     06/08/2023
# Copyright:   (c) lloyd 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num=int(input("Enter a number:\n"))
if 1<=num<=100:
    if num%2==1:
        print("weird")
    elif num%2==0 and 2<=num<=5:
         print("Not Weird")
    elif num%2==0 and 6<=num<=20:
        print("Weird")
    elif num%2==0 and num>20:
        print("Not Weird")

else:
    print("Invalid input")
