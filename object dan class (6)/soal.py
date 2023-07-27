# # soal no 1
# class belanja():
#     total_belanja = 0

#     def __init__(self, nama_barang, jumlah_barang, harga):
#         self.nama_barang = nama_barang
#         self.jumlah_barang = jumlah_barang
#         self.harga = harga
#         self.total_harga = jumlah_barang*harga
#         belanja.total_belanja += 1

#     def detail_belanja(self):
#         print('Nama barang :', self.nama_barang)
#         print('Jumlah Barang :', self.jumlah_barang)
#         print('Harga : Rp', self.harga)
#         print('Total Harga : Rp', self.total_harga)

#     def jumlah_belanja(self):
#         print('jumlah belanja yang di beli =', belanja.total_belanja)


# # membuat objek
# belanjaan1 = belanja('sepatu', 1, 35000)
# belanjaan2 = belanja('kemeja', 4, 2500000)
# belanjaan3 = belanja('Binder A5', 2, 32000)

# # pemanggilan detail belanja
# belanjaan1.detail_belanja()
# belanjaan2.detail_belanja()
# belanjaan3.detail_belanja()

# # total belanja
# belanja.jumlah_belanja(belanja)

#-----------------------------------------------------------------------------------#


# # soal no 2
# class mahasiswa():
#     total_mahasiswa = 0

#     def __init__(self, nama_mahasiswa, npm, prodi):
#         self.nama_mahasiswa = nama_mahasiswa
#         self.npm = npm
#         self.prodi = prodi
#         mahasiswa.total_mahasiswa += 1

#     def detail_mahasiswa(self):
#         print('Nama Mahasiswa :', self.nama_mahasiswa)
#         print('NPM :', self.npm)
#         print('Prodi :', self.prodi)

#     def jumlah_mahasiswa(self):
#         print('jumlah Mahasiswa', mahasiswa.total_mahasiswa)


# # membuat objek
# mahasiswa1 = mahasiswa('Dewi Ratnasari', 123456789, 'Sains Data')
# mahasiswa2 = mahasiswa('Budi Susanto', 345678901, 'Sains Data')
# mahasiswa3 = mahasiswa('Dewi Kartika', 345678901, 'Sains Data')
# mahasiswa4 = mahasiswa('Muhamad David', 456789012, 'Bisnis Digital')
# mahasiswa5 = mahasiswa('Christian Bambang', 567890123, 'Bisnis Digital')
# mahasiswa6 = mahasiswa('Sandra Kusumawati', 678901234, 'Bisnis Digital')

# # pemanggilan detail mahasiswa
# mahasiswa1.detail_mahasiswa()
# mahasiswa2.detail_mahasiswa()
# mahasiswa3.detail_mahasiswa()
# mahasiswa4.detail_mahasiswa()
# mahasiswa5.detail_mahasiswa()
# mahasiswa6.detail_mahasiswa()
# # total mahasiswa
# mahasiswa.jumlah_mahasiswa(mahasiswa)


# ------------------------------------------------------------------------------

# # soal no 3

# # class
# class kebutuhan():
#     total_kebutuhan = 0

#     def __init__(self, nama, tipe):
#         self.nama = nama
#         self.tipe = tipe
#         kebutuhan.total_kebutuhan += 1

#     def detail_kebutuhan(self):
#         print('Nama Kebutuhan :', self.nama)
#         print('Tipe kebutuhan :', self.tipe)

#     def jumlah_kebutuhan(self):
#         print('Banyaknya Kebutuhan Saya : ', kebutuhan.total_kebutuhan)


# # objek
# kebutuhan1 = kebutuhan('Makanan', 'Prioritas')
# kebutuhan2 = kebutuhan('Baju', 'Penting tapi bukan prioritas')
# kebutuhan3 = kebutuhan('Permen', 'Tidak penting dan bukan prioritas')

# # mengakses variabek objek
# kebutuhan1.detail_kebutuhan()
# kebutuhan2.detail_kebutuhan()
# kebutuhan3.detail_kebutuhan()

# # total kebutuhan
# kebutuhan.jumlah_kebutuhan(kebutuhan)

