# Aprian Handayani
# Job Connector Data Science and Machine Learning
# Capstone project - Penjualan barang toko

katalog = {
            'Grup' : ["Seventeen", "Seventeen", "Seventeen", "Seventeen", "Seventeen",
                      "BTS", "BTS", "BTS", "BTS",
                      "NCT", "NCT", "NCT", "NCT",
                      "EXO", "EXO", "EXO", "EXO"],
            'Album' : ["Hitorijanai", "Hitorijanai", "Hitorijanai", "Heaven","Heaven",
                       "Proof", "Proof", "Butter", "Butter",
                       "Empathy", "Empathy", "Resonance", "Resonance",
                       "Exist", "Exist", "Exist", "Exist"],
            'Versi' : ["Type A", "Type B", "Type C", "AM 5:2", "PM 2:14",
                       "Standard", "Compact", "Cream", "Peaches",
                       "Dream", "Reality", "Past", "Future",
                       "E Ver", "X Ver", "O Ver", "Digipack"],
            'Harga' : [385000, 385000, 385000, 400000, 400000,
                       400000, 370000, 370000, 370000,
                       339000, 339000, 385000, 385000,
                       385000, 385000, 310000, 180000],
            'Stok' : [12, 10, 15, 20, 25,
                      22, 10, 19, 13,
                      15, 20, 17, 18,
                      15, 27, 22, 19]
};


def menu_utama():
    while True:
        pilihan_menu = input("""
=====================================================================
                    Selamat datang di Toko Album
=====================================================================
                                       
List Menu:
1. Menampilkan katalog
2. Menambah stock barang
3. Menghapus stock barang
4. Membeli barang
5. Mengupdate barang
6. Exit program
                    
Masukkan angka menu yang ingin dijalankan : """)

        if pilihan_menu == "1":
            tampilan_katalog()
        elif pilihan_menu == "2":
            tambah_katalog()
        elif pilihan_menu == "3":
            hapus_stock()
        elif pilihan_menu == '4':
            pembelian()
        elif pilihan_menu == '5':
            update()
        elif pilihan_menu == '6':
            print("=" * 69)
            print("\t Terima kasih telah berbelanja di toko kami ")
            print("=" * 69)
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1 - 6 yang telah disediakan")

def format_rupiah(angka):
    return "Rp {:,}".format(angka).replace(',', '.')

def tampilan_katalog():
    print('\n\t\t\tDaftar Katalog\n')
    print('| No |    Grup    |      Album      |    Versi   |    Harga   |  Stok  |')
    for i in range(len(katalog["Grup"])):
        print('| {0:<2} | {1:<10} | {2:<15} | {3:<10} | {4:<8} | {5:<6} |'.format(i+1, katalog["Grup"][i], katalog["Album"][i], katalog["Versi"][i], format_rupiah(katalog["Harga"][i]), katalog["Stok"][i]))

def print_temp(Grup, Album, Versi, Harga, Stok):
    print(f"Grup\t: {Grup}\nAlbum\t: {Album}\nVersi\t: {Versi}\nHarga\t: {Harga}\nStok\t: {Stok}")

def tambah_katalog():
    print("=" * 69)
    print('\t\t\tMenambah Stok Barang')
    print("=" * 69)
    # Grup
    while True:
        tambah_grup = input("\nMasukkan nama grup : ")
        if tambah_grup.isdigit():
            print("Nama grup tidak boleh hanya angka")
        else:
            break
            
    # Album
    while True:
        tambah_album = input("Masukkan nama album baru: ")
        if len(tambah_album) > 2:
            break
        else:
            print("Nama album minimal memiliki lebih dari 2 karakter") 
  
    # Versi
    while True:
        tambah_versi = input("Masukkan versi album: ")
        if len(tambah_versi) > 1:
             # Cek duplikasi
            duplikat = False
            for i in range(len(katalog['Versi'])):
                if katalog['Versi'][i] == tambah_versi:
                    duplikat = True
                    break
            if duplikat:
                print("Versi album ini sudah ada. Silakan masukkan versi lain.")
            else:
                break
        else:
            print("Nama versi minimal memiliki 1 karakter")
    # Harga
    while True:
        tambah_harga = input("Masukkan harga album: ")
        if not tambah_harga.isdigit() or int(tambah_harga) < 100000:
            print("Hanya menerima inputan berupa angka dan minimal harga 100.000 rupiah")
            continue
        tambah_harga = int(tambah_harga)
        break
    # Stok
    while True:
        tambah_stok = input("Masukkan jumlah stok album: ")
        if not tambah_stok.isdigit() or int(tambah_stok) <= 0:
            print("Stok harus bilangan bulat positif dan lebih dari 0")
            continue
        tambah_stok = int(tambah_stok)
        break
    # Preview data dan verifikasi
    while True:
        print("=" * 69)
        print("\t\t   Preview Stok yang ditambahkan")
        print("=" * 69)
        print_temp(tambah_grup, tambah_album, tambah_versi, tambah_harga, tambah_stok)
        verifikasi = input("\nSimpan data yang ditambahkan (Y/N) : ").upper()
        if verifikasi == "Y":
            tambah_list = [tambah_grup, tambah_album, tambah_versi, tambah_harga, tambah_stok]
            for key, value in zip(katalog.keys(), tambah_list):
                katalog[key].append(value)
            print("=" * 27)
            print(" Data berhasil ditambahkan ")
            print("=" * 27)
            tampilan_katalog()
        else:
            tambah_list = []
            print("=" * 21)
            print(" Data tidak disimpan ")
            print("=" * 21)
        break
        
