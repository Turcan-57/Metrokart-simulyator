# MetroKart Simulyatoru

PIN_KOD = "1234"
cehd = 3

# Başlanğıc dəyərlər
balans = 0
borc = 0
gunluk_limit = 100
gunluk_artirim = 0
gedis_sayi = 0
umumi_odenis = 0
umumi_endirim = 0
emeliyyatlar = []

rejim = "normal"

# PIN giriş
while cehd > 0:
    pin = input("PIN daxil et: ")
    if pin == PIN_KOD:
        print("Giriş uğurludur\n")
        break
    else:
        cehd -= 1
        print("Səhv PIN! Qalan cəhd:", cehd)

if cehd == 0:
    print("Kart bloklandı!")
    exit()

# Əsas proqram
while True:
    print("\n1) Balansı göstər")
    print("2) Balans artır")
    print("3) Gediş et")
    print("4) Son əməliyyatlar")
    print("5) Günlük statistika")
    print("6) Parametrlər")
    print("0) Çıxış")

    secim = input("Seçim et: ")

    # 1. Balans
    if secim == "1":
        print("Balans:", balans, "AZN | Borc:", borc)

    # 2. Balans artır
    elif secim == "2":
        try:
            mebleg = float(input("Məbləğ daxil et: "))
            if mebleg <= 0:
                print("Yanlış məbləğ!")
                continue

            if gunluk_artirim + mebleg > gunluk_limit:
                print("Limit keçildi!")
                continue

            gunluk_artirim += mebleg

            if borc > 0:
                if mebleg >= borc:
                    mebleg -= borc
                    borc = 0
                else:
                    borc -= mebleg
                    mebleg = 0

            balans += mebleg
            emeliyyatlar.append(("Artırım", mebleg, 0, balans))

            print("Yeni balans:", balans)

        except:
            print("Yanlış daxil etdiniz!")

    # 3. Gediş
    elif secim == "3":
        if rejim == "telebe":
            qiymet = 0.20
            endirim = 0
        elif rejim == "pensiya":
            qiymet = 0.15
            endirim = 0
        else:
            gedis_sayi += 1
            if gedis_sayi == 1:
                qiymet = 0.40
                endirim = 0
            elif 2 <= gedis_sayi <= 4:
                qiymet = 0.36
                endirim = 0.04
            else:
                qiymet = 0.30
                endirim = 0.10

        if balans >= qiymet:
            balans -= qiymet
            umumi_odenis += qiymet
            umumi_endirim += endirim
            emeliyyatlar.append(("Gediş", qiymet, endirim, balans))
            print("Keçid uğurlu!")
        elif 0.30 <= balans < 0.40:
            print("Təcili keçid edildi!")
            balans -= 0.30
            borc += 0.10
        else:
            print("Balans kifayət etmir!")

    # 4. Son əməliyyatlar
    elif secim == "4":
        try:
            n = int(input("Neçə əməliyyat göstərilsin: "))
            for emel in emeliyyatlar[-n:]:
                print(emel)
        except:
            print("Yanlış!")

    # 5. Statistika
    elif secim == "5":
        print("Gediş sayı:", gedis_sayi)
        print("Ümumi ödəniş:", umumi_odenis)
        print("Ümumi endirim:", umumi_endirim)
        print("Artırılan məbləğ:", gunluk_artirim)

    # 6. Parametrlər
    elif secim == "6":
        print("1) Limit dəyiş")
        print("2) Rejim dəyiş")
        sec = input("Seç: ")

        if sec == "1":
            try:
                gunluk_limit = float(input("Yeni limit: "))
            except:
                print("Yanlış!")
        elif sec == "2":
            print("1) Normal")
            print("2) Tələbə")
            print("3) Pensiyaçı")
            r = input("Seç: ")
            if r == "1":
                rejim = "normal"
            elif r == "2":
                rejim = "telebe"
            elif r == "3":
                rejim = "pensiya"

    # 0. Çıxış
    elif secim == "0":
        print("Proqram dayandı")
        break

    else:
        print("Yanlış seçim!")
