# operasi logika dan boolean

# not,or,not

# NOT
print("===NOT===")
a = False
C = not a
print("data a = ", a)
print("------------------NOT")
print("data c = ", C)

# OR (jika salah satu true, hasilnya akan true)
print("====OR====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", C)
a = True
b = False
c = a or b
print(a, "OR", b, "=", C)
a = False
b = True
c = a or b
print(a, "OR", b, "=", C)
a = True
b = True
c = a or b
print(a, "OR", b, "=", C)

# AND (jika salah satu true, hasilnya true)
print("====AND====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", C)
a = True
b = False
c = a and b
print(a, "AND", b, "=", C)
a = False
b = True
c = a and b
print(a, "AND", b, "=", C)
a = True
b = True
c = a and b
print(a, "AND", b, "=", C)