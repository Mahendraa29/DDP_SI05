class animal:
    def __init__(self,nama,makanan,hidup,berkembang_biak):
        self.nama = nama
        self.makanan = makanan 
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    
    def cetak(self):
        print(f"hewan {self.nama} ini makanan {self.makanan} hidupnya di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}")

c1 = animal("buaya", "daging","amfibi","bertelur")
c1.cetak()