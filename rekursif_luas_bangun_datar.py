import math

def luas_lingkaran(r):
    return math.pi * r * r
def luas_persegi(sisi):
    return sisi * sisi
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
while True:
    print("Pilih bangun datar:")
    print("1. Lingkaran")
    print("2. Persegi")
    print("3. Segitiga")
    print("4. Keluar")
    
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        r = float(input("Masukkan jari-jari: "))
        print("Luas lingkaran:", luas_lingkaran(r))
    elif pilihan == 2:
        sisi = float(input("Masukkan panjang sisi: "))
        print("Luas persegi:", luas_persegi(sisi))
    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print("Luas segitiga:", luas_segitiga(alas, tinggi))
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid")