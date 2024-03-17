from abc import ABC, abstractmethod

class Bentuk2D(ABC):
    @abstractmethod
    def get_luas(self):
        pass

    @abstractmethod
    def get_keliling(self):
        pass

class PersegiPanjang(Bentuk2D):
    def __init__(self, panjang, lebar):
        self.__panjang = panjang
        self.__lebar = lebar
    
    def get_luas(self):
        return self.__panjang * self.__lebar

    def get_keliling(self):
        return 2 * (self.__panjang + self.__lebar)

kotak = PersegiPanjang(5, 2)
print(f"Keliling: {kotak.get_keliling()}")
print(f"Luas: {kotak.get_luas()}")