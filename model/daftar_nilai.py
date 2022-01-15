kontak = {}


def tambah_kontak(nama, nim, tugas, uts, uas):
    akhir = round((float(tugas) * 0.3) + (float(uts)
                  * 0.35) + (float(uas) * 0.35), 2)
    kontak[nama] = nama, nim, tugas, uts, uas, akhir


def ubah_kontak(nama):
    if nama in kontak.keys():
        del kontak[nama]
        print("\n===Masukan Perubahan Data===")
        from view.input_nilai import inputan
        inputan()
    else:
        print("-"*40)
        print("| Data {} tidak ditemukan |".format(nama))
        print("-"*40)
        print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))


def cari_data(nama):
    if nama in kontak.keys():
        print("\n=====================================================================")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|=================|==================|=======|=======|===============|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(
            nama, kontak[nama][1], kontak[nama][2], kontak[nama][3], kontak[nama][4], kontak[nama][5]))
        print("======================================================================")
    else:
        print("-"*40)
        print("| Data {} tidak ditemukan |".format(nama))
        print("-"*40)


def hapus(nama):
    if nama in kontak.keys():
        del kontak[nama]
        return True
    else:
        print("-"*40)
        print("| Data {} tidak ditemukan |".format(nama))
        print("-"*40)
        return False
