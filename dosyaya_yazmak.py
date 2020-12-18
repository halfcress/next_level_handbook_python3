dosya = open("C:/Users/Ozan/Desktop/pano ders/deneme2.txt","w")

#yazılacak şeyler öncelikle dosya oluşturulduktan veya programa gösterildikten sonra bir değişkene atılır.
#ve method aracılığı ile bu değişken yazdırılır.

yazılacaklar = "halfcress"

dosya.write(yazılacaklar)


dosya.close()

dosya2 = open("C:/Users/Ozan/Desktop/pano ders/deneme2.txt")

okuma_degiskeni = dosya2.read()

print(okuma_degiskeni)