#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lloyd
#
# Created:     01/09/2023
# Copyright:   (c) lloyd 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

N= int(input())
lis=[]
for i in range(N):
    user=input().split()
    if user[0]=="insert":
        lis.insert(int(user[1]),int(user[2]))
    elif user[0]=="print":
        print(lis)
    elif user[0]=="remove":
        lis.remove(int(user[1]))
    elif user[0]=="append":
        lis.append(int(user[1]))
    elif user[0]=="sort":
        lis.sort()
    elif user[0]=="pop":
        lis.pop()
    else:
        lis.reverse()