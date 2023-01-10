# Taş-Kağıt-Makas Oyunu
import random
Liste = ["Taş","Kağıt","Makas"]
toplam_o = 0
toplam_b = 0

while True:
    bilgisayar = random.choice(Liste)

    secim = input("Taş? / Kağıt? / Makas?:")

    print("Bilgisayarın seçimi:{}\nSizin seçiminiz:{}".format(bilgisayar, secim))
    if secim=="Taş" or secim=="taş":
        if bilgisayar==Liste[0]:
            print("Berabere")
        if bilgisayar==Liste[1]:
            toplam_b = toplam_b + 1
            print("Bilgisayar:{}".format(toplam_b))
            print("Siz:{}".format(toplam_o))
        if bilgisayar==Liste[2]:
            toplam_o = toplam_o + 1
            print("Bilgisayar:{}".format(toplam_b))
            print("Siz:{}".format(toplam_o))
    if secim=="Kağıt" or secim=="kağıt":
        if bilgisayar==Liste[0]:
            toplam_o = toplam_o + 1
            print("Bilgisayar:{}".format(toplam_b))
            print("Siz:{}".format(toplam_o))
        if bilgisayar==Liste[1]:
            print("Berabere")
        if bilgisayar==Liste[2]:
            toplam_b = toplam_b + 1
            print("Bilgisayar:{}".format(toplam_b))
            print("Siz:{}".format(toplam_o))
    if secim=="Makas" or secim=="makas":
        if bilgisayar==Liste[0]:
            toplam_b = toplam_b + 1
            print("Bilgisayar:{}".format(toplam_b))
            print("Siz:{}".format(toplam_o))
        if bilgisayar==Liste[1]:
            toplam_o = toplam_o + 1
            print("Bilgisayar:{}".format(toplam_b))
            print("Siz:{}".format(toplam_o))
        if bilgisayar==Liste[2]:
            print("Berabere")
    if toplam_o==3 or toplam_b==3:
        if toplam_o==3:
            print("Tebrikler kazandınız :)")
        else:
            print("Bilgisayar Kazandı.")
        break
