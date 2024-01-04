import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN ORDER BY Tahun_ditemukan ASC") 
baris_table = kursor.fetchall()

print("Data Hewan:")
print("=============================================================================================")
print("{:<5} {:<20} {:<15} {:<13} {:<18} {:<10}".format("Id", "Nama_hewan", "Jenis", "Asal", "Jumlah_sekarang", "Tahun_ditemukan"))
print("=============================================================================================")
for baris in baris_table:
    print("{:<5} {:<20} {:<15} {:<18} {:<18} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()