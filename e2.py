def masodik():
    # 2.	MegelőzőKövetkezőSzám: A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!

    szam = int(input("Kérem adjon meg egy egész számot!"))
    if (szam < 10) and (szam > -10):
        megelozo = szam-1
        rakovetkezo = szam +1
        print("A(z) "+str(szam)+" szám megelöző és rákövetkező egész értékei: "+str(megelozo)+", "+str(rakovetkezo)+".")