# # ------------------------------------------------------------------------------

# # soal no 4
# class menu():
#     jumlah_menu = 0

#     def __init__(self, nama, asal, peminat):
#         self.nama = nama
#         self.asal = asal
#         self.peminat = peminat
#         menu.jumlah_menu += 1

#     def banyak_menu(self):
#         print('Banyak menu yang tersedia:', menu.jumlah_menu)

#     def detail_menu(self):
#         print('Nama menu :', self.nama)
#         print('Asal Menu :', self.asal)
#         print('Banyaknya Peminat menu :', self.peminat)


# # method
# c1 = menu('Nasi padang', 'Padang', 'Banyak')
# c2 = menu('Rendang', 'Padang', 'Banyak')

# # fungsi
# c1.detail_menu()
# c2.detail_menu()

# menu.banyak_menu(menu)

# # ------------------------------------------------------------------------------

# class produk():
#     jumlah_produk = 0

#     def __init__(self, nama, harga):
#         self.nama = nama
#         self.harga = harga
#         produk.jumlah_produk += 1

#     def berapa_jumlah(self):
#         print('Totak porduk :', produk.jumlah_produk)

#     def detail_produk(self):
#         print('Nama:', self.nama)
#         print('Harga:', self.harga)
#         print()


# produk1 = produk('Tissue', 2000)
# produk2 = produk('air minereral', 3000)
# produk3 = produk('Roti', 2000)

# produk1.detail_produk()
# produk2.detail_produk()
# produk3.detail_produk()

# produk.berapa_jumlah(produk)


# # ------------------------------------------------------------------------------

# # soal no 6
# class kota():
#     def __init__(self, kota, bahasa, nama, musik):
#         self.kota = kota
#         self.bahasa = bahasa
#         self.nama = nama
#         self.musik = musik

#     def detail_kota(self):
#         print('ibu kota Jawa Barat:', self.kota)
#         print('Bahasa Daerah :', self.bahasa)
#         print('Nama Gubernur :', self.nama)
#         print('Alat musik :', self.musik)


# # method
# kota1 = kota('Bandung', 'Sunda', 'Ridwan kamil', 'Angklung')
# # fungsi
# kota1.detail_kota()

# # ------------------------------------------------------------------------------
# # soal no 7
# class hp():
#     def __init__(self, nama, storage):
#         self.nama = nama
#         self.storage = storage
#         self.harga = 10000
#         self.brand = 'SAMSUNG'

#     def detail_hp(self):
#         print('Brand Hp:', self.brand)
#         print('Harga:', self.harga)
#         print('Nama Pemilik :', self.nama)
#         print('Storage :', self.storage)


# # method
# cos1 = hp('FAJAR', '6GB')
# # fungsi
# cos1.detail_hp()

# # ------------------------------------------------------------------------------
# # SOAL NO 9
# class band:
#     def __init__(self, nama, gengre, asal, label, personil, top):
#         self.nama = nama
#         self.gengre = gengre
#         self.asal = asal
#         self.label = label
#         self.personil = personil
#         self.top = top


# band1 = band('Rocket Rockers', 'Indonesian Indie', 'Bandung',
#              'Sony Music Indonesia', 'Aska, Ozom, Bisma', ' Ingin Hilang Ingatan')

# print('Nama Band =', band1.nama)
# print('Gengre =', band1.gengre)
# print('Asal =', band1.asal)
# print('Label =', band1.label)
# print('Personil =', band1.personil)
# print('Top Hits Song =', band1.top)

# # ------------------------------------------------------------------------------
# soal no 10

class JuicyLucy:
    def __init__(self, genre, label):
        self.genre = genre
        self.label = label
        self.sexo = ' Zam Zam Y.M'
        self.vokalis = 'Julian Kaisar'
        self.gitar = 'Denis Ligia'


band = JuicyLucy('Indonesia pop', 'E-Motion Entertainment')
print('Gengre =', band.genre)
print('Label =', band.label)
print('Saxophonis =', band.sexo)
print('Vokalis =', band.vokalis)
print('Gitaris =', band.gitar)
