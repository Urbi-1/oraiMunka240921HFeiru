def fmasodik():
    # A program olvasson be a konzolról egy egész számot! A program döntse el, hogy a megadott számpáros vagy páratlan, és írja ki az eredményt a konzolra!
    szam = int(input("Kérem adjon meg egy egész számot!"))
    if szam%2 == 0:
        print("A szám páros.")
    else:
        print("A szám páratlan.")
    # tesztelés
    # páros szám be:2 ki:A szám páros. működés: ok
    # páratlan szám be:5 ki:A szám páratlan. működés: ok
    # 0 be:0 ki:A szám páros. működés: ok