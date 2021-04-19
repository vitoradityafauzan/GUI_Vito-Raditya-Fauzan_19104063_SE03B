# Parameter untuk Inheritance
class Titik(object):
    def __init__(self, x=0, y=0):
        # Self mirip dengan This dr  java, js
        self.x = x
        self.y = y

    def pindah(self, x, y):
        self.x = x
        self.y = y

    def cetak(self):
        print(f'{self.x}, {self.y}')


# Buat Object
titik = Titik()
# memanggil method
titik.cetak()
titik.pindah(5, 10)
titik.cetak()