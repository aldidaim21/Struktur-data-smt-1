# #1
# class motor:

#     def __init__(self, brand, harga, warna):
#         self.brand = brand
#         self.harga = harga
#         self.warna = warna


# # kendaraan1
# kendaraan1 = motor('KAWASAKI', 500, 'Merah')
# print(kendaraan1.brand)
# print(kendaraan1.harga)
# print(kendaraan1.warna)

# #3
# class Mobil:
#     def __init__(self, brand, harga):
#         self.brand = brand
#         self.harga = harga
#         self.kondisi = 'baru'
#         self.pemakaian = '3 tahun'


# kendaraan1 = Mobil('TOYOTA', 500)
# print('Brand =', kendaraan1.brand)
# print('Price =', kendaraan1.harga)
# print('Kondisi =', kendaraan1.kondisi)
# print('Pemakaian =', kendaraan1.pemakaian)

# # 4
# class Buah:

#     penjual = 'Pak Imron'  # ini class object attribute

#     def __init__(self, nama_buah, harga):
#         self.nama_buah = nama_buah
#         self.harga = harga

#     jenis_buah = 'Pisang Ambon'  # ini class object attribute


# fruit1 = Buah('Pisang', 10000)
# print('Nama buah =', fruit1.nama_buah)
# print('Harga buah =', fruit1.harga)
# print('Nama penjual buah =', fruit1.penjual)
# print('Jenis Pisang =', fruit1.jenis_buah)


# 5
class Karyawan():
    jumlah_karyawan = 0

    def __init__(self, nama, jobdesk, lama_bekerja):
        self.nama = nama
        self.jobdesk = jobdesk
        self.lama_bekerja = lama_bekerja
        Karyawan.jumlah_karyawan += 1

    def total_karyawan(self):
        print('Total Karyawan =', Karyawan.jumlah_karyawan)

    def detail_karyawan(self):
        print('Nama karyawan :', self.nama)
        print('Jobdesk karyawan :', self.jobdesk)
        print('Lama bekerja :', self.lama_bekerja)


# membuat objek
karyawan1 = Karyawan('Adi', 'salesman', '2 bulan')
karyawan2 = Karyawan('Susi', 'kadiv HR', '2 tahun')
karyawan3 = Karyawan('Budi', 'Marketing', '10 bulan')
karyawan4 = Karyawan('Tuti', 'Manager', '4 tahun')
karyawan5 = Karyawan('Santoso', 'Sekretaris', '5 tahun')
# mengakses attribut objek
karyawan1.detail_karyawan()
karyawan2.detail_karyawan()
karyawan3.detail_karyawan()
karyawan4.detail_karyawan()
karyawan5.detail_karyawan()
Karyawan.total_karyawan(Karyawan)
