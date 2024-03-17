class Hewan:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def makan(self):
        print(self.nama, " sedang makan...")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan...")
    
    def bersuara(self):
        pass

class Kucing(Hewan):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)

    # polymorphism inheritance
    def bersuara(self):
        print("miaw")
    
    # polymorphism antar kelas
    def tidur(self):
        print("sedang tidur di kasur")

class Anjing(Hewan):
    def __init__(self, nama, usia):
        super().__init__(nama, usia)

    # polymorphism inheritance
    def bersuara(self):
        print("guk guk")

    # polymorphism antar kelas
    def tidur(self):
        print("sedang tidur di kamar mandi")

anggora = Kucing("anggora", 5)
anggora.makan()
anggora.berjalan()
anggora.bersuara()

anjing = Anjing("anjing",10)
anjing.makan()
anjing.berjalan()
anjing.bersuara()