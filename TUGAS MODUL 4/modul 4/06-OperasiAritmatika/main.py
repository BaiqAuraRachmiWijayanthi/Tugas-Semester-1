# operasi aritmatika

a = 10
b = 3

# operasi perjumlahan (tambah)
print("====TAMBAH====")
Hasil = a + b
print(a,"+", b , "=", Hasil)

# operasi pengurangan (KURANG)
print("====KURANG====")
Hasil = a - b
print(a,"-", b , "=", Hasil)

# operasi perkalian (KALI)
print("====kali====")
Hasil = a * b
print(a,"*", b , "=", Hasil)

# operasi pembagian (BAGI)
print("====BAGI====")
Hasil = a / b
print(a,"/", b , "=", Hasil)

# opersai pemangkatan (EXPONENTIAL)
print("====EXPONENTIAL===")
Hasil = a ** b
print(a,"**", b , "=", Hasil)

# operasi sisa pembagian (MODULUS)
print("====MODULUS====")
Hasil = a % b
print(a,"%", b , "=", Hasil)

# operasi floor devision (DEVISION)
print("====FLOOR DEVISION====")
Hasil = a // b
print(a,"//", b , "=", Hasil)

# prioritas perhitungan (operasi)
"""
 1.()
 2. perkalian, pembagian dll * / ** % //
 3. penjumlahan dan pengurangan + -
"""

x = 3
y = 4
z = 2

Hasil = x**z * (y + x) / z - z % y // x
print(x, "**" ,z,"*" ,y, "+" ,x, "/" ,z, "-" ,z, "%" ,y, "//" ,x, "=", Hasil)

Hasil = x + y * z
print(x, "+", y, "*" ,z)
Hasil = (x + y) * z
print("(",x, "+", y,")", "*", z, "=", Hasil)