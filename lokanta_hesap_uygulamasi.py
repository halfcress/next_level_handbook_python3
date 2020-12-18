masalar = dict()
for i in range(10):
    masalar[i] = 0

def hesapekle():

    masano = int(input("Lütfen masayı seçiniz:"))
    if masano <= 9:
            eklenecekmasa = masalar[masano]
            tutar = int(input("Lütfen eklenecek tutarı seçiniz"))
            toplam = tutar + eklenecekmasa
            masalar[masano] = toplam

            print("ekleme işlemi başarılı! lütfen menüye dönmek için bir tuşa basınız")
            input()
    else:
            print("Böyle bir masa bulunamadı")
def hesapcikar():

    masano = int(input("Lütfen masayı seçiniz:"))
    if masano <= 9:
            cikarilacakmasa = masalar[masano]
            tutar = int(input("Lütfen çıkarılacak tutarı seçiniz"))
            cikarilan = cikarilacakmasa - tutar
            masalar[masano] = cikarilan
            print("çıkarma işlemi başarılı! lütfen menüye dönmek için bir tuşa basınız")
            input()
    else:
            print("böyle bir masa bulunamadı")


def hesapkontrol(dosya_adi):

    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("/n")
        veriler.pop()
        dosya.close()
        flag = True

    except FileNotFoundError:
        dosya = open(dosya_adi, "w")
        dosya.close()
        print("Program ilk kez çalıştırıldı ve kayıt dosyası oluşturuldu.")
        flag = False
    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = float(i[1])
    else:
        pass

def kayitguncelle():
    dosya = open("kayitlar.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "/n")

    dosya.close()






def main():

    hesapkontrol("kayitlar.txt")

    while True:

        print("""
        [1] Masaları görüntüle
        [2] Hesap ekle
        [3] Hesap çıkar
        [4] Çıkış
            
        """)

        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz.")

        if secim == "1":
            for i in range(10):
                print("Masa numarası {} , Masa Ücreti {}".format(i,masalar[i]))

            input()

        elif secim == "2":
            hesapekle()
        elif secim == "3":
            hesapcikar()
        elif secim == "4":
            quit()
        else:
            print("Hatalı giriş yaptınız.")




main()



