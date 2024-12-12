from animals import*
class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,Bisa, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bisa = Bisa
        self.warna = warna

    def cetak_ular(self):
        super().cetak()
        print(f"ular ini {self.bisa} dan hewan ini bewarna {self.warna}")

kobra = ular("ular kobra", "daging", "hutan", "bertelur", "berbisa", "hitam" )
kobra.cetak_ular()

sanca = ular("ular sanca", "daging", "hutan", "bertelur", "berbisa", "hijau" )
sanca.cetak_ular()