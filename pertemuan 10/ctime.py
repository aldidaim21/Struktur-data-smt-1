import time
import datetime


# # time time()
# a = time.time()

# print(a)


# # ctime
# print("menggunakan ctime ")
# waktu = 1673853056.9091797
# hasil = time.ctime(waktu)
# print(hasil)


# # localtime
# print("menggunakan local time")
# localtime = time.localtime()
# print("waktu saat ini", type(localtime))

# # pake parameter
# waktu1 = time.localtime()
# waktu2 = time.strftime("%m:%a:%y,%H:%M:%y", waktu1)
# print(waktu2)

# # pake date time
# print("/n menggunakan paramater")
# waktu3 = datetime.datetime.now()
# print(waktu3)


# # menggunakan parameter setekah date time
# waktu4 = datetime.datetime.now()
# print(waktu4.year)
# print(waktu4.month)
# print(waktu4.day)
# print(waktu4.hour)
# print(waktu4.minute)
# print(waktu4.second)

# menghitung hari
tanggallahir = datetime.datetime(2003, 4, 21, 10, 20, 10)
umur = datetime.datetime.now()
tua = umur.year - tanggallahir.year
tuabulan = umur.month - tanggallahir.month
tuahari = tanggallahir.day - umur.day
print("umur saya", tua, "tahun")
print(tuabulan, "bulan")
print(tuahari, "hari")

# # waktu pake slesh
tuatua = (umur-tanggallahir).days//30
print("waktu yang saya lalui", tuatua, "bulan")
