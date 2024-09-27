import math
# 16.	Tárolj el 2 számot egy-egy változóba, melyek egy derékszögű háromszög befogói. Mekkora a harmadik oldalt?

a = 3
b = 5
# math.sqrt() gyökvonás
c = math.sqrt(a*a+b*b)
# c = math.sqrt(a**2+b**2)
c= (a**2+b**2)**(1/2)
print("A derékszögű háromszög haramadik oldala: "+str(c))