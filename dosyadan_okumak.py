dosya2 = open("C:/Users/Ozan/Desktop/pano ders/deneme2.txt","r")

okunan = dosya2.readlines() #readlines satır satır okur ve her okuduğu satırı bir öğe olarak listeye
# yerleştirir. Eğer alt satıra geçme işlemi yapıldıysa onlarıda /n olarak göreceğiz.
print(okunan)

#readlines ' ın read ' den farkı üstte yazdığımdır. ancak normal dosyanın içini okumak için read i kullanmak
#daha mantıklı. readlines'ın readline' dan farkı ise adından da anlaşılacağı üzere readline yalnızca ilk
# satırı alıyor.


dosya2.close()

#yazmada kullandığımızın tam tersini uyguladık özetle.