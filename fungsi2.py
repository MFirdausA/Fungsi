#variabel global

nama = "Hendri"
versi = "17.0"

def help():
    #variabel lokal
    nama = "ableh"
    versi = "16.0"
    print("Nama: %s" % nama)
    print("versi: %s" % versi)

#mengakses variabel
print("Nama: %s" % nama)
print("versi: %s" % versi)

#memanggil fungsi help
help()