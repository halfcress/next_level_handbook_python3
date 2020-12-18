kelime = "ozanhalfcress"

print(kelime[2:6]) #2. indexten başlayarak 6. indexe kadar bastır. 6 dahil değil.
print(kelime[2:]) # bu şekilde bırakırsak 2 den başlayara sonuna kadar yazar. ancak toplamda 13 karakter
#ve 12 indexten oluşan bu değişkende print(kelime[2:100]) gibi abartı büyük bir değer yazsaydık ta hata
#mesajı almayacaktık ve 2 den başlayarak sona kadar yazacaktı aynı şekilde.
print(kelime[:5]) #0. indexten başlayıp 5. indexe kadar yaz. 5. index dahil değil.
print(kelime[::]) #atlayarak yaz demektir ancak bu şekilde bırakırsak baştan başlayıp sona kadar bastırır. Bunu
#kullanmak için;
print(kelime[::1]) #defaultundan hiç bir farkı yoktur baştan başlayarak sıra sıra yazar.
print(kelime[::2]) #baştan başlayarak 2 şer index ara ile yazar
print(kelime[::3]) #baştan başlayarak 3 er index ara ile yazar. Şayet;
print(kelime[::-1]) # şeklinde bir kullanım olursa bu sefer tersten başlayarak sıra sıra yazar.
print(kelime[::-2]) #sondan başlayarak 2 şer index ara ile yazar.
print(kelime[::-3]) #sondan başlayarak 3 er index ara ile yazar.