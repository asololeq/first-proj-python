import json
import os

FILE_NAME = "catatan_pengeluaran.json"

def save_data(data):
  with open(FILE_NAME, "w") as file:
    json.dump(data, file)

def load_data():
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
      return json.load(file)
  else:
    return []
  
def bersihkan_layar():
  os.system("cls" if os.name == "nt" else "clear")

def menampilkan_pilihan():
  nama_project = "Selamat Datang di Overcial, mengatur Financial anda supaya tidak Over"
  pilihan_project = """Berikut Pilihan untuk Anda
  0. Keluar
  1. Atur Anggaran
  2. Tambah Catatan Pengeluaran
  3. Total Pengeluaran
  4. Total Anggaran Saat Ini
  5. Rata-rata Pengeluaran
  """
  print(nama_project)
  print(pilihan_project)

transaksi = []

while True:
  bersihkan_layar()
  menampilkan_pilihan()
  pilihan = int(input(f"Masukkan Pilihan Anda = "))

  match pilihan:
    case 1:
      bersihkan_layar()
      print("Mari Atur Anggaran Anda untuk Berapa Lama?")
      anggaran = int(input("Masukkan Nominal Anggaran Anda = Rp"))
      skala_anggaran = int(input("Masa Berlaku Anggaran (Masukkan dalam kelipatan hari) ="))
      target_pengeluaran = anggaran * (75/100) // skala_anggaran
      print(f"Target Pengeluaran Anda adalah Rp{target_pengeluaran:,} dalam 1 hari")
      print("")
      input("Tekan Enter untuk kembali ke menu")
    case 2:
      bersihkan_layar()
      print("Tambah Catatan Pengeluaran Anda")
      catatan = input("Buat Apa? ")
      nominal = int(input("Rp "))
      catatan_pengeluaran = {
          "Catatan" : catatan,
          "Nominal" : nominal
      }
      transaksi.append(catatan_pengeluaran)
      print("Pengeluaran Anda Berhasil ditambahkan")
      print("")
      input("Tekan Enter untuk kembali ke menu")
    case 3:
      bersihkan_layar()
      total_pengeluaran = 0
      for pengeluaran in transaksi:
        total_pengeluaran += pengeluaran["Nominal"]
      print(f"Total Pengeluaran Anda adalah Rp{total_pengeluaran}")
      print("")
      input("Tekan Enter untuk kembali ke menu")
    case 4:
      bersihkan_layar()
      if anggaran == 0:
        print("Anda Belum Mengatur Anggaran")
        print("")
        input("Silahkan tekan enter untuk melanjutkan dan pilih 1 untuk mengatur anggaran")
      else:
        total_anggaran = anggaran - total_pengeluaran
        print(f"Total Anggaran Anda Saat Ini adalah Rp{total_anggaran}")
        print("")
        input("Tekan Enter untuk kembali ke menu")
    case 5:
      bersihkan_layar()
      total_transaksi = len(transaksi)
      range_pengeluaran = total_pengeluaran // total_transaksi
      print(f"Anda mengeluarkan dana sebanyak Rp{range_pengeluaran:,} per hari")
      print("")
      input("Tekan Enter untuk kembali ke menu")
    case 0:
      bersihkan_layar()
      print("Terimakasih sudah menggunakan Overcial")
      break
    case _:
      bersihkan_layar()
      print("Pilihan Tidak Tersedia")
      print("")
      input("Tekan Enter untuk kembali ke menu")