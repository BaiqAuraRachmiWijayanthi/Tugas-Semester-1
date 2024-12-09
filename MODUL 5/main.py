# program untuk menentukan grade berdasarkan nilai 
nilai = float(input("masukan nilai anda (bisa desimal,misal 82.5):"))

if 90 <= nilai <= 100:
    grade = "A"
elif 81 <= nilai < 90:
    grade = "A-"
elif 75 <= nilai < 81:
    grade = "B+"
elif 70 <= nilai <75:
    grade = "B"
elif 65 <= nilai <70:
    grade = "C+"
elif 60 <= nilai < 65:
    grade = "C"
elif 55 <= nilai < 60:
    grade = "D"
elif 0 <= nilai < 55:
    grade = "E"
else :
    garde = "Nilai tidak valid"

print(f"Nilai Anda Adalah {nilai} dan grade Anda Adalah {grade}")