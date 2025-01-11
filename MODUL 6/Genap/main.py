print("SELAMAT DATANG DI NIAGA!")
nama = input("Masukkan nama anda:")
kartu_member = input("Apakah Anda punya kartu member? (ya/tidak): ").strip().lower()
belanja = float(input("Masukkan total belanja Anda (Rp): "))

# Variabel
diskon_persen = 0
diskon = 0

# Logika perhitungan diskon
if kartu_member == "ya":
    if belanja > 500000:
        diskon_persen = 0.1
    elif belanja >= 100000:
        diskon_persen = 0.05
else:
    if belanja > 100000:
        diskon_persen = 0.03

# Hitung nilai diskon
diskon = diskon_persen * belanja
total_bayar = belanja - diskon

# Output hasil
print("\n===== Detail Transaksi NIAGA =====")
print(f"Nama Pelanggan : {nama}")
print(f"Total Belanja : Rp{belanja:,.0f}")
print(f"Diskon Persen : {diskon_persen * 100:.0f}%")
print(f"Diskon        : Rp{diskon:,.0f}")
print(f"Bayar         : Rp{total_bayar:,.0f}")
