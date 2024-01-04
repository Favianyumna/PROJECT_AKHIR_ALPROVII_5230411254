import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute(f"SELECT * FROM HEWAN WHERE Jenis = 'Mamalia' AND Asal = 'Sumatera'")
baris_table = kursor.fetchall()

print("Data hewan :")
print("================================================================================================")
print("{:<5} {:<20} {:<17} {:<13} {:<20} {:<20}".format("Id", "Nama_hewan", "Jenis", "Asal", "Jumlah_sekarang", "Tahun_ditemukan"))
print("=================================================================================================")
for baris in baris_table:
    print("{:<5} {:<20} {:<15} {:<18} {:<21} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()