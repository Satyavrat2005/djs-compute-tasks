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

def is_leap(year):
    if year%4==0:
        if year%100!=0 or year%400==0:
            return True

    return False


year = int(input())
print(is_leap(year))