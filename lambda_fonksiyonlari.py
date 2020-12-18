def ucgenmi(a,b,hipotenüs):
    if a**2 + b**2 == hipotenüs**2:
        return True
    else:
        return False

print(ucgenmi(3,4,5)) ##true verecek
print(ucgenmi(2,4,5)) ##false verecek

# ancak biz bu tarz kolay fonksiyonlarda def yerine lambda denen özel tanılamayı kullanmalıyız. Çünkü
#python üzerinde lambda , def e ziyade çok daha hızlı çalışır.
#örneğin;

fonksiyon = lambda a,b,hipotenüs : a**2 + b**2 == hipotenüs**2
#ilk başa tanımlayacağımız fonksiyon değişkeni, ikinci kısıma lambda olduğunu belirtmek ve arkasında kullanacağımız parametreler.
#ve en son olarak TRUE vermesini istediğimiz olayı yazıyoruz.

print(fonksiyon(3,4,5)) #true verecek.
print(fonksiyon(2,4,5)) #false verecek.