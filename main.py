from kalkulator_ipk import Mapel, HitungIPK

while True:
    try:
        jumlah_semester = int(input("Jumlah semester: "))
        if jumlah_semester > 0:
            break
        print("Error: Jumlah semester harus lebih dari 0")
    except ValueError:
        print("Error: Input semester harus berupa angka")


def input_nilai(mapel):
    while True:
        try:
            val = int(input(f"Nilai {mapel}: "))
            if 0 <= val <= 100:
                return val
            print("Error: Nilai harus antara 0 - 100")
        except ValueError:
            print("Error: Nilai harus berupa angka")


kalkulator = HitungIPK()

for smt in range(1, jumlah_semester + 1):
    print(f"SEMESTER {smt} ")
    
    while True:
        try:
            jumlah_mapel = int(input("Jumlah mata pelajaran: "))
            if jumlah_mapel > 0:
                break
            print("Error: Jumlah mata pelajaran harus lebih dari 0")
        except ValueError:
            print("Error: Input jumlah mata pelajaran harus berupa angka")
    
    daftar_bobot_smt = []
    
    for i in range(1, jumlah_mapel + 1):
        nama_mapel = input(f"Nama mapel ke-{i}: ")
        nilai = input_nilai(nama_mapel)
        
        mapel_obj = Mapel(nama_mapel, nilai)
        daftar_bobot_smt.append(mapel_obj.bobot)

    ips = kalkulator.hitung_ips(daftar_bobot_smt)
    print(f"IPS Semester {smt}: {ips:.2f}")

ipk = kalkulator.hitung_ipk()

print("IPK:", round(ipk, 2))
print("Status:", kalkulator.cek_status(ipk))