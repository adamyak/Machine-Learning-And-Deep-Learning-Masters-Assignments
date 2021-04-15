# -*- coding: utf-8 -*-

"""
 Write a program which will find all such numbers which are divisible by 7 but are not
 multiple of 5, between 2000 and 3200(both included). The numbers obtained should be
 printed in comma-separated sequence in single line.
"""

            
a = [num for num in range(2000,3201) if num%7 == 0 if num%5 != 0] 
print(a) 
        

"""
Write a python program to accept the user's first and last name and then getting them 
printed in the reverse order with a space between first and last name.
"""
first_name = input("Enter First name :" )
last_name = input("Enter Last name :")
print("Reversed Order is : {}{}{}".format(first_name[::-1],(" "),last_name[::-1] ))

"""
Write a python program to find the volume of a sphere with diameter 12cm.
Formula = V= 4/3*pi*r**3
"""

import math

d = 12
a =  4/3*math.pi*(d/2)**3
print("Volume of sphere is, V = ",a)