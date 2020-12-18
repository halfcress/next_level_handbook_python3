#kendi hata mesajımızı yaratmaya yarar.

#örneğin;

sayı = int(input("Lütfen 111 dışında bir sayı giriniz"))

if sayı == 111:
    raise Exception("İstenmeyen sayı girildi!!!!!!")

else:
    print("Güzel sayı!")