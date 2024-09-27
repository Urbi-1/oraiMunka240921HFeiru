def hatos():
    #A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!
    szam= int(input("Kérem adjon meg egy valósszámot 0-360 között"))

    print(szam)

    if (szam >= 0) and (szam <= 360):
        if (szam == 0) :
            print("nullszög")
        elif (szam >0) and (szam <90) :
            print("hegyesszög")
        elif (szam == 90) :
            print("derékszög")
        elif (szam > 90) and (szam < 180):
            print("tompaszög")
        elif (szam == 180) :
            print("egyenesszög")
        elif (szam > 180) and (szam < 360):
            print("homorúszög")
        elif (szam == 360) :
            print("teljesszög")

    else:
        print("Hiba: érvénytelen százalék!")
