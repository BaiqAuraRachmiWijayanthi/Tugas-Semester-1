# rom datetime import date

# fungsi untuk menghitung usia
def hitung_usia(tanggal,bulan,tahun):
    # mendapatkan tanggal hari ini 
    today = dt.today()

    # Membuat objek tanggal lahir dari input
    tanggal_lahir = dt (tahun, bulan, tanggal)

    # Menghitung selisih tahun, bulan, dan hari
    usia = today.year - tanggal_lahir.year

    # Menyesuaikan jika belum melewati ulang tahun tahun ini
    if today.month < tanggal_lahir.month or (today.month == tanggal_lahir.month and today.day < tanggal_lahir.day):
        usia -= 1

    return usia, tanggal_lahir

# Input dari pengguna
tanggal = int(input("Masukkan Tanggal Lahir (1-31): "))
bulan = int(input("Masukkan Bulan Lahir (1-12): "))
tahun = int(input("Masukkan Tahun Lahir: "))

# Menghitung usia
usia, tanggal_lahir = hitung_usia(tanggal, bulan, tahun)

# Menampilkan hasil
print(f"Tanggal Lahir Anda: {tanggal_lahir.strftime('%d-%m-%Y')}")
print(f"Usia Anda: {usia} tahun")

# import fungsi date

import datetime as dt


tanggal = 20
bulan = 11
tahun = 2010

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(tanggal_lahir)
hari_ini = dt.date.today()
print(hari_ini)

usia = hari_ini - tanggal_lahir
print(usia) 

# hitung usia dalam tahun dan bulan
usia_tahun = hari_ini.year - tanggal_lahir.year
usia_bulan = hari_ini.month - tanggal_lahir.month

# cetak usia
print(f"usia: {usia_tahun}tahun, {usia_bulan} bulan")

tanggal = int(input)("masukkan tanggal lahir:")
tanggal = int(input)("masukkan bulan lahir:")
tanggal = int(input)("masukkan tahun lahir:")