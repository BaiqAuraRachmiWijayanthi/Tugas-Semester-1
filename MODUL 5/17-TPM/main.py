# program Menghitung Diskon Belanja 

# Input : Apakah pelanggan memiliki kartu member 
is_member = input("Apakah member? (ya/tidak): ").lower()
total_belanja = int(input("input total belanja (Rp): "))

# Inisialisasi Variable Diskon
diskon_persen = 0

# Logika Menentukan Diskon 
if is_member == "ya":
    if total_belanja > 500000:
        diskon_persen = 20
    else:
        diskon_persen = 10
else:
    if total_belanja > 500000:
        diskon_persen = 5

# Menghitung total diskon dan total bayar 
diskon = (diskon_persen / 100) * total_belanja
total_bayar = total_belanja - diskon 

# output hasil
print("\nOutput:")
print(f"Total Belanja : Rp {550,000:,}")
print(f"Diskon persen : {20}%")
print(f"Diskon : Rp { 110,000:,}")
print(f"Bayar : Rp {440,000:,}")