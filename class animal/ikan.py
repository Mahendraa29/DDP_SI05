from animals import *
class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,warna_ikan,jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f"warna ikan ini adalah warrna {self.warna} dan hewan ini jenisnya {self.jenis}")

print("####### cetak ikan #######")
print("####### objek pertama ####### ")
nemo = ikan("ikan nemo", "plankton", "air", "bertelur", "orange", "ikan air laut")
nemo.cetak_ikan()

print("####### objek kedua ####### ")
piranha = ikan("ikan piranha", "daging", "air", "bertelur","coklat", "ikan air tawar")
piranha.cetak_ikan()