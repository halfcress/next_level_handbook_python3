import math

reel = float(input("reel kısım: "))
imag = float(input("imajiner kısım"))

if reel > 0 and imag > 0:


    zmutlak = float(math.sqrt(reel*reel + imag*imag))

    aci = float(math.atan(imag/reel))

    x = zmutlak * zmutlak

    print("""
    Verilen karmaşık sayının;
    Radyan cinsinden açısı: {}
    Derece cinsinden açısı: {}
    Uzunluğu : Karekök içerisinde -> {}
    
    Kutupsal gösterimi: Karekök içerisinde {} * e üzeri j{}
    
    
    """.format(aci,math.degrees(aci),zmutlak*zmutlak,zmutlak*zmutlak,math.degrees(aci)))

elif reel < 0 and imag > 0:

    zmutlak = float(math.sqrt(reel * reel + imag * imag))

    aci = float(math.atan(imag / reel))

    x = zmutlak * zmutlak

    print("""
        Verilen karmaşık sayının;
        Radyan cinsinden açısı: {}
        Derece cinsinden açısı: {} +180 derece***(EKLEMEYİ UNUTMA)
        Uzunluğu : Karekök içerisinde -> {}

        Kutupsal gösterimi: Karekök içerisinde {} * e üzeri j{}+180 derece***(EKLEMEYİ UNUTMA)


        """.format(aci, math.degrees(aci), zmutlak * zmutlak, zmutlak * zmutlak, math.degrees(aci)))

elif reel < 0 and imag < 0:
    zmutlak = float(math.sqrt(reel * reel + imag * imag))

    aci = float(math.atan(imag / reel))

    x = zmutlak * zmutlak

    print("""
        Verilen karmaşık sayının;
        Radyan cinsinden açısı: {}
        Derece cinsinden açısı: {} -180 derece***(ÇIKARMAYI UNUTMA)
        Uzunluğu : Karekök içerisinde -> {}

        Kutupsal gösterimi: Karekök içerisinde {} * e üzeri j{}-180 derece***(ÇIKARMAYI UNUTMA)


        """.format(aci, math.degrees(aci), zmutlak * zmutlak, zmutlak * zmutlak, math.degrees(aci)))

elif reel > 0 and imag < 0:

    zmutlak = float(math.sqrt(reel * reel + imag * imag))

    aci = float(math.atan(imag / reel))

    x = zmutlak * zmutlak

    print("""
        Verilen karmaşık sayının;
        Radyan cinsinden açısı: {}
        Derece cinsinden açısı: {}
        Uzunluğu : Karekök içerisinde -> {}

        Kutupsal gösterimi: Karekök içerisinde {} * e üzeri j{}


        """.format(aci, math.degrees(aci), zmutlak * zmutlak, zmutlak * zmutlak, math.degrees(aci)))

else:
    print("hata!")

