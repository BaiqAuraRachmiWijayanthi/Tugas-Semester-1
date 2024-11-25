# Mengenal String
# string = kumpulan karakter

data = "ini adalah string" # 21 karakter
print(data)
print(type(data))

# 1.cara membuat string 
"""
 1.dengan mengguanakan single quote '...'
 2. dengan menggunakan double quote "..."
"""

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print("ini hari ju'mat")
print("nama saya ma'ruf")

# 2.menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')

print('c:\\user\\adam')

# tab(\t)
print("ronaldo\t\tmessi")
print("MU\t\tjuara")

# backspce (\b)
print("mu\bjuara")

# newline (\n, \r)
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carrige return

# raw string
print(r"c:\user\adam")