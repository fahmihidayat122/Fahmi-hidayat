from re import U


ulangi = True

while ulangi:

    class Mobil:
        def __init__(self, merek,cc,harga):
            self.merek = merek
            self.cc = cc
            self.harga = harga

        def showKategori(self):
            kategori = "komersial"
            if self.cc == 500:
                kategori = "komersial"
            elif self.cc == 1000:
                kategori = "semi-sport"
            elif self.cc == 2000:
                kategori = "Sport"
            print("Mobil dengan Merek {} dan CC sebesar {} dan harga sebesar {}. Kategori mobil adalah {}".format(self.merek,self.cc,self.harga, kategori))

    merek_mobil = (input("masukkan merek : "))
    cc_mobil = int(input("masukkan CC : "))
    harga_mobil = int(input("masukkan harga : "))

    mobil = Mobil(merek_mobil,cc_mobil,harga_mobil)

    mobil.showKategori()

    confirm = input("Ulangi Program [Y/N]: ")

    if confirm == "y" or confirm == "Y":
        ulangi = True
    else:
        ulangi = False