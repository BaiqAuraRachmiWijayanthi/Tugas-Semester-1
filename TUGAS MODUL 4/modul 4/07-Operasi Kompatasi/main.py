# operasi komparasi / perbandingan

# hasil operasi selalau bertipe boolean (TRUE/ FALSE)

# <,>,==,!=,>=,<=,is, dan is not

a = 4
b = 2

# lebih besar dari (>)
print("====Lebih Besar Dari (>)====")
hasil = a > 3 # TRUE
print(a, ">", 3, "=", hasil)
hasil = b > 3 # FALSE
print(b, ">", 3, "=", hasil)
hasil = b > 2 # FALSE
print(b, ">", 2, "=", hasil)

# kurang dari (<)
print("====Kurang Dari (<)====")
hasil = a < 3 # FALSE
print(a, "<", 3, "=", hasil)
hasil = b < 3 # TRUE
print(b, "<", 3, "=", hasil)
hasil = b < 2 # FALSE
print(b, "<", 2, "=", hasil)

# kurang dari sama dengan (<=)
print("====Kurang Dari Sama Dengan (<=)====")
hasil = a <= 3 # TRUE
print(a, "<=", 3, "=", hasil)
hasil = b <= 3 # FALSE
print(b, "<=", 3, "=", hasil)
hasil = b <= 2 # TRUE
print(b, "<=", 2, "=", hasil)

# lebih besar dari sama dengan (>=)
print("====Lebih Besar Dari Sama Dengan (<=)====")
hasil = a >= 3 # TRUE
print(a, ">=", 3, "=", hasil)
hasil = b >= 3 # FALSE
print(b, ">=", 3, "=", hasil)
hasil = b >= 2 # TRUE
print(b, ">=", 2, "=", hasil)

# sama dengan (==)
print("====Sama Dengan (==)====")
hasil = a == 3 # FALSE
print(a, "==", 3, "=", hasil)
hasil = a == 4 # TRUE
print(a, "==", 4, "=", hasil)

# tidak sama dengan (!=)
print("====Tidak Sama Dengan (!=)====")
hasil = a != 3 # TRUE
print(a, "!=", 3, "=", hasil)
hasil = a != 4 # FALSE
print(a, "!=", 4, "=", hasil)

# is sebagai komparasi 
print("====objek identitiy")
x = 5
y = 5
hasil = x is y # TRUE
print(x, "is", y, "=", hasil)
print("nilai x = ", x, "id = ", hex (id(x)))
print("nilai x = ", y, "id = ", hex (id(y)))

# is not sebagai komparasi 
print("====objek identitiy")
x = 5
y = 6
hasil = x is not y # TRUE
print(x, "is", y, "=", hasil)
print("nilai x = ", x, "id = ", hex (id(x)))
print("nilai x = ", y, "id = ", hex (id(y)))