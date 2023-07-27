# class Orang:
#     pass


# org = Orang()
# print(org)

# class mobil:
#     def __init__(self, jenis, warna):
#         self.jenis = jenis
#         self.warna = warna

# mobil1 = mobil('Sedan', 'Merah')
# mobil2 = mobil('SUV', 'Hitam')

# print(mobil1.__dict__)
# print(mobil2.__dict__)

#{'jenis': 'Sedan', 'warna': 'Merah'}
#{'jenis': 'SUV', 'warna': 'Hitam'}


# class Mobil:
#     def print_warna(self):
#         print(self.warna)

#     def print_merk(self):
#         print(self.merk)


# class SUV(Mobil):
#     def __init__(self, warna, merk):
#         self.warna = warna
#         self.merk = merk


# mobil = SUV('Merah', 'Mitsubishi')
# mobil.print_warna()
# mobil.print_merk()


# class Mobil:
#     var_a = 'Merah'


# mobila = Mobil()
# print(mobila.a)


class Pesawat:
    def bisa_terbang(self):
        print('Bisa Terbang')


class Mobil:
    def bisa_terbang(self):
        print('Tidak Bisa Terbang')
# Lalu kita persiapkan metode utamanya,


def cek_terbang(Kendaraan):
    Kendaraan.bisa_terbang()


# Sekarang mari kita inisiasi objectnya,
pesawat = Pesawat()
mobil = Mobil()
# Setelah kita mari kita masukkan ke dalam fungsi kita sebelumnya,
cek_terbang(pesawat)
cek_terbang(mobil)
