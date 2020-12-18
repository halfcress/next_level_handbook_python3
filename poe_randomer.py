import random
import os
build_liste = list()

menu = """
1) build ekle
2) görüntüle
3) çekilişi başlat

"""

while True:

    print(menu)
    os.system("cls")
    secim = input("Seçimi yap:")

    if secim == "1":
        add_build = input("Eklenecek buildi gir: ")
        build_liste.append(add_build)
        print("çıkmak için enter'a bas")
        input()

    elif secim == "2":
        print(build_liste)
    elif secim == "3":
        print("""
        Çuzi : {} veya {}
        Duzi : {} veya {}
        Ozi :  {} veya {}
        
        
        """.format(random.choice(build_liste),random.choice(build_liste),random.choice(build_liste),random.choice(build_liste),random.choice(build_liste),random.choice(build_liste)))
    else:
        print("hatalı giriş")


