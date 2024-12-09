# percabangann 
# percabangann 1 kondisi 

# struktur percabangan 
"""
    1.if -nya
    2.kondisinya,statmen yang harus terpenuhi agar aksi dijalankan 
    3.Aksinya
"""


nama = input("masukan nama anda!")

# percabangan inline
# if <kondisi> : <aksi>
#if nama == "adam": print("selamat datang")
#print("Terimakasih") # bukan aksi

# percabangan dengan indentitas
if nama == "adam" :
    print("selamat datang") # aksi
    print("selamat belajar") # aksi
print("Terimakasih") # bukan aksi

# percabangan dengan Else Statement
if nama == "adam" :
     print("selamat datang")
else:
     print("anda bukan adam")

print("program berakhir")           
