class eleman:

    carpan = 5

    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        self.eposta = self.ad+self.soyad+"@sirket.net"
    def adsoyad(self):
        return "adı : {}  soyadı : {}".format(self.ad,self.soyad)

calisan1 = eleman("ozan","gözlüklü",3500)

calisan2 = eleman("halfcress","hc",1950)

print(eleman.adsoyad(calisan1))
print(eleman.carpan)


# print(calisan1)
# print(calisan1.ad,calisan1.soyad,calisan1.eposta)
# print(calisan1.adsoyad())
#
# print(calisan2)
# print(calisan2.ad,calisan2.soyad)
# print(calisan2.eposta)



# class eleman:
#     def __init__(self,ad,soyad,maas):
#         pass
#
# calisan1 = eleman("ozan","gözlüklü",3500)
# calisan1.ad = "ozan"
# calisan1.soyad = "gözlüklü"
# calisan1.maas = 3500
#
# calisan2 = eleman()
# calisan2.ad = "halfcress"
# calisan2.soyad = "hc"
# calisan2.maas = 1950
#
#
# print(calisan1)
# print(calisan1.ad,calisan1.soyad)
#
# print(calisan2)
# print(calisan2.ad,calisan2.soyad)