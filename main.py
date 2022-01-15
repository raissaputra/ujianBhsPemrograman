from view.view_nilai import *
from view.input_nilai import *
title()
while True:
    pilihan = input("Pilih Menu: ")
    if pilihan.lower() == 'k':
        print("Terimakasih, sudah mencoba")
        ext = input("Tekan ENTER untuk keluar")
        if ext == '':
            break
        else:
            break
    elif pilihan.lower() == 'l':
        cetak()

    elif pilihan.lower() == 't':
        inputan()

    elif pilihan.lower() == 'u':
        ubah()

    elif pilihan.lower() == 'c':
        cari_data()

    elif pilihan.lower() == 'h':
        hapus()
    else:
        wrong()
