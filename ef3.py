def fharom():
    # A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz a math.fabs() függvény helyett elágazást használjon!
    szam = float(input("Kérem adjon meg egy egész számot!"))
    if szam >= 0:
        eredmeny = szam
        print("|" + str(szam) + "|=" + str(eredmeny))
    else:
        eredmeny = szam * (-1)
        print("|" + str(szam) + "|=" + str(eredmeny))
    #tesztelés
    # be:Kérem adjon meg egy egész számot!0 ki:|0.0|=0.0 működés: ok
    # be:Kérem adjon meg egy egész számot!6 ki:|6.0|=6.0 működés: ok
    # be:Kérem adjon meg egy egész számot!-6 ki:|-6.0|=6.0 működés: ok
