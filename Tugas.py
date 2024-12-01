# list jenis kendaraan
kendaraan = ["BMW M4 Competition", "mobil", "2979cc", "hitam", "4 Roda" ]
print(kendaraan)

# Menambahkan harga kendaraan
kendaraan.append("RP 2,774 MILIAR")
print(kendaraan)

# Menambahkan tipe kendaraan 
kendaraan.insert(2, "Sedan")
print(kendaraan)



# Tugas 2
pilih = int  (input("""Selamat datang duaplikasi menghitung
                    1. Untuk menghitung luas persegi
                    2. Untuk menghitung luas linkaran
                    3. Untuk  menghitung luas segitiga 
                    masukan pilihan anda : """))

match pilih:
    case 1 : 
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukan sisi persegi: "))
        luasPsg = sisi*sisi
        print("luas persegi yang sisinya ", sisi,"adalah", luasPsg )
    case 2 : 
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jari_jari = int(input("Masukan jari_jari lingkaran: "))
        luasLkr = 3.14 * jari_jari * jari_jari
        print("luas lingkaran yang jari-jarinya  ", jari_jari,"adalah", luasLkr )
    case 3 : 
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukan masukan alas segitiga: "))
        tinggi = int(input("Masukan masukan tinggi segitiga: "))
        luasSgt = 0,5 * alas * tinggi
        print("luas segitiga dengan alas  ", alas, "dan tinggi", tinggi,"adalah", luasSgt )
    case _: 
        print("Anda Salah Pilih")