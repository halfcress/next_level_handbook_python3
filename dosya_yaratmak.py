dosya = open("C:/Users/Ozan/Desktop/pano ders/deneme2.txt","w")
#öncelikle dizin belirtilir, ardından slash koyularak yaratacağımız şey girilir. oluşturma işlemi yapmak
#için "w" kullanmalıyız. Bu bir fonksiyon parametresidir. Default olarak read dir, biz write a çevirmiş
#oluyoruz bu sayede. Dosya yoksa yaratır varsa siler yeniden yaratır veya içini boşaltır.


dosya.close() #dosya close etmezsek eğer, büyük çaplı projelerde dosya açık kaldığı için yavaşlığa sebebiyet
#verir.

