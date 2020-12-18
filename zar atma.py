import random


menu="""
1)Tek zar için basınız
2)İki zar için basınız
3)Programdan çıkmak için basınız
"""
while True:
    print(menu)
    secim = input("Lütfen seçiminizi giriniz: ")
    if secim== "1":

        print("Zar sonucu :{}".format(random.randint(1,6)))

    elif secim=="2":

        print("Zar sonucu :{} {}".format(random.randint(1, 6), random.randint(1, 6)))

    elif secim=="3":
        quit()
    else:
        print("hatalı giriş yaptınız")
