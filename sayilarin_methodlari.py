#integer sayıların methodları;

"""
bit.lenght() --> bit uzunluğu


"""

#float sayıların methodları;
"""
as_integer_ratio() -----> bölüm sonucunu vermesi gereken sayıları gösterir.
is_integer() ---> sayı tam sayı ise true döndürür.
"""

sayi1 = float(input("Lütfen bir sayı giriniz:"))
print("""
Girdiğiniz sayıyı elde etmek için yandaki 1. sayıyı 2. sayıya bölünüz -> {}

""".format(sayi1.as_integer_ratio()))

sayi2= 5.0
print(sayi2.is_integer())

#Karmaşık sayı nitelikleri

"""
imag --> sanal kısmı verir
real --> gerçek kısmı verir.
""" #method olmadıkları için yanlarında () yok.

sayi3 = 5+12j
print(type(sayi3))
print("""
Sayi : {}
Sayinin Reel Kısmı: {}
Sayinin İmajiner Kısmı: {}

""".format(sayi3,sayi3.real,sayi3.imag))