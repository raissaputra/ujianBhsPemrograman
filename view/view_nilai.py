from model.daftar_nilai import kontak
from view.input_nilai import cari_data


def title():
    print("="*65)
    print("PROGRAM INPUT DATA NILAI".center(65))
    print("="*65)
    print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))
    print("="*65)


def wrong():
    print("="*65)
    print("| Pilih menu yang tersedia |".center(65))
    print("="*65)
    print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))


def cetak():
    print("="*65)
    print("PROGRAM INPUT DATA NILAI".center(65))
    print("="*65)
    print("| NO |     NAMA      |   NIM   | TUGAS |  UTS  |  UAS  | AKHIR  |")
    print("|====|===============|=========|=======|=======|=======|=========")
    no = 1
    for tabel in kontak.values():
        print("|{0:3} |{1:15}|{2:9}| {3:5} | {4:5} | {5:5} | {6:6} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        no += 1
    print("="*65)
    print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))


def cari_data():
    cari_data()
    print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))
