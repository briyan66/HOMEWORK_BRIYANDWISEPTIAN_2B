def tambah_data(data_barang,nama_barang, stok):
    data_barang[nama_barang] = stok
    print("Data barang berhasil ditambahkan")

def hapus_data(data_barang,nama_barang):
    if nama_barang in data_barang:
        del data_barang[nama_barang]
        print("Data barang dihapus.")
    else:
        print("Data barang tidak ada.")

def tampilkan_data(data_barang):
    if data_barang:
        print("Data Barang:")
        for nama_barang, stok in data_barang.items():
            print(f"{nama_barang}: {stok}")
    else:
        print("Tidak ada data barang.")

def hitung_jumlah_data(data_barang):
    return len(data_barang)


def cari_data_barang(data_barang,nama_barang):
    if nama_barang in data_barang:
        return nama_barang, data_barang[nama_barang]
    else:
        return None


def edit_data_barang(data_barang, nama_barang, stok_baru):
    if nama_barang in data_barang:
        data_barang[nama_barang] = stok_baru
        print(f"Stok barang '{nama_barang}' telah diperbarui menjadi {stok_baru}.")
    else:
        print(f"Barang '{nama_barang}' tidak ditemukan.")



def menu():
    data_barang = {}
    while True:
        print("\nPilihan Menu:")
        print("1. Tambah Data Barang")
        print("2. Hapus Data Barang")
        print("3. Tampilkan Data Barang")
        print("4. Hitung Jumlah Data")
        print("5. Pencarian Data")
        print("6. Edit Data")
        print("7. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7): ")

        if pilihan == '1':
            nama_barang = input("Masukkan nama barang: ")
            stok = input("Masukkan stok barang: ")
            tambah_data(data_barang, nama_barang, stok)
        elif pilihan == '2':
            nama_barang = input("Masukkan nama barang yang akan dihapus: ")
            hapus_data(data_barang, nama_barang)
        elif pilihan == '3':
            tampilkan_data(data_barang)
        elif pilihan == '4':
            jumlah_data = hitung_jumlah_data(data_barang)
            print(f"Jumlah data barang yang tersimpan: {jumlah_data}")
        elif pilihan == '5':
            nama_barang = input("Masukkan nama barang yang ingin dicari: ")
            hasil_pencarian = cari_data_barang(data_barang, nama_barang)
            if hasil_pencarian:
                print(f"Barang ditemukan: Nama Barang: {hasil_pencarian[0]}, Stok: {hasil_pencarian[1]}")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == '6':
            nama_barang = input("Masukkan nama barang yang ingin diedit: ")
            stok_baru = int(input("Masukkan stok baru: "))
            edit_data_barang(data_barang, nama_barang, stok_baru)
        elif pilihan == '7':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")