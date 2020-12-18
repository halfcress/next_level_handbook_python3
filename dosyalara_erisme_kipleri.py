"""
"r" -> okuma
"w" -> yazma (dosya varsa hata vermez, siler baştan yazar, dosya yoksa oluşturur)
"a" -> yazma (dosya varsa hata vermez, silmez kaldığı yerden yazar, dosya yoksa oluşturur)
"x" -> yazma (dosya varsa hata verir ve yazmaz. dosya yoksa oluşturur ve yazar) silme işlemi istemediğimiz
durumlarda bunu kullanmak daha mantıklıdır. Temiz başlangıç.

"r+" -> okuma ve yazma. (eğer dosya yoksa hata verir)
"w+" -> okuma ve yazma. (dosya yoksa hata vermez, oluşturur. Ancak aynı isimde başka bir dosya varsa içeriğini
siler)
"a+" -> okuma ve yazma (içeriği w gibi silmez, ekleme yapar) (hem dosyayı read eder hem yazarız.)
"x+" -> okuma ve yazma (varsa hata verir yukarıdaki "x" işleminden farkı okumalı versiyon olması.)




"""