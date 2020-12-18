"""
abs() -> mutlak değer
divmod() -> bölüm ve kalan
max() -liste içerisindeki maximum değeri gösterir.
min() -liste içerisindeki minimum değeri gösterir.
sum() -dizi içindeki tüm sayıları toplama


"""
sayi1 = -8


print("""
{} sayısının mutlak değeri {} 'dir.

""".format(sayi1,abs(-8)))

sayi2 = 39
sayi3 = 12

print("""
{} sayisi ile {} sayısının bölümleri parantezin ilk başında, kalanı ise parantezin sonundadır.

{}

""".format(sayi2,sayi3,divmod(sayi2,sayi3)))

