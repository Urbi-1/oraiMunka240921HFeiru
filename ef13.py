def tizenharom () :
    #A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

     sugar= float(input("Kérem adja meg a kör sugarát!"))
     kerulet = 2* sugar *3.14
     teulet = 3.14* (sugar ** 2)

     if (sugar > 0 ) :
        print("A kör kerülete =",str(kerulet))
        print("A kör területe =", str(teulet))
     else:
        print("Hiba")

