class Orang:

    def __init__(self, nama: str, umur: int, tinggi_badan: float, berat_badan: float):
        self.nama = nama
        self.umur = umur
        self.tinggi_badan = tinggi_badan
        self.berat_badan = berat_badan

    def __str__(self) -> str:
        return "Nama: {}\n" \
            "Umur: {}\n" \
            "TB: {}\n" \
            "BB:{}".format(self.nama, self.umur, self.tinggi_badan, self.berat_badan) 


kevin = Orang("kevin", 1, 5, 1)
mamat = Orang("Mamat", 99, 50, 10000)

print(kevin)
print(mamat)



tab = {
    'geeks': 4127, 
    'for': 4098, 
    'geek': 8637678
}

# using format() in dictionary
print('Geeks: {0}; For: {1}; '
    'Geeks: {1}'.format(tab, "kevin"))
 
# data = dict(fun ="GeeksForGeeks", adj ="Portal")
 
# print("I love {fun} computer {adj}".format(**data))