def hapus_stock():
    print("=" * 69)
    print('\t\t\tMenghapus Stok Barang')
    print("=" * 69)
    tampilan_katalog()
    while True:
        hapus_nomor = input("\nMasukkan nomor album yang akan dihapus: ")
        if not hapus_nomor.isdigit():
            print("Hanya menerima angka yang tersedia pada kolom nomor")
            continue
        else:
            hapus_nomor = int(hapus_nomor)
            if 1 <= hapus_nomor <= len(katalog['Album']):
                index = hapus_nomor - 1
                for key in katalog.keys():
                    katalog[key].pop(index)
                print(f"Data nomor {hapus_nomor} berhasil dihapus!")
                tampilan_katalog()
                break
            else:
                print("Nomor album tidak valid")
            continue
        break

def update():
    print("=" * 69)
    print('\t\t\t Memperbarui Stok Barang')
    print("=" * 69)
    tampilan_katalog()
    perbarui_nomor = int(input("\nMasukkan nomor album yang akan diperbarui: "))
    if 1 <= perbarui_nomor <= len(katalog['Album']):
        index = perbarui_nomor - 1
        print("Masukkan data baru (kosongkan jika tidak ingin mengubah)")
        # Grup update
        while True:
            grup_update = input(f"Grup ({katalog['Grup'][index]}): ")
            if grup_update.isdigit():
                print("Nama grup tidak boleh hanya berupa angka")
            else:
                break
        # Album update
        album_update = input(f"Album ({katalog['Album'][index]}): ")
        # Versi update
        versi_update = input(f"Versi ({katalog['Versi'][index]}): ")
        # Harga update
        harga_update = input(f"Harga ({katalog['Harga'][index]}): ")
        # Stok update
        stok_update = input(f"Stok ({katalog['Stok'][index]}): ")

        if grup_update:
            katalog["Grup"][index] = grup_update
        if album_update:
            katalog['Album'][index] = album_update
        if versi_update:
            katalog['Versi'][index] = versi_update
        if harga_update:
            katalog['Harga'][index] = int(harga_update)
        if stok_update:
            katalog['Stok'][index] = int(stok_update)
        
        print(f"Album nomor {perbarui_nomor} berhasil diperbarui!")
        tampilan_katalog()
    else:
        print("Nomor album tidak valid")

def tampilan_keranjang():
    if not keranjang:
        print("Keranjang belanja kosong.")
    else:
        print("=" * 69)
        print('\t\t\tKeranjang Belanja:')
        print("=" * 69)
        print('| No |    Album     |   Versi    |   Harga    | Jumlah |    Total     |')
        total_semua = 0
        for i, item in enumerate(keranjang):
            total_semua += item["Total"]
            print('| {0:<2} | {1:<12} | {2:<10} | {3:<10} | {4:<6} | {5:<12} |'.format(
                i+1, item['Album'], item['Versi'], format_rupiah(item['Harga']), item['Jumlah'], format_rupiah(item['Total'])))
        print(f'\nTotal harga semua barang di keranjang: {format_rupiah(total_semua)}')

keranjang = []
def pembelian():
    print("=" * 69)
    print('\t\t\tPembelian Barang')
    print("=" * 69)
    while True:
        tampilan_katalog()
        nomor_album = input("\nMasukkan nomor album yang ingin dibeli: ")
        if not nomor_album.isdigit():
            print("Nomor album tidak valid")
            continue
        nomor_album = int(nomor_album)
        if 1 <= nomor_album <= len(katalog['Album']):
            index = nomor_album - 1
            jumlah_beli = int(input(f"\nMasukkan jumlah yang ingin dibeli (Stok tersedia: {katalog['Stok'][index]}): "))
            
            if 0 < jumlah_beli <= katalog['Stok'][index]:
                total_harga = jumlah_beli * katalog['Harga'][index]
                katalog['Stok'][index] -= jumlah_beli
                keranjang.append({
                    "Album": katalog["Album"][index],
                    "Versi": katalog["Versi"][index],
                    "Harga": katalog["Harga"][index],
                    "Jumlah": jumlah_beli,
                    "Total": total_harga
                })
                tampilan_keranjang()
                while True: 
                    tambah_belanja = input("\nApakah ada lagi yang ingin dibeli? y/n : ").lower()
                    if tambah_belanja == "y":
                        break
                    elif tambah_belanja == "n":
                        while True:
                            total_harga = sum(item['Total'] for item in keranjang)
                            bayar = int(input("Silakan masukkan jumlah uang: "))
                            kurang = total_harga - bayar
                            kembali = bayar - total_harga
                            if bayar < total_harga:
                                print(f"Uang anda kurang sebesar {format_rupiah(kurang)}")
                            else:
                                print(f"Terima kasih. \nUang kembali anda {format_rupiah(kembali)}" if kembali > 0 else "Terima kasih")
                                keranjang.clear()
                                return
                    else:
                        print("\nHanya menerima inputan y atau n")
            else:
                print("Jumlah yang ingin dibeli tidak valid atau stok tidak mencukupi.")
        else:
            print("Nomor album tidak valid")

menu_utama()