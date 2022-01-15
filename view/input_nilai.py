from model.daftar_nilai import *


def inputan():
    while (True):
        nama = input("NAMA   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print('Harus Angka')
        except ValueError:
            print('Harus Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS  : "))
            if tugas == '':
                print('Harus Angka')
        except ValueError:
            print('Harus Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Harus Angka')
        except ValueError:
            print('Harus Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                print('Harus Angka')
        except ValueError:
            print('Harus Angka')
        else:
            break
    tambah_kontak(nama, nim, tugas, uts, uas)
    print("-"*65)
    print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))


def ubah():
    from model.daftar_nilai import ubah_kontak
    ubah_kontak(nama=input("Masukan nama baru untuk ubah data : "))


def hapus():
    from model.daftar_nilai import hapus
    hapus(nama=input("Masukan nama yang akan di hapus : "))
    print(" (T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar ".center(65))


def cari_data():
    from model.daftar_nilai import cari_data
    cari_data(nama=input("Masukan nama yang di cari : "))
