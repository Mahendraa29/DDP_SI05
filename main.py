import math

# BANGUN DATARr

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f"luas persegi {sisi} * {sisi} = {luas}")
    print(f"keliling persegi adalah {keliling}")

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2* (panjang + lebar)
    print(f"luas persegi panjang adalah {panjang} * {lebar} = {luas}")

def l_segitiga(alas, tinggi):
    luas= 1/2*alas*tinggi
    print(f"Luas segitiga adalah {alas} * {tinggi} = {luas}")

def l_lingkaran(r):
    luas = 3.14*r**2
    keliling = 2*3.14*r
    print(f"Luas lingkaran dengan jari-jari {r} adalah = {luas}")
    print(f"keliling lingkaran jari-jari{r} adalah = {keliling}")

def l_jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    print(f"Luas jajar genjang adalah {alas} * {tinggi} = {luas}")


# BANGUN RUANG

def l_kubus(s):
    volume = s*s*s
    luas = 6*(s*s)
    print(f"volume kubus dengan sisi {s} adalah = {volume}")
    print(f"luas kubus dengan sisi {s} adalah = {luas}")

def l_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas = 2 * [(panjang * lebar ) + (panjang * tinggi ) + (lebar * tinggi )]
    print(f"volume balok adalah  {panjang} * {lebar} * {tinggi} = {volume}")
    print(f"luas balok adalah = 2 * [({panjang} * {lebar}) + ({panjang} * {tinggi})+ ({lebar} * {tinggi})]  = {luas}")

def l_tabung(r, tinggi):
    volume = 3.14 * r**2 * tinggi
    luas = 2 * 3.14 * r * (r + tinggi)
    print(f"volume tabung adalah 3.14 * {r}**2 * {tinggi} = {volume}")
    print(f"keliling tabung adalah 2 * 3.14 * {r} * ({r} + {tinggi} = {luas}")

def l_bola(r):
    volume = 4/3 * 3.14 * r**3
    luas = 4 * 3.14 * r**2
    print(f"Luas bola dengan jari-jari {r} adalah = {volume}")
    print(f"Luas bola dengan jari-jari {r} adalah = {luas}")
    
def l_kerucut(r, tinggi, luas_selimut):
    volume = 1/3 * (3.14 * r**2)* tinggi
    luas = (3.14 * r * luas_selimut )+(3.14 * r * r)
    print(f"volume kerucut adalah 1/3 * (3.14 * {r}**2)* {tinggi}= {volume}")
    print(f"Luas kerucut adalah (3.14 * {r} * {luas_selimut} )+(3.14 * {r} * {r}) = {luas}")
    
# PERHITUNGAN DASAR

def penjumblahan(bil1, bil2):
    penjumblahan = bil1 + bil2
    print(f"hasil penjumblahan dari {bil1} + {bil2} adalah = {penjumblahan}")

def pengurangan(bil1, bil2):
    pengurangan = bil1 - bil2
    print(f"hasil pengurangan dari {bil1} - {bil2} adalah = {pengurangan}")

def pembagian(bil1, bil2):
    pembagian = bil1 / bil2
    print(f"hasil penjumblahan dari {bil1} / {bil2} adalah = {pembagian}")

def perkalian(bil1, bil2):
    perkalian = bil1 * bil2
    print(f"hasil pekalian dari {bil1} x {bil2} adalah = {perkalian}")

def pangkat(bil1, bil2):
    pangkat = bil1 ** bil2
    print(f"hasil pangkat dari {bil1} ** {bil2} adalah = {pangkat}")