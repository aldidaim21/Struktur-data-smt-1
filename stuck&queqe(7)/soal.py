# #1 - 3
# s = [90, 100, 250, 600, 700, 1000, 2000]
# # 1
# s.append(5000)
# print("data setelah ditambahkan : ", s)
# # 2
# s.append(10000)
# print("data setelah ditambahkan :", s)
# # 3
# s.pop()
# print('data sekarang :', s)


# #4 - 6
# s1 = [11, 44, 56, 98, 143, 234, 167]
# # 4
# s1.pop()
# print('data :', s1)
# # 5
# s1.append(475)
# print("data sekarang :", s1)
# # 6
# s1.pop()
# print('data sekarang :', s1)
# s1.pop()
# print("data akhir :", s1)

# 7

# LIST Jumlah Buku tanggal 09 januari 2022
buku = [1, 2, 3, 4, 5, 6]
print("Jumlah Buku Awal:", buku)

# Penambahan Buku pada 30 april
buku.append(7)
print("Penambahan Buku", 7)
print("Jumlah Buku : ", buku)

# Penambahan Buku pada 30 april
buku.append(8)
print("Penambahan Buku", 8)
print("Jumlah Buku : ", buku)

# Penambahan Buku pada 30 april
buku.append(10)
print("Penambahan Buku", 10)
print("Jumlah Buku : ", buku)

# Pengambilan Buku oleh Pelanggan
buku.pop()
print("Pengambilan Buku oleh Pelanggan", buku)
print("Jumlah Buku : ", buku)

# 8

# # list sepeda motor
# sepedamotor = [1, 2, 3]
# print("Jumlah Sepeda Motor :", sepedamotor)

# # Penambahan Sepeda Motor Baru yang akan disimpan oleh teman mas wahyu
# sepedamotor.append(4)
# print("Penambahan Sepeda motor menjadi", 4)
# print("Jumlah Sepeda Motor : ", sepedamotor)

# # Pengambilan Sepeda Motor ole teman mas wahyu
# sepedamotor.pop()
# print("Pengambilan Sepeda Motor", sepedamotor)
# print("Jumlah Sepeda Motor : ", sepedamotor)

# # Pengambilan Sepeda Motor oleh adik mas wahyu
# sepedamotor.pop()
# print("Pengambilan Sepeda Motor ", sepedamotor)
# print("Jumlah Sepeda Motor : ", sepedamotor)


# # B Queue

# from collections import deque
# from collections import deque  # modul for queue
# antrian = deque([10, 11, 12, 13, 14])

# # 1
# antrian.append(15)
# print('data antrian masuk : 15')
# print('data antrian : ', antrian)

# # 2

# # keluar
# keluar = antrian.popleft()
# print('data keluar : ', keluar)
# print('data antrian sekarang : ', antrian)
# # keluar
# keluar = antrian.popleft()
# print('data keluar : ', keluar)
# print('data antrian sekarang : ', antrian)

# # masum
# antrian.append(16)
# print('data antrian masuk : 16')
# print('data antrian sekarang :', antrian)


# # Jumlah Antrian Pagi Jam 10.00 WIB
# antrian = deque([1, 2, 3, 4, 5])

# print("Jumlah Antrian : ", antrian)

# # Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.20 WIB
# antrian.append(6)
# print("Nasabah ke ", 6)
# print("Jumlah Antrian :", antrian)

# # Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.30 WIB
# antrian.append(7)
# print("Nasabah ke ", 7)
# print("Jumlah Antrian :", antrian)

# # Antrian Bertambah / Kedatangan Nasabah Baru pada Pagi Jam 10.30 WIB
# antrian.append(8)
# print("Nasabah ke ", 8)
# print("Jumlah Antrian :", antrian)

# # Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.35 WIB
# out = antrian.popleft()
# print("Nasabah yang keluar", out)
# print("Jumlah Nasabah Sekarang :", antrian)

# # Antrian Berkurang / Nomor Antrian telah dipanggil Pada 10.40 WIB
# out = antrian.popleft()
# print("Nasabah yang keluar", out)
# print("Jumlah Nasabah Sekarang :", antrian)
