from datetime import date

# Fungsi untuk menghitung usia
def hitung_usia(tanggal, bulan, tahun):
    # Mendapatkan tanggal hari ini
    today = date.today()

    # Membuat objek tanggal lahir dari input
    tanggal_lahir = date(tahun, bulan, tanggal)

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