import math
def hetedik ():

    #A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

    szam = int(input("Kérem adjon meg egy valós számot!"))

    if (szam >= 0 ):
        eredmeny=math.sqrt(szam)
        print("Négyzetgyök=",round(eredmeny,2))
    else:
        print("Hiba")







