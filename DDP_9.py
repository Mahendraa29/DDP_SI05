print("\n====== No 1 ======")

def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)


print("\n====== No 2 ======")

def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)


print("\n====== No 3 ======")

# Rata-Rata nilai kelulusan 70

def skor(nilai):
    if nilai >= 80:
        print("lulus")
    else:
        print("tidak lulus")

skor(80)
skor(40)


print("\n====== No 4 ======")

def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)