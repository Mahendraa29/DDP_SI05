from Gempa import *
    # membuat objek gempa dengan lokasi dan skala gempa

Gempa1 = Gempa("Banten", 1.2)
GEmpa2 = Gempa("Palu", 6.1)
Gempa3 = Gempa("Cianjur", 5.6)
Gempa4 = Gempa("Jayapura", 3.3)
Gempa5 = Gempa("Garut", 4.0)

#info gempa
print("## info gempa bumi ##")
print()
Gempa1.dampak()
print()
GEmpa2.dampak()
print()
Gempa3.dampak()
print()
Gempa4.dampak()
print()
Gempa5.dampak()
