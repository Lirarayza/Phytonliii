KKM = 80
nama = input("masukkan nama : ")
kelas = input("masukkan kelas : ")
nilai = int(input("masukkan nilai : "))

if nilai >= KKM:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print(f"Nama Siswa : {nama}")
print(f"Kelas : {kelas}")
print(f"Nilai : {nilai}")
print(f"KKM : {KKM}")
print(f"Status : {status}")
