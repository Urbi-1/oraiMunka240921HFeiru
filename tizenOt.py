# 15.	Tárolj el 3 számot egy-egy változóba! Írd ki a középső számot az értékük szerint összehasonlítva!

szam1 = -1.5
szam2 = -4
szam3 = 2.5

if ((szam1 < szam2) and (szam2 < szam3)) or ((szam3 < szam2) and (szam1 > szam2)):
    print("A középső szám: " + str(szam2))
elif ((szam1 < szam3) and (szam2 > szam3)) or ((szam1 > szam3) and (szam2 < szam3)):
    print("A középső szám: " + str(szam3))
else:
    print("A középső szám: " + str(szam1))
