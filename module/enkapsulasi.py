import random

class Manusia:
    def __init__(self, nama: str, umur: int, tinggi_badan: float, berat_badan: float):
        self.__nama = nama
        self.__umur = umur
        self.__tinggi_badan = tinggi_badan
        self.__berat_badan = berat_badan

    @staticmethod
    def is_mature(umur):
        if umur > 18:
            print("Udah dewasa")
        else:
            print("Belum dewasa")

    @classmethod
    def generate(cls, nama):
        return cls(nama, random.randrange(1,100), random.uniform(1,100),random.uniform(1,100))
    
    # getter
    @property
    def nama(self):
        return self.__nama

    # getter
    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    # setter
    def set_umur(self, umur_baru):
        self.__umur = umur_baru

    umur = property(get_umur, set_umur)

    def __str__(self) -> str:
        return "Nama: {}\n" \
            "Umur: {}\n" \
            "TB: {}\n" \
            "BB:{}".format(self.nama, self.umur, self.tinggi_badan, self.berat_badan) 

class Hewan:
    def __init__(self, nama: str, jenis: str):
        self.nama = nama
        self.jenis = jenis

    def berjalan(self, orang: Manusia):
        print(f"Hewan {self.nama} sedang berjalan")
        # orang.nama = self.nama
        # orang.set_umur(100)
        orang.umur = 100

orang = Manusia("seekor orang", 5, 2, 1)
musang = Hewan("Akhdan", "Mamalia")

print(orang.nama)
print(orang.get_umur())

musang.berjalan(orang)

print(orang.get_nama())
print(orang.get_umur())

akhdan = Manusia.generate("akhdan")
print(akhdan.umur)

Manusia.is_mature(akhdan.umur)