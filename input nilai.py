from colorama import Fore, Style, init #pip install colorama
import time
init(autoreset=True)#instalisasi colorama
class Dosen:
    data_mahasiswa = 0
    def __init__(self,nama,nim,kelas,matkul,kehadiran,uts,uas):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.namaMatkul = matkul
        self.kehadiran = kehadiran
        self.uts = uts
        self.uas = uas

        Dosen.data_mahasiswa += 1
        
    def Tampil_data_mentah(self):
        print(f"Nama               : {self.nama}")
        print(f"NIM                : {self.nim}")
        print(f"Kelas              : {self.kelas}")
        print(f"Mata kuliah        : {self.namaMatkul}")
        print(f"Nilai Kehadiran    : {self.kehadiran}")
        print(f"Nilai UTS          : {self.uts}")
        print(f"Nilai UAS          : {self.uas}")

    def Konversi_nilai(self):
        Kehadiran = (self.kehadiran*10)/100
        UtS = (self.uts*40)/100
        UaS = (self.uas*50)/100
        
        koversi = Kehadiran+UtS+UaS
        return koversi

    def tampilkan_nilaiALLA_matkl(self):
        print("====NILAI MATKUL====")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Matkul  : {self.namaMatkul}")
        print(f"Nilai   : {self.Konversi_nilai()}")



def master():
    data_mahasiswa = []
    while True:

        print(Fore.BLUE+"\n"+"="*40)
        print(Fore.LIGHTGREEN_EX + "Silahkan pilih menu"+Style.RESET_ALL)
        print("1. Dosen")
        print("2. Mahasiswa")
        print("3. Keluar")
        print(Fore.BLUE+"="*40+Style.RESET_ALL)
        try:
            time.sleep(2)
            #user selects menu
            pilihan = int(input("Silahkan pilih menu (1-3) : "))

            if pilihan == 1 :
                #check options
                if input("Apakah anda yakin? (Y/N): ").strip().lower() not in ("y","yes","true","1"):
                    continue

                # input
                nama_mhs = input("Nama mahasiswa : ")
                nim_mhs = input("Nim mahasiswa : ").strip()
                kelas_mhs = input("Kelas mahasiswa : ")

                print("Data mahasiswa berhasil tersimpan!silahkan input nilai")
                nama_mtkl = input("Nama mata kuliah : ")
                
                try:
                    nilai_kehadiran = int(input("Nilai kehadiran : "))
                    nilai_uts = int(input("Nilai uts : "))
                    nilai_uas = int(input("Nilai UAS : "))

                    simpan = Dosen(nama_mhs,nim_mhs,kelas_mhs,nama_mtkl,nilai_kehadiran,nilai_uts,nilai_uas)
                    data_mahasiswa.append(simpan)

                    print(Fore.GREEN + "Data berhasil disimpan")
                    simpan.Tampil_data_mentah()
                except ValueError:
                    print(Fore.RED+"Silahkam masukkan angka"+Style.RESET_ALL)
                

            elif pilihan == 2 :
                # check options
                if input("Apakah anda yakin? (Y/N): ").strip().lower() not in ("y","yes","true","1"):
                    continue
                
                # check NIM 
                cek_NIM = input("Masukkan NIM anda : ").strip()
                mhs = next((m for m in data_mahasiswa if m.nim == cek_NIM),None)
                if mhs :
                    print(Fore.GREEN+"NIM ditemukan"+Style.RESET_ALL)
                    mhs.tampilkan_nilaiALLA_matkl()
                else:
                    print(Fore.RED+"NIM tidak ditrmukan"+Style.RESET_ALL)
                
            elif pilihan == 3:
                print(Fore.MAGENTA+"Terima kasih telah menggunakan layanan kami"+Style.RESET_ALL)
                break

            else:
                print(Fore.RED+"Pilihan tidak tersedia!"+Style.RESET_ALL)
                time.sleep(1)
            
        except ValueError : 
            print(Fore.RED+"Mohon masukkan angka"+Style.RESET_ALL)
if __name__ == "__main__":
    master()