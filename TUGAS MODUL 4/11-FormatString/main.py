# format String
#katakunci f

# contoh generic
# string
nama = "Amad Dialo"
format_str = f"Hallo {nama}"
print(format_str)
print("Hallo",nama)

# boolean 
boolean = False
format_str = f"boolean = {boolean}"
print(format)

# angka
angka = 2005.5
format_str = f"an"

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal 
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus :+2f}"

print(format_minus)
print(format_plus)

# format persen 
persentase = 0.045
format_persen = f"persen = {persentase}"
print(format_persen)
