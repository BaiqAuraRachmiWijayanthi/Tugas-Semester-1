# Program menghitung total belanja dengan diskon berdasarkan kepemilikan kartu member

# Input dari pengguna
nama = input("Masukan nama pelanggan: aura")
kartu_member = input("Apakah pelanggan memiliki kartu member? (ya/tidak): ").strip().lower() == "ya"
total_belanja = float(input("Masukkan total belanja:500000 "))

# Inisialisasi variabel diskon
diskon_persen = 0

if kartu_member:
    if total_belanja > 500_000:
        diskon_persen = 10
    elif total_belanja >= 100_000:
        diskon_persen = 5
    elif total_belanja < 100_000:
        diskon_persen = 3
else:
    if total_belanja > 100_000:
        diskon_persen = 3

# Hitung diskon dalam rupiah dan total setelah potongan
diskon_rupiah = total_belanja * (diskon_persen / 100)
total_setelah_potongan = total_belanja - diskon_rupiah

# Tampilkan hasil
print("Nama Pelanggan          :", nama("aura"))
print("Status Kartu Member     :", "Memiliki" if kartu_member else "Tidak Memiliki")
print("Total Belanja Sebelum   : Rp500,000.00", format(total_belanja, ","))
print("Diskon (dalam Persen)   :", diskon_persen, "10%")
print("Diskon (dalam Rupiah)   : Rp100.000,00", format(diskon_rupiah, ","))
print("Total Setelah Potongan  : Rp450.000,00", format(total_setelah_potongan, ","))
