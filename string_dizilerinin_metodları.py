Karakter Dizilerinin Metotları
replace()
string = "volkan"
string = string.replace("v","V")
print(string)
Volkan
Bu metot sayesinde bir string içerisinde istediğimiz karakterler yerine yenilerini koyabiliyoruz.

split(), rsplit(), splitlines()
string = "İstanbul Büyükşehir Belediyesi"
bolunmus = string.split(" ")
print(bolunmus)
['İstanbul', 'Büyükşehir', 'Belediyesi']
String ifadeyi, parametre içerisinde verilen öğenin bulunduğu yerlerden böldü.

bolunmus = string.split(" ",1)
print(bolunmus)
string = "bu bir denemedir bu bir denemedir"
bolunmus = string.split(" ",2)
print(bolunmus)
['İstanbul', 'Büyükşehir Belediyesi']
['bu', 'bir', 'denemedir bu bir denemedir']
İkinci parametrede kaç kez bölme işlemi uygulanacağını belirleyebiliyoruz. Fakat dikkat edilmesi gereken şey şudur: iki bölme işlemi uygulandığında ortaya üç adet öğe çıkacaktır.

string = "İstanbul Büyükşehir Belediyesi"
bolunmus = string.rsplit(" ",1)
print(bolunmus)
['İstanbul Büyükşehir', 'Belediyesi']
rsplit() Metodunun tek farkı string ifadeyi sağdan sola doğru okumasıdır.

metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""
print(metin.splitlines())
['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı', "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin", 'Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını', 'düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından', 'gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz', "komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek", 'adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama', 'dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek', 'halini almıştır diyebiliriz.']
splitlines() Metodu ile bir metinsel ifadeyi satırlarına bölebiliriz.

lower()
Büyük harfleri küçük harflere dönüştürmek için kullandığımız bir metot.

print("BUNLAR BÜYÜKTÜR".lower())
bunlar büyüktür
upper()
Küçük harfleri büyük yazdırmak için kullanılır.

print("küçük harfler".upper())
KÜÇÜK HARFLER
islower()
Karakter dizisi içerisinde hiç büyük harf yer almıyorsa True döndürür.

print("küçük harfler".islower())
True
print("Küçük mü".islower())
False
Bir tane dahi büyük harf var ise False döndürür.

isupper()
islower() Metodunun tam tersi görev görür.

print("küçük harfler".isupper())
False
print("BÜYÜK HARFLER".isupper())
True
print("KaRIŞIK".isupper())
False
join()
bolunmus = "İstanbul Büyükşehir Belediyesi".split()
birleştirme_karakteri = " "
string = birleştirme_karakteri.join(bolunmus)
print(string)
İstanbul Büyükşehir Belediyesi
Görüldüğü gibi split ile ayırdığımız veya zaten ayrık olan sözcükleri join() metodu ile birleştirebiliyoruz.

count()
bir ifadenin string içerisinde kaç kez geçtiğini sorgular.

print("deneme".count("e"))
3
index(), rindex()
Bir ifadenin, karakter dizisi içerisinde geçen ilk konumunu döndürür. rindex() ise sağdan sola doğru okuyarak ilk karşılaşılan konumu döndürür.

print("deneme".index("e"))
print("deneme.".rindex("e"))
1
5
find(), rfind()
index() metotlarıyla tamamen aynı işi yapar fakat index() metotları, eğer string içerisinde aranan ifadeyi bulamazsa hata verir, find() metotları ise hata vermez.

string = "deneme"
print(string.index("a"))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-25-36a4283b87e5> in <module>()
      1 string = "deneme"
----> 2 print(string.index("a"))

ValueError: substring not found
print(string.find("a"))
-1
find() metotları bu gibi durumlarda hata yerine -1 değerini döndürür.

isalpha()
Bir string yalnızca alfabe karakterlerinden oluşuyorsa True döndürür.

print("deneme".isalpha())
True
print("dene3me".isalpha())
False
isdigit()
Bir string yalnızca sayısal ifade içeriyorsa True değeri döndürür.

print("1234565".isdigit())
True
print("12434223f".isdigit())
False