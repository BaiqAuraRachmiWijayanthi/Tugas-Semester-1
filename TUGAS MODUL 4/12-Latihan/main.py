# import fungsi date

from datetime import date

# Input data tanggal lahir dari pengguna
tanggal = 23
bulan = 4
tahun = 2006

# Konversi input ke tipe data date
tanggal_lahir = date(tahun, bulan, tanggal)
print(f"tanggal_lahir = {tanggal_lahir}")

# Mendapatkan tanggal hari ini
hari_ini = date.today()
print(f"hari_ini = {hari_ini}")

# Menghitung usia dalam tahun
usia_tahun = hari_ini.year - tanggal_lahir.year
# Menghitung usia dalam bulan
usia_bulan = hari_ini.month - tanggal_lahir.month

# Periksa apakah ulang tahun belum lewat
if (hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day):
    usia_tahun -= 1
    usia_bulan += 12  # Tambahkan 12 bulan karena tahun sebelumnya

# Pastikan bulan dihitung dengan benar (jika usia_bulan negatif)
if hari_ini.day < tanggal_lahir.day:
    usia_bulan -= 1

# Menampilkan hasil
print(f"Usia Anda: {usia_tahun} tahun {usia_bulan} bulan")