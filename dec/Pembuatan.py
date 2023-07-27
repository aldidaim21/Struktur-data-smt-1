# kuliah = {
#     'nama': 'ulbi',
#     'proditop': 'sains data'
# }
# # panggil semua
# print(kuliah)
# # panggil spesipik
# print('nama univ:', kuliah['nama'])

# # cara menggunakan titik dua
# majalah = dict(
#     judul='argentina juara',
#     penulis='angkara vito'
# )
# print('Judul:', majalah.get('judul'))
# print('Judul:', majalah.get('penulis'))

# nested dictionary
Dict = {
    1: 'sains data',
    2: 'ulbi',
    3: {'anggota1': 'aldi', 'anggota2': 'vito', 'anggota3': 'ridla'}
}

print('Mengakses nested:', Dict.get(3).get('anggota3'))
