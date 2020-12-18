import os

bulunulan_dizin = os.getcwd()

print(bulunulan_dizin)
print("dizin değişti")

os.chdir("../../") #change directory
bulunulan_dizin = os.getcwd()

print(bulunulan_dizin)

print("asdasdeasdasd")
input("enter a basınız")

os.system("cls") #linux için "clear" , ekranı temizlemeye yarar.

os.path.expanduser("~") #ev dizinini işaret eder.
ev_dizin = os.path.expanduser("~") # bu şekilde kullanır ve ev_dizin değişkenini bastırırsak;
print(ev_dizin) #ev dizinini gösterir.

