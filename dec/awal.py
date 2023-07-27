# cara pertama
majalah = {
    "judul": "ARGENTINA JUARA",
    "penulis": "Angkara Vito",
    "share_count": {
        "facebook": 0,
        "twitter": 2
    }
}
# errorr
print('Instagram share:', majalah['instagram'])
# ga error
print('Instagram share:', majalah.get('instagram', 0))

# # cara kedua
# majalah1 = dict(
#     judul="ARGENTINA JUARA",
#     penulis="Angkara",
# )

# cara kurung siku
majalah = {
    "judul": "ARGENTINA JUARA",
    "penulis": "Angkara"
}
