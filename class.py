# class merupakan sebuah blueprint
class Bangunan:
    def __init__(self, nama, tinggi, total_pekerja):
        self.nama = nama
        self.tinggi = tinggi
        self.total_pekerja = total_pekerja
    
    # method / fungsi class
    # sifat dari objek
    def roboh(self):
        print(f"yah bangunan {self.nama} roboh :(")

    def selisih_tinggi(self, other):
        print(f"selisihnya: {abs(self.tinggi - other.tinggi)}")

gedung_c = Bangunan("gedung c", 10, 9000)
gedung_z = Bangunan("gedung z", 100, 1)
gedung_c.roboh()
gedung_z.selisih_tinggi(gedung_c)