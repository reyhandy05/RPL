class Mapel:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        self.bobot = self.ubah_ke_bobot(nilai)

    def ubah_ke_bobot(self, nilai):
        if nilai >= 85:
            return 4
        elif nilai >= 75:
            return 3
        elif nilai >= 65:
            return 2
        elif nilai >= 50:
            return 1
        else:
            return 0

class HitungIPK:
    def __init__(self):
        self.daftar_ips = []

    def hitung_ips(self, list_bobot):
        ips = sum(list_bobot) / len(list_bobot)
        self.daftar_ips.append(ips)
        return ips

    def hitung_ipk(self):
        return sum(self.daftar_ips) / len(self.daftar_ips)

    def cek_status(self, ipk):
        ipk_round = round(ipk, 2)
        if ipk_round == 4:
            return "Super Jenius!"
        elif ipk_round >= 3:
            return "Lulus"
        elif ipk_round >= 2:
            return "Lulus Secara Bersyarat"
        else:
            return "Gak Lulus"